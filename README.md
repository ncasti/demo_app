# Audio Lessons

Short conversational-language audio lessons, inspired by the Duolingo-style audio lesson
format: bilingual hosts introduce a real-life dialogue, break down key phrases, have the
listener repeat them, then have the listener actually participate in the conversation.

Started as B1 French; now also includes an A1 Italian sample to test that the format and
production pipeline generalize across level and language.

## Pedagogy: no proactive phonetics, at any level

The original reference script (A1 French: bonjour/bonsoir/au revoir) uses phoneme-level
drilling — single sounds, then syllables, then words, with proactive pronunciation coaching
("notice how these sounds blend"). The Italian A1 script's **first draft** copied that
approach, on the theory that true beginners need it more than B1 learners do. It didn't hold
up: it burned most of the episode on English explanation and left too little room for actual
Italian content, and — separately — the fragment-isolation pattern ("bon-" / "-jour") that
worked fine when voiced by real bilingual actors doesn't render reliably through AI TTS at
all (confirmed the hard way: a bare "en" read with English phonetics even when the language
was explicitly forced).

The policy that replaced it, now applied at **every** level:
- Play the dialogue once at natural conversational speed (no slow first pass, no phoneme
  walkthrough).
- Break down **whole repertoire phrases** by meaning, not by sound — "Un caffè, per favore"
  means "a coffee, please," full stop. No "notice how these sounds blend."
- Skip proactive pronunciation coaching entirely. It becomes a later, *retroactive* layer:
  once a learner's own audio comes back through speech recognition, we can flag what actually
  went wrong instead of front-loading generic phonetic instruction before they've said a
  word.
- Where A1 differs from B1 isn't phonetics, it's **repetition and scope**: a true beginner
  still needs more speaking-challenge reps per phrase than a B1 learner, and an A1 episode
  should still end with a small, complete, real exchange (a full bar transaction, not endless
  isolated vocabulary) — B1 gets a free-response role-play beat on top of that, since it can
  assume more existing ability to construct a sentence unprompted.
- **Never isolate a chunk below 2-3 words**, and never leave a target-language word/phrase
  quoted inside an English-tagged chunk — both are AI-TTS production constraints, documented
  in `audio-gen/README.md`, that apply regardless of pedagogical level.

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
- `scripts/a1-it-01-buongiorno-al-bar.md` — A1 Italian: "Al bar," a full bar transaction
  (greet, order, thank) covering three repertoire phrases, no proactive phonetics.
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
