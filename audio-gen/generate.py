"""
Rough-voice-pass generator for audio lesson scripts.

Usage:
    export ELEVENLABS_API_KEY=sk_...
    python3 generate.py audio-gen/manifests/b1_fr_01_cafe.py [--out-dir out/]

Requires ffmpeg on PATH. Reads the API key from the ELEVENLABS_API_KEY env
var only -- never pass it on the command line or hardcode it here.
"""
import argparse
import importlib.util
import json
import os
import subprocess
import sys
import time
import urllib.request
import urllib.error

API_KEY = os.environ.get("ELEVENLABS_API_KEY")

ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
# SFX keys backed by a fixed, hand-picked asset file instead of a generation
# prompt. Chosen by the user from A/B'd AI-generated options plus a trimmed
# uploaded reference; this is a stock sound file they supplied, so licensing
# for real product use hasn't been independently verified -- flagged to the
# user at pick time, their call to proceed.
FIXED_SFX_ASSETS = {
    "SPEAKER_SFX": os.path.join(ASSETS_DIR, "sfx", "speaker_cue.mp3"),
    "CORRECT_SFX": os.path.join(ASSETS_DIR, "sfx", "correct_cue.mp3"),
    # Not referenced by any manifest yet -- today's scripts are linear
    # playback with no live grading, so there's no "wrong answer" branch to
    # cue. Registered now for when app-side/ASR grading can actually trigger
    # it, so it doesn't need to be re-picked later.
    "INCORRECT_SFX": os.path.join(ASSETS_DIR, "sfx", "incorrect_cue.mp3"),
    # A single consistent signature sting, used for both intro and outro on
    # every episode -- replaces the old per-episode AI-generated guitar/
    # mandolin prompt, which varied episode to episode and occasionally
    # rendered as a phrase that repeated within the clip. Chosen by the user
    # from several rounds of A/B'd ElevenLabs sound-generation candidates
    # (marimba/kalimba/glockenspiel/synth directions, then full-band
    # arrangements layering marimba, bass, percussion, and pad for texture);
    # the winning take had ~1.25s of trailing silence padding it out to the
    # requested duration, trimmed locally with a short fade-out.
    "INTRO_STING": os.path.join(ASSETS_DIR, "sfx", "intro_sting.mp3"),
    "OUTRO_STING": os.path.join(ASSETS_DIR, "sfx", "intro_sting.mp3"),
}

# eleven_v3 with an explicit language_code actually produces correct French
# phonetics. turbo_v2_5 accepted the same language_code param without error
# but silently ignored it for pronunciation purposes -- confirmed by direct
# A/B listening comparison, not just by the request succeeding. Don't
# downgrade this without re-verifying by ear; a 200 response proves nothing
# about which language actually came out.
TTS_MODEL_ID = "eleven_v3"
DEFAULT_SPEED = 0.92  # slightly slower than natural, for learner processing time
# Gap between language-switched chunks within one line is asymmetric on purpose:
# short going INTO a non-English chunk (don't make the listener wait through dead
# air before the French/Italian plays), longer coming OUT of one (give processing
# time afterward). Keyed off which language just finished, not which is next.
GAP_BEFORE_TARGET = 0.15
GAP_AFTER_TARGET = 0.55
# Minimum breathing room between two consecutive dialogue turns (different
# speakers or the same one) that don't already have an explicit "silence"
# segment between them in the manifest -- prevents back-to-back lines from
# sounding mashed together now that each clip's own padding is trimmed.
MIN_TURN_GAP = 0.35


def _post(url, payload, out_path, max_retries=4):
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"xi-api-key": API_KEY, "Content-Type": "application/json"},
        method="POST",
    )
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                with open(out_path, "wb") as f:
                    f.write(resp.read())
                return True
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")
            if e.code == 429 and attempt < max_retries - 1:
                wait = 2 ** attempt
                print(f"    rate limited, retrying in {wait}s...")
                time.sleep(wait)
                continue
            print(f"    FAILED ({e.code}): {body[:300]}")
            return False
        except Exception as e:
            print(f"    FAILED (exception): {e}")
            if attempt < max_retries - 1:
                time.sleep(2)
                continue
            return False
    return False


def tts(text, voice_id, lang, out_path):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    payload = {
        "text": text,
        "model_id": TTS_MODEL_ID,
        "language_code": lang,
        "voice_settings": {"stability": 0.55, "similarity_boost": 0.75, "speed": DEFAULT_SPEED},
    }
    return _post(url, payload, out_path)


def sound_fx(prompt, duration, out_path):
    url = "https://api.elevenlabs.io/v1/sound-generation"
    payload = {"text": prompt, "duration_seconds": min(duration, 30)}
    return _post(url, payload, out_path)


def get_sfx(key, prompt, duration, sfx_cache):
    if key in FIXED_SFX_ASSETS:
        asset_path = FIXED_SFX_ASSETS[key]
        if not os.path.exists(asset_path):
            print(f"    FAILED: fixed asset for '{key}' not found at {asset_path}")
            return None
        return asset_path
    os.makedirs(sfx_cache, exist_ok=True)
    cached_mp3 = os.path.join(sfx_cache, f"{key}.mp3")
    if not os.path.exists(cached_mp3):
        print(f"    generating SFX '{key}' ({duration}s): {prompt}")
        if not sound_fx(prompt, duration, cached_mp3):
            return None
    return cached_mp3


def ffprobe_duration(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", path],
        check=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
    )
    return float(out.stdout.decode().strip())


def make_silence(seconds, out_path):
    subprocess.run(
        ["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono",
         "-t", str(seconds), out_path],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )


def to_wav(in_path, out_path, gain_db=None, trim_silence=False):
    af_parts = []
    if trim_silence:
        # Strip leading dead air the TTS call baked in, so pacing into a line
        # is controlled by our own explicit gaps, not unpredictable padding.
        #
        # This used to ALSO trim trailing silence, via the same filter run a
        # second time on the reversed signal. Investigated a "last sound cut
        # off" report by measuring rather than guessing: at matched
        # pixels-per-second, spectrograms of raw vs. trailing-trimmed short
        # clips showed real energy running right up to the edge in BOTH --
        # meaning eleven_v3 often doesn't render a fade-out tail for a short
        # or isolated word, it just stops. With no safety margin to trim into,
        # any trailing trim risks shaving into the last audible sound, and a
        # short/bare-word clip (exactly the "one-off word" case reported) has
        # the least margin of all. A longer line with a real decay tail
        # (checked separately) wasn't meaningfully affected by trailing trim
        # either way, since duration=0 only ever removed ~15-30ms. So trailing
        # trim was doing little for pacing while carrying real cutoff risk --
        # removed rather than tuned. Pacing after a line is still controlled
        # by GAP_AFTER_TARGET/GAP_BEFORE_TARGET and MIN_TURN_GAP as before;
        # worst case a line now carries a bit of untrimmed raw tail (observed
        # up to ~600ms on one long-decay sample) rather than any risk of a
        # clipped ending.
        af_parts.append(
            "silenceremove=start_periods=1:start_duration=0:start_threshold=-45dB:start_silence=0.05"
        )
    if gain_db:
        af_parts.append(f"volume={gain_db}dB")
    af = ["-af", ",".join(af_parts)] if af_parts else []
    subprocess.run(
        ["ffmpeg", "-y", "-i", in_path, "-ar", "44100", "-ac", "1", *af, out_path],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )


def loop_trim_wav(in_path, seconds, out_path):
    subprocess.run(
        ["ffmpeg", "-y", "-stream_loop", "-1", "-i", in_path, "-t", str(seconds),
         "-ar", "44100", "-ac", "1", out_path],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )


def concat_wavs(wav_paths, out_path):
    list_file = out_path + ".txt"
    with open(list_file, "w") as f:
        for p in wav_paths:
            f.write(f"file '{os.path.abspath(p)}'\n")
    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", list_file, "-c", "copy", out_path],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )


def gen_line_wav(speaker, chunks, voices, out_dir, tag):
    """Generate one speaker line from a list of (lang, text) chunks, stitched together."""
    voice_id = voices[speaker]
    chunk_wavs = []
    for j, (lang, t) in enumerate(chunks):
        mp3_path = os.path.join(out_dir, f"{tag}_{j}_{lang}.mp3")
        wav_path = os.path.join(out_dir, f"{tag}_{j}_{lang}.wav")
        if not os.path.exists(mp3_path):
            if not tts(t, voice_id, lang, mp3_path):
                return None
            time.sleep(0.3)
        to_wav(mp3_path, wav_path, trim_silence=True)
        chunk_wavs.append(wav_path)
        if j < len(chunks) - 1:
            gap_path = os.path.join(out_dir, f"{tag}_{j}_gap.wav")
            gap = GAP_AFTER_TARGET if lang != "en" else GAP_BEFORE_TARGET
            make_silence(gap, gap_path)
            chunk_wavs.append(gap_path)
    combo_path = os.path.join(out_dir, f"{tag}_combo.wav")
    concat_wavs(chunk_wavs, combo_path)
    return combo_path


def build_scene(scene, voices, out_dir, idx, sfx_cache):
    """A scene = persistent ambience bed + accent stings at start/end, with the
    scene's dialogue lines layered on top at full volume for its whole length."""
    key = scene["key"]
    lines = scene["lines"]
    turn_gap = scene.get("turn_gap", 0.35)

    line_wavs = []
    for j, (speaker, text) in enumerate(lines):
        wav = gen_line_wav(speaker, [(scene.get("lang", "fr"), text)],
                            voices, out_dir, f"{idx:03d}_{key}_L{j}_{speaker}")
        if wav is None:
            return None
        line_wavs.append(wav)
        if j < len(lines) - 1:
            gap_path = os.path.join(out_dir, f"{idx:03d}_{key}_L{j}_turngap.wav")
            make_silence(turn_gap, gap_path)
            line_wavs.append(gap_path)

    dry_path = os.path.join(out_dir, f"{idx:03d}_{key}_dry.wav")
    concat_wavs(line_wavs, dry_path)
    dry_dur = ffprobe_duration(dry_path)

    lead = scene.get("lead", 0.9)
    tail = scene.get("tail", 1.3)
    total = lead + dry_dur + tail

    amb_mp3 = get_sfx(f"{key}_AMBIENCE", scene["ambience_prompt"], 30, sfx_cache)
    if amb_mp3 is None:
        return None
    amb_wav_raw = os.path.join(out_dir, f"{idx:03d}_{key}_amb_raw.wav")
    to_wav(amb_mp3, amb_wav_raw)
    amb_wav = os.path.join(out_dir, f"{idx:03d}_{key}_amb.wav")
    loop_trim_wav(amb_wav_raw, total, amb_wav)

    start_mp3 = get_sfx(f"{key}_START", scene["start_prompt"], scene.get("start_dur", 1.5), sfx_cache)
    end_mp3 = get_sfx(f"{key}_END", scene["end_prompt"], scene.get("end_dur", 1.8), sfx_cache)
    if start_mp3 is None or end_mp3 is None:
        return None
    start_wav = os.path.join(out_dir, f"{idx:03d}_{key}_start.wav")
    end_wav = os.path.join(out_dir, f"{idx:03d}_{key}_end.wav")
    to_wav(start_mp3, start_wav)
    to_wav(end_mp3, end_wav)
    end_offset = lead + dry_dur

    out_path = os.path.join(out_dir, f"{idx:03d}_{key}_scene.wav")
    filter_complex = (
        f"[0:a]volume=0.42,afade=t=in:st=0:d=1,afade=t=out:st={max(total - 1, 0):.2f}:d=1[amb];"
        f"[1:a]volume=0.9,adelay=0|0[start];"
        f"[2:a]volume=0.9,adelay={int(end_offset * 1000)}|{int(end_offset * 1000)}[end];"
        f"[3:a]volume=1.0,adelay={int(lead * 1000)}|{int(lead * 1000)}[dlg];"
        f"[amb][start][end][dlg]amix=inputs=4:duration=longest:normalize=0"
    )
    subprocess.run(
        ["ffmpeg", "-y",
         "-i", amb_wav, "-i", start_wav, "-i", end_wav, "-i", dry_path,
         "-filter_complex", filter_complex,
         "-ar", "44100", "-ac", "1", out_path],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    return out_path


def build_script(name, segments, voices, out_dir):
    sfx_cache = os.path.join(out_dir, "sfx_cache")
    os.makedirs(out_dir, exist_ok=True)
    wav_parts = []
    prev_kind = None
    print(f"=== {name}: {len(segments)} segments ===")

    for i, seg in enumerate(segments):
        idx = f"{i:03d}"
        kind = seg[0]

        # Two consecutive dialogue turns with no explicit silence/sfx/scene
        # between them used to rely on leftover TTS padding for a natural
        # breath -- now that each clip is silence-trimmed, that padding is
        # gone, so back-to-back turns need an explicit minimum gap or they
        # sound mashed together.
        if kind in ("speech", "speech_multi") and prev_kind in ("speech", "speech_multi"):
            gap_path = os.path.join(out_dir, f"{idx}_min_turn_gap.wav")
            make_silence(MIN_TURN_GAP, gap_path)
            wav_parts.append(gap_path)

        if kind == "silence":
            wav_path = os.path.join(out_dir, f"{idx}_silence.wav")
            make_silence(seg[1], wav_path)
            wav_parts.append(wav_path)

        elif kind == "sfx":
            _, key, prompt, duration = seg
            mp3 = get_sfx(key, prompt, duration, sfx_cache)
            if mp3 is None:
                print(f"!!! Stopping {name} at segment {idx}: SFX '{key}' failed.")
                return False
            wav_path = os.path.join(out_dir, f"{idx}_sfx_{key}.wav")
            gain = 4 if key == "SPEAKER_SFX" else (9 if key == "CORRECT_SFX" else None)
            to_wav(mp3, wav_path, gain_db=gain)
            wav_parts.append(wav_path)

        elif kind == "speech":
            _, speaker, text, lang = seg
            print(f"  [{idx}] {speaker}: {text[:60]}{'...' if len(text) > 60 else ''}")
            wav = gen_line_wav(speaker, [(lang, text)], voices, out_dir, f"{idx}_{speaker}")
            if wav is None:
                print(f"!!! Stopping {name} at segment {idx} due to failure.")
                return False
            wav_parts.append(wav)

        elif kind == "speech_multi":
            _, speaker, chunks = seg
            label = " / ".join(f"[{lang}] {t[:30]}" for lang, t in chunks)
            print(f"  [{idx}] {speaker} (multi): {label[:90]}")
            wav = gen_line_wav(speaker, chunks, voices, out_dir, f"{idx}_{speaker}")
            if wav is None:
                print(f"!!! Stopping {name} at segment {idx} due to failure.")
                return False
            wav_parts.append(wav)

        elif kind == "scene":
            _, scene = seg
            print(f"  [{idx}] SCENE '{scene['key']}': {len(scene['lines'])} lines, persistent ambience")
            wav = build_scene(scene, voices, out_dir, i, sfx_cache)
            if wav is None:
                print(f"!!! Stopping {name} at segment {idx}: scene '{scene['key']}' failed.")
                return False
            wav_parts.append(wav)

        else:
            raise ValueError(f"unknown segment kind: {kind}")

        prev_kind = kind

    final_wav = os.path.join(out_dir, f"{name}.wav")
    concat_wavs(wav_parts, final_wav)
    final_mp3 = os.path.join(out_dir, "..", f"{name}.mp3")
    subprocess.run(
        ["ffmpeg", "-y", "-i", final_wav, "-codec:a", "libmp3lame", "-qscale:a", "2", final_mp3],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    print(f"=== {name} done: {os.path.abspath(final_mp3)} ===\n")
    return True


def load_module(path):
    spec = importlib.util.spec_from_file_location("manifest", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", help="path to a manifest .py file (defines NAME, SEGMENTS, CAST)")
    parser.add_argument("--out-dir", default="out")
    args = parser.parse_args()

    if not API_KEY:
        print("ERROR: set ELEVENLABS_API_KEY in your environment first.")
        sys.exit(1)

    mod = load_module(args.manifest)
    build_script(mod.NAME, mod.SEGMENTS, mod.CAST, os.path.join(args.out_dir, mod.NAME))
