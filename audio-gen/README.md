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
   across lessons -- check `verified_languages` on `/v2/voices` first,
   and spot-check by ear if a language isn't explicitly verified.
3. Write a manifest in `manifests/` mirroring an existing one.
4. Run it. Cached SFX/lines mean a failed run resumes cheaply -- rerunning
   only regenerates what's missing from `out/<name>/`.
