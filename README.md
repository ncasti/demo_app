# Audio Lessons

Short conversational-language audio lessons, inspired by the Duolingo-style audio lesson
format: bilingual hosts introduce a real-life dialogue, break down key phrases, have the
listener repeat them, then have the listener actually participate in the conversation.

Started as B1 French; now also includes an A1 Italian sample to test that the format and
production pipeline generalize across level and language.

## Pedagogy: A1 vs. B1

The original reference script (A1 French: bonjour/bonsoir/au revoir) uses phoneme-level
drilling — single sounds, then syllables, then words, with proactive pronunciation coaching
("notice how these sounds blend"). That's the right call for true beginners with no base to
draw on, so the Italian A1 script keeps it.

At B1, learners already know the phonetics, so the French B1 scripts instead:
- Play the dialogue once at **natural conversational speed** (no slow first pass).
- Break down **chunks and idioms** ("ça fait un bail," "qu'est-ce que vous en pensez de...")
  rather than individual sounds.
- End with a **role-play beat**: the listener has to construct their own response to a new
  prompt, not just repeat a line back.
- Skip **proactive pronunciation coaching** entirely. Pronunciation feedback becomes a later,
  *retroactive* layer: once speech recognition is in the loop, we can detect actual
  mispronunciations from what a learner said and flag them after the fact, instead of
  front-loading generic phonetic instruction nobody asked for.

## Status

- [x] Step 1 — sample scripts drafted (`scripts/`)
- [x] Step 2 — audio generation pipeline built and working (`audio-gen/`) for the two French
      scripts: bilingual hosts, native-language dialogue voices, explicit per-chunk language
      locking (fixes cross-language mispronunciation), persistent scene ambience
- [ ] Italian A1 script written but **not yet rendered to audio** — ready to run, unverified
      by ear
- [ ] Sound effects/ambience: basic version done (persistent scene ambience, cue chimes,
      intro/outro sting) — not yet mixed/ducked professionally
- [ ] Later — exercises + porting into an interactive app

## Contents

- `scripts/b1-01-cafe-substitution.md` — B1 French: "Il n'en reste plus," handling an
  unavailable order at a bakery, accepting a substitution.
- `scripts/b1-02-catching-up-with-a-friend.md` — B1 French: "Ça fait un bail !," running into
  an old friend, making and adjusting plans.
- `scripts/a1-it-01-buongiorno-al-bar.md` — A1 Italian: "Buongiorno al bar," greeting the
  barista, phoneme-level drilling in the reference script's original style.
- `audio-gen/` — the generation pipeline (ElevenLabs TTS + sound-generation) and one manifest
  per script. See `audio-gen/README.md` for how it works and how to add a new language/lesson.
- `research/tts-options.md` — bilingual TTS vendor research from before we settled on
  ElevenLabs.

## Next steps

1. Listen to the Italian sample script's audio once rendered (`audio-gen/manifests/a1_it_01_bar.py`)
   and confirm the shared Clara/Max host voices hold up in a third language.
2. Decide whether ambience should duck under dialogue (lower automatically while a host/
   character is speaking) rather than sit at a constant background level.
3. Design the actual speaking-exercise grading/interactivity layer (speech recognition +
   retroactive pronunciation feedback), then port into an app.
