# B1 French Audio Lessons

5-minute conversational-French audio lessons for B1 (intermediate) learners, inspired by the
Duolingo-style audio lesson format: bilingual hosts introduce a real-life dialogue, break down
key "repertoire phrases," have the listener repeat them, then have the listener actually
participate in the conversation.

## What's different from the A1 reference script

The reference script this project is inspired by teaches A1 material (bonjour/bonsoir/au
revoir) with phoneme-level drilling (single sounds, then syllables, then words). At B1, learners
already have those basics, so these scripts instead:
- Play the dialogue once at **natural conversational speed** (no slow first pass).
- Break down **chunks and idioms** ("ça fait un bail," "qu'est-ce que vous en pensez de...")
  rather than individual sounds.
- End with a **role-play beat**: the listener has to construct their own response to a new
  prompt, not just repeat a line back.

## Status

- [x] Step 1 — 2 sample scripts drafted (`scripts/`)
- [ ] Step 2 — generate audio with bilingual hosts + native French dialogue voices
- [ ] Step 3 — add sound effects / ambience
- [ ] Later — exercises + porting into an interactive app

## Contents

- `scripts/b1-01-cafe-substitution.md` — "Il n'en reste plus": handling an unavailable order
  at a bakery, accepting a substitution.
- `scripts/b1-02-catching-up-with-a-friend.md` — "Ça fait un bail !": running into an old
  friend, making and adjusting plans.
- `research/tts-options.md` — bilingual TTS vendor research and recommendation for step 2.

## Next steps

1. Review the two scripts — flag anything that reads wrong, too easy/hard, or off-tone.
2. Once approved, generate a rough voice pass (see `research/tts-options.md` for the
   recommended approach) so we can hear pacing and tone before investing in polish.
3. Layer in SFX/ambience per the `[SFX]`/`Audio` cues already in the scripts.
