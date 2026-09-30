# Script-writing guidelines

A living reference for writing `scripts/*.md`, distilled from the user's review feedback over
time. When they give feedback on a script, the specific fix goes in that script; the
generalizable rule behind it belongs here too, so future scripts don't need the same
correction twice.

This is separate from `audio-gen/README.md`'s "production rules" (trailing periods, bare-word
isolation, English/target-language leakage) -- those are mechanical TTS-rendering constraints,
checked automatically by `audio-gen/lint_manifest.py`. This file is about the script's content
and pedagogy -- judgment calls a linter can't make.

**Notation:** mark a word/phrase that should be spoken in Italian inside otherwise-English text
as `[it]...[/it]` (e.g. an Italian "bar" is nothing like an English one). This is a script
annotation only -- it never reaches the manifest or gets read aloud; it just tells whoever
writes the manifest to isolate that span into its own `("it", ...)` chunk instead of leaving it
inside an `("en", ...)` chunk.

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
- **The very first episode needs more upfront framing than later ones.** Jumping straight into
  the scene works once the listener already knows the show's format; episode 1 should tell
  them what they're about to learn first (e.g. "this is our first episode, so today we'll
  start with the basics — greetings, and ordering a coffee") before cutting to the dialogue.
- **Generalizations need one concrete example, not just an assertion.** "Add 'per favore' and
  it works everywhere" is abstract -- follow it with an actual substitution using a
  recognizable word or cognate the listener can map onto anything else ("Try it with
  anything — 'Un tè, per favore.'"). This is the same substitution-drill instinct as the
  chapter structure, applied to a one-line aside, not just a full drilled phrase.

## Content consistency

- **Name things the same way throughout one episode.** Don't call the same place/person/thing
  two different names in adjacent lines (caught: an episode said "Florence" in one line and
  "Firenze" in the next; another said "Rome" and "Roma" for the same destination). Pick one
  name per language context and stick to it for the whole episode.
- **The "next time" preview must match the actual next episode's topic.** Don't preview a
  topic from a later episode, and don't invent unsupported framing to justify it (caught:
  episode 1's outro said "next time, the part everyone forgets to learn — asking prices,"
  which was episode 3's topic, not episode 2's, and "everyone forgets to learn this" wasn't
  grounded in anything). Check the very next episode's actual scope before writing this line.
- **A vocabulary word under discussion is spoken in its own language, not translated.** When
  a line explains a false-friend or loanword (e.g. Italian "bar" isn't an English bar), the
  word itself should be spoken in the target language even inside English narration, not
  read with English phonetics -- it's the word being taught, not an English word that happens
  to be spelled the same. Isolate it into its own chunk like any other target-language
  mention (see `audio-gen/README.md`'s production rules); add it to `lint_manifest.py`'s
  `SAFE_BARE_WORDS` if it's a standalone noun the linter would otherwise flag.

## Process notes

- **Revisit old workarounds when their underlying constraint changes.** Episode 1 doubled
  "Ottimo" and "Prego" in narration to dodge the bare-single-word isolation rule, before
  `SAFE_BARE_WORDS` existed. Once both words were added to that allowlist, the doubling was
  obsolete and just sounded redundant on a listen -- worth a periodic check for other
  workarounds that outlived the reason they were added, not just new violations.

## Open items

Nothing queued yet -- add new rules here as review feedback surfaces them.
