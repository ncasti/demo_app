# Audio generation pipeline

Rough-voice-pass generator used to render lesson scripts (`../scripts/*.md`) into
listenable audio, via ElevenLabs (TTS + sound-generation for SFX/ambience).

## Usage

```bash
export ELEVENLABS_API_KEY=sk_...   # never commit this, never pass it as an arg
python3 generate.py manifests/b1_fr_01_cafe.py --out-dir out/
```

Requires `ffmpeg` on `PATH`. Output lands at `out/<script-name>.mp3`.

**Caution when editing a manifest you've already generated once:** per-segment cache files
are keyed by position (`out/<script-name>/<index>_...`), not by content. If you insert,
remove, or reorder a segment and rerun without clearing `out/<script-name>/` first, later
segments can silently reuse a stale cached clip from the old position instead of regenerating
-- this happened while fixing episode 1's cue order (the fix produced zero new API calls
until the stale directory was deleted). `rm -rf out/<script-name> out/<script-name>.mp3`
before rerunning after any structural edit; a pure text/wording tweak to an existing segment
is safe to rerun without clearing, since that segment's own cache file just gets overwritten.
The same applies to `sfx_cache/INTRO_STING.mp3`/`OUTRO_STING.mp3` specifically: the cache key
is the fixed filename, not the prompt text, so changing the prompt (e.g. the anti-repeat
wording added below) does nothing on a rerun unless that cached file is deleted too.

## Known fixes worth knowing about

- **Dead air after "Repeat after Max/Clara."**: episodes 1 through 25 all had a manually
  inserted `("silence", 3.0)` (3.5 in the French scripts) directly after that instruction
  line, before Max/Clara actually modeled the phrase again. That's pure dead air -- nothing
  happens between the instruction and the model saying the phrase. Removed across every
  manifest; the instruction line and the modeled phrase are both `speech` segments with
  nothing explicit between them now, so `MIN_TURN_GAP` (0.35s) provides the breath instead of
  a 3-second silence.
- **Intro/outro stings sounding like they play twice**: the AI-generated jingle prompt never
  said the phrase should play only once, and a ~3.5s "podcast intro jingle" prompt often came
  back as a short musical phrase repeated within the clip -- confirmed by eye on a waveform
  (two near-identical swells of amplitude). Prompt now explicitly says "played once only,
  does not loop or repeat." Existing episodes won't pick this up without clearing their cached
  `INTRO_STING.mp3`/`OUTRO_STING.mp3` first (see caution above) and rerunning.
- **Trailing silence trim risked cutting the last sound off a word**: `to_wav(...,
  trim_silence=True)` used to run the same `silenceremove` filter on both ends (trimming the
  tail via the reverse-trim-reverse trick). Investigated a "word gets cut off" report by
  measuring rather than guessing -- swept `start_duration`/`start_threshold`/`start_silence`
  against real cached clips, and at matched pixels-per-second, spectrograms of raw vs.
  trailing-trimmed short clips showed real energy running right up to the edge in both: a
  short or isolated word from eleven_v3 often doesn't render a fade-out tail, it just stops.
  With no safety margin to trim into, trailing trim risked shaving into the last audible
  sound, worst on exactly the short/bare-word clips that were reported as cut off. A
  longer line with a real decay tail (checked separately) wasn't meaningfully affected by
  trailing trim either way, since it only ever removed ~15-45ms. So trailing trim was doing
  little for pacing while carrying real cutoff risk on the clips most likely to need every
  millisecond -- removed rather than tuned; only leading silence is trimmed now. Pacing after
  a line is still controlled by `GAP_AFTER_TARGET`/`GAP_BEFORE_TARGET`/`MIN_TURN_GAP`, so a
  line may now carry a little untrimmed raw tail (observed up to ~600ms on one long-decay
  sample) instead of any risk of a clipped ending.

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
    together — this is what fixes cross-language mispronunciation versus
    letting the model guess from mixed-language text. Each chunk's own
    leading/trailing silence is trimmed before stitching (TTS output pads
    unpredictably otherwise), then a deliberate gap is inserted: short
    (`GAP_BEFORE_TARGET`) going into a non-English chunk so there's no dead
    air before it, longer (`GAP_AFTER_TARGET`) coming out of one so there's
    processing time afterward. When writing the English text around a
    chunk, don't refer to it as "that word" if the chunk is actually a
    multi-word phrase (e.g. "en" surfacing as "n'en reste plus") — name the
    target word explicitly in the English narration, then introduce the
    audio as "right here in ..." so it's clear the phrase, not the word
    alone, is what plays.
  - `("silence", seconds)` — a pause
  - `("sfx", key, prompt, duration)` — a short generated sound effect,
    cached by `key` so repeated cues (e.g. the correct-answer chime) are only
    generated once. A key can instead be backed by a fixed local file (see
    `FIXED_SFX_ASSETS` near the top of `generate.py`) instead of a generation
    prompt -- used for `SPEAKER_SFX`, which is a specific sound the user
    picked from A/B'd options, not something to regenerate from a prompt.
  - **"Listen in" transition convention**: any time the script cuts from the
    hosts to native-speaker-only audio *that isn't already wrapped in a
    `scene`* (e.g. a quick montage of different voices saying the same
    phrase), insert a short `sfx` cue right before it — a brief ambient
    swell, like tuning into a real conversation — so the listener gets an
    audible signal that they've left the "teaching booth" and are now
    listening in on real people. `scene` blocks already get this via their
    own start/end accent sounds; standalone voice-montage moments don't, so
    they need it added explicitly. See `LISTEN_IN_STING` in
    `a1_it_01_bar.py` for the pattern.
  - `("scene", scene_dict)` — a block of back-and-forth dialogue with
    **persistent background ambience** mixed underneath it for the scene's
    full duration (not just bookend stingers), plus a short accent sound at
    the very start and end (a door chime, footsteps, etc.)

## Notes on model choice

Uses `eleven_v3` with an explicit `language_code` per call, not
`eleven_multilingual_v2`'s auto-detection — auto-detect is unreliable on short
or ambiguous tokens embedded in the other language's sentence.

**History, because this took two wrong turns to get right:**
1. Started on `eleven_multilingual_v2`, relying on its auto-detection. Worked
   for full sentences, mispronounced short embedded words as English (e.g. a
   bare "en" read with English phonetics).
2. Switched to `eleven_turbo_v2_5` with an explicit `language_code` field,
   assuming that would force correct pronunciation. It didn't: the API
   accepted the parameter and returned 200 every time, but a direct A/B
   listening comparison (turbo vs. v3 vs. a native voice, same line) showed
   turbo was still not using French phonetics — the field was silently
   ignored for pronunciation purposes. **A successful response proves
   nothing about which language actually came out; only listening does.**
3. `eleven_v3` with the same `language_code` field actually respects it —
   confirmed by ear, not just by the request succeeding.

Forcing the language alone still wasn't enough for a *bare single word*
("en", "va", "tu", "bail") — the model has too little signal to know what
it's saying even once it knows what language it's in. ElevenLabs does
support IPA/CMU pronunciation dictionaries for this (only on
`eleven_flash_v2`/`eleven_v3`; non-English requires `eleven_v3`
specifically), but authoring correct IPA for a language you can't personally
proofread by ear is its own risk, and doesn't fix the underlying problem the
way just not isolating a bare word does.

**The actual rule: never isolate a chunk below 2-3 words.** Every
`speech_multi` chunk should be pulled from a natural phrase that already
appears (or naturally could appear) elsewhere in the script — e.g. don't
isolate "en", use "n'en reste plus" or "vous en pensez"; don't isolate "va",
use "ça me va". Full phrases carry enough context for the model to get right
every time; single words don't, no matter what language you force.

**Second rule, easy to miss on a first pass: a target-language word quoted
inside an English-tagged chunk still gets read with English phonetics.**
The chunk's `lang` governs the *whole* chunk, so `("en", "That word you
heard — \"buongiorno\" — means...")` mispronounces "buongiorno" exactly the
same way an isolated bare word does, even though it's sitting inside a much
longer sentence. This bit the Italian script even after the bare-word rule
above was already applied there — every English narration line needs a
pass to find quoted target-language words/phrases and pull each one out
into its own `("it", ...)` (or whatever the language is) chunk via
`speech_multi`, the same way the French scripts do it. Do this pass on the
whole script before generating, not reactively per complaint — it's the
same fix every time.

This constraint does **not** apply to the A1-style phoneme/syllable
breakdown pattern (e.g. "buon-" / "-giorno") used for true-beginner scripts —
that's a different, harder problem. The original reference script's A1
lessons were voiced by real bilingual actors who could deliberately hit an
isolated fragment on request; an AI TTS model doesn't have that same
context-free control. Don't assume a syllable-fragment manifest (see
`a1_it_01_bar.py`) will render cleanly via direct TTS the same way a
full-phrase one does -- it may need a different production method (e.g.
synthesize the *whole* word once, then trim the syllable boundary out of that
single clean take in post, rather than asking the model to speak a bare
fragment on its own).

## Adding a new language/lesson

1. Write the script as a `.md` file in `../scripts/`, following the existing
   format (see `../README.md` for the A1-vs-B1 pedagogy differences).
2. Pick voices: ElevenLabs' `/v1/shared-voices?language=<code>` search
   surfaces native voices for dialogue characters. Reuse the existing
   Clara/Max voice IDs for hosts where possible, for brand consistency
   across lessons -- but check `verified_languages` on `/v2/voices` for the
   target language code **before** committing to that voice, don't just spot
   check after the fact. This bit the Italian episode: Chris (used for Max
   in French) has no `it` entry in `verified_languages` at all, and his
   Italian lines -- especially bare words like "Prego" -- intermittently
   came out with English phonetics, confirmed by ear. Missing
   `verified_languages` for a language isn't a soft risk to keep an eye on,
   it's a real predictor of wrong-language pronunciation. If a host's
   regular voice isn't verified for the new language, don't ship it and
   hope -- swap in a voice that is (see `a1_it_01_bar.py`'s Max, swapped to
   Vittorio for Italian). The character name is the consistent brand
   element across languages; the underlying voice doesn't have to be, the
   same way a recurring character gets a different voice actor per
   language in dubbing.
3. Write a manifest in `manifests/`, building the repeat-after-me /
   reverse-translate / round-trip drill blocks with `lesson_segments.py`'s
   `speaking_challenge()`, `reverse_translate_item()`, and `roundtrip_step()`
   rather than hand-copying the segment tuples -- that module's docstring
   explains why (episodes 1-2 shipped with a real bug in those shapes before
   they were centralized). Everything else in a manifest -- intro banter,
   scene dialogue, phrase-breakdown narration, recap -- is unique content
   and stays hand-written.
4. Run it. Cached SFX/lines mean a failed run resumes cheaply -- rerunning
   only regenerates what's missing from `out/<name>/`.
