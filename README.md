# Audio Lessons

Short conversational-language audio lessons, inspired by the Duolingo-style audio lesson
format: bilingual hosts introduce a real-life dialogue, break down key phrases, have the
listener repeat them, then have the listener actually participate in the conversation.

Started as B1 French; now also includes a 25-episode A1 Italian arc (new-scenario episodes
plus a spaced-repetition practice episode after every 2-3 new ones) to test that the format
and production pipeline generalize across level, language, and episode count.

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
- [x] Step 2 — audio generation pipeline built and working (`audio-gen/`) for all 27 scripts
      (2 French + 25 Italian): bilingual hosts, native-language dialogue voices, explicit
      per-chunk language locking on `eleven_v3` (fixes cross-language mispronunciation),
      persistent scene ambience
- [x] Italian A1 episode rendered — first real test of the pipeline on a new language,
      confirmed working end to end
- [x] Scaling test, round 1 — 4 more Italian episodes (introductions, market, a
      spaced-repetition practice episode, directions), applying every lesson from episode 1
      up front (voice `verified_languages` checked before writing dialogue, correct
      speak/reveal cue ordering, no bare-word isolation)
- [x] Scaling test, round 2 — 15 more Italian episodes (6-20: 10 new scenarios + 5 practice
      episodes), all generated in one pass. Factored the repeat-after-me / reverse-translate
      / round-trip block shapes into `audio-gen/lesson_segments.py` once the pattern proved
      stable across 5 episodes, rather than hand-copying them 15 more times — the shared
      module is also where the episode-1/2 SPEAKER_SFX-ordering bug got fixed once instead of
      per episode. Character voices reused across scenarios (a small recurring native cast)
      rather than researching new ones per episode.
- [x] Scaling test, round 3 — 5 more Italian episodes (21-25: clarification phrases, family,
      a practice episode, age/birthdays, taxis), same process as round 2. Total run across all
      three rounds used ~56k of a 121k/month character quota, so quota is not the constraint
      on scaling further.
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
- `scripts/a1-it-02-piacere.md` — A1 Italian: "Piacere!," introducing yourself.
- `scripts/a1-it-03-quanto-costa.md` — A1 Italian: "Quanto costa?," asking for something and
  its price at a market stall.
- `scripts/a1-it-04-practice-uno.md` — A1 Italian: first spaced-repetition practice episode,
  recombining episodes 1-3 into one "day in Italy" with no new vocabulary.
- `scripts/a1-it-05-scusi-dove.md` — A1 Italian: "Scusi, dov'è...?," asking for directions.
- `scripts/a1-it-06-che-ore-sono.md` through `a1-it-20-practice-sei.md` — 15 more A1 Italian
  episodes (time, restaurant, weather, asking for help, phone calls, train tickets, clothes
  shopping, likes/dislikes, hotel check-in, small talk, and five practice episodes spaced
  through the run) — see each script's Production notes for scenario-specific choices.
- `scripts/a1-it-21-non-capisco.md` through `a1-it-25-prendo-un-taxi.md` — 5 more A1 Italian
  episodes (clarification phrases, family, a practice episode, age/birthdays, taxis).
- `audio-gen/` — the generation pipeline (ElevenLabs TTS + sound-generation), one manifest per
  script, and `lesson_segments.py` (shared speaking-challenge / reverse-translate /
  round-trip block builders, factored out once the pattern proved stable). See
  `audio-gen/README.md` for how it works and how to add a new language/lesson.
- `research/tts-options.md` — bilingual TTS vendor research from before we settled on
  ElevenLabs.

## Next steps

1. Decide whether ambience should duck under dialogue (lower automatically while a host/
   character is speaking) rather than sit at a constant background level.
2. Design the actual speaking-exercise grading/interactivity layer (speech recognition +
   retroactive pronunciation feedback), then port into an app.
3. Revisit the French episodes with the lessons learned from scaling Italian (per-voice
   `verified_languages` check up front, correct speak/reveal cue ordering) for consistency.
