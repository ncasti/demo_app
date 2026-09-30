# Script-writing guidelines

A living reference for writing `scripts/*.md`, distilled from the user's review feedback over
time. When they give feedback on a script, the specific fix goes in that script; the
generalizable rule behind it belongs here too, so future scripts don't need the same
correction twice.

This is separate from `audio-gen/README.md`'s "production rules" (trailing periods, bare-word
isolation, English/target-language leakage) -- those are mechanical TTS-rendering constraints,
checked automatically by `audio-gen/lint_manifest.py`. This file is about the script's content
and pedagogy -- judgment calls a linter can't make.

## Process

**Every new or edited episode gets written/updated as a script first, reviewed and approved by
the user, before any audio is generated.** Write or revise `scripts/<name>.md`, present it for
review, incorporate feedback, and only build the manifest and run `generate.py` once approved.
Don't generate audio speculatively "to see how it sounds" -- API calls and the user's listening
time both cost more than a text review round does.

## Pedagogy

- **No proactive phonetics, at any level.** Play the dialogue once at natural conversational
  speed. Break down whole repertoire phrases by meaning ("Un caffè, per favore" = "a coffee,
  please"), never by sound. No "notice how these sounds blend." Pronunciation coaching is a
  later, retroactive layer once real speech-recognition feedback exists -- not front-loaded
  generic instruction before the learner has said a word.
- **A1 vs. B1 differs in repetition and scope, not phonetics.** A1 needs more speaking-challenge
  reps per phrase. Every episode should end with a small, complete, real exchange (a full
  transaction, not isolated vocabulary) -- B1 adds a free-response role-play beat on top, since
  it can assume more ability to construct a sentence unprompted.
- **Chapters, not forced single-shot episodes.** A topic spans however many episodes it
  actually needs -- typically 1-2, occasionally 3 if the back-and-forth genuinely grows that
  long. Don't pad a topic to a fixed part count; let the content decide.
- **Substitution drills, not verbatim repeats.** Each new phrase gets drilled once as taught,
  then again with a substitution variant in the same slot (table for two -> also table for
  three; a ticket to Rome -> also to Milan) -- production, not just recall of one fixed
  sentence.
- **Inline review uses fresh fillers.** A chapter's later episode reviews the previous
  episode's phrases with *new* substitution fillers, not the exact phrase heard before, so it
  tests the pattern rather than rote memory.
- **Practice-episode density should track the registry, not a fixed cadence.** Run
  `audio-gen/registry_tools.py overdue --top 8` before writing a practice episode's review
  section, rather than defaulting to "the last 2-3 episodes."

## Content consistency

- **Name things the same way throughout one episode.** Don't call the same place/person/thing
  two different names in adjacent lines (caught: an episode said "Florence" in one line and
  "Firenze" in the next; another said "Rome" and "Roma" for the same destination). Pick one
  name per language context and stick to it for the whole episode.

## Open items

Nothing queued yet -- add new rules here as review feedback surfaces them.
