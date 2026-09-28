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
draw on, so the Italian A1 script keeps that teaching approach. The *audio production* of it
had to adapt, though: the reference script's fragments ("bon-" / "-jour") were voiced by real
bilingual actors who could deliberately hit an isolated syllable on request. AI TTS can't do
that reliably — confirmed the hard way on the French scripts (a bare "en" read with English
phonetics even when the language was forced), then designed around it for Italian from the
start: every Italian audio chunk is a complete real word ("giorno," "Buongiorno") and the
syllable-by-syllable teaching happens in English narration around it, not as isolated
fragments.

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
- [x] Step 2 — audio generation pipeline built and working (`audio-gen/`) for all three
      scripts (2 French + 1 Italian): bilingual hosts, native-language dialogue voices,
      explicit per-chunk language locking on `eleven_v3` (fixes cross-language
      mispronunciation), persistent scene ambience
- [x] Italian A1 episode rendered — first real test of the pipeline on a new language,
      confirmed working end to end
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

1. Confirm the shared Clara/Max host voices hold up in Italian by ear (Chris/Max isn't
   explicitly ElevenLabs-verified for Italian, unlike Matilda/Clara).
2. Decide whether ambience should duck under dialogue (lower automatically while a host/
   character is speaking) rather than sit at a constant background level.
3. Design the actual speaking-exercise grading/interactivity layer (speech recognition +
   retroactive pronunciation feedback), then port into an app.
