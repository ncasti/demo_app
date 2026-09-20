# Audio generation pipeline

Rough-voice-pass generator used to render lesson scripts (`../scripts/*.md`) into
listenable audio, via ElevenLabs (TTS + sound-generation for SFX/ambience).

## Usage

```bash
export ELEVENLABS_API_KEY=sk_...   # never commit this, never pass it as an arg
python3 generate.py manifests/b1_fr_01_cafe.py --out-dir out/
```

Requires `ffmpeg` on `PATH`. Output lands at `out/<script-name>.mp3`.

## How a manifest works

Each file in `manifests/` defines three things:
- `NAME` — output filename stem
- `CAST` — `{speaker: elevenlabs_voice_id}`
- `SEGMENTS` — an ordered list of beats. Segment kinds:
  - `("speech", speaker, text, lang)` — one line, one language (`lang` is
    "en"/"fr"/"it"/... and is passed to ElevenLabs as an explicit
    `language_code` — required so short/ambiguous words don't get
    mispronounced in the wrong language)
  - `("speech_multi", speaker, [(lang, text), ...])` — one line that mixes
    languages (e.g. an English sentence with a French phrase embedded).
    Each chunk is a separate TTS call in its own language, stitched back
    together with a short gap — this is what fixes cross-language
    mispronunciation versus letting the model guess from mixed-language text.
  - `("silence", seconds)` — a pause
  - `("sfx", key, prompt, duration)` — a short generated sound effect,
    cached by `key` so repeated cues (e.g. the correct-answer chime) are only
    generated once
  - `("scene", scene_dict)` — a block of back-and-forth dialogue with
    **persistent background ambience** mixed underneath it for the scene's
    full duration (not just bookend stingers), plus a short accent sound at
    the very start and end (a door chime, footsteps, etc.)

## Notes on model choice

Uses `eleven_turbo_v2_5` with an explicit `language_code` per call, not
`eleven_multilingual_v2`'s auto-detection — auto-detect is unreliable on short
or ambiguous tokens (a bare "en", a bare "va") embedded in the other
language's sentence. Forcing the language explicitly fixed that.

## Adding a new language/lesson

1. Write the script as a `.md` file in `../scripts/`, following the existing
   format (see `../README.md` for the A1-vs-B1 pedagogy differences).
2. Pick voices: ElevenLabs' `/v1/shared-voices?language=<code>` search
   surfaces native voices for dialogue characters. Reuse the existing
   Clara/Max voice IDs for hosts where possible, for brand consistency
   across lessons -- check `verified_languages` on `/v2/voices` first,
   and spot-check by ear if a language isn't explicitly verified.
3. Write a manifest in `manifests/` mirroring an existing one.
4. Run it. Cached SFX/lines mean a failed run resumes cheaply -- rerunning
   only regenerates what's missing from `out/<name>/`.
