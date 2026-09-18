# Bilingual TTS options for B1 Audio Lessons

The core requirement: **Clara and Max each need to sound like one consistent person**
across English narration and French phrases in the same lesson — not two different voices
stitched together, and not an English speaker doing a French accent. The scenario dialogue
voices (Client/Boulanger, Léa/Camille) are a simpler problem — those are pure monolingual
French clips, so any good native French voice works.

## The real constraint

Most TTS vendors (classic Amazon Polly, standard Google Cloud voices, most of PlayHT) tie a
voice to a single locale. To get a "bilingual" host with those, you'd generate the English
lines with one voice/locale and the French lines with a *different* voice, then hope they sound
like the same person. They usually don't.

Two vendors are actually built for this:

### 1. Azure AI Speech — "Multilingual" / Dragon HD Omni voices (recommended for hosts)
- Voices literally named `...MultilingualNeural` (or the newer Dragon HD Omni voices — Ava,
  Andrew, Emma, Brian, Florian, Seraphina, Remy, Vivienne, Xiaoxiao) keep **one voice identity**
  across languages with automatic language detection — no accent-swap, no separate voice ID.
- You can feed it a script that's mostly English with French phrases inline, or full French
  lines, and it holds the same timbre and switches pronunciation/prosody appropriately.
- Largest locale/voice catalog of any vendor (600+ voices, 150+ locales) if you also want a wide
  pool of distinct native French voices for the dialogue-clip characters.
- Price cut on Neural HD voices (~$22/1M characters as of March 2026) makes the premium tier
  cheaper than Google's equivalent.
- **Best fit for**: Clara & Max's host lines, which are genuinely bilingual within a lesson.

### 2. ElevenLabs — multilingual model + expressive "audio tags"
- Same voice ID produces consistent timbre across languages (multilingual model, not per-locale
  voices) — also a valid pick for bilingual hosts.
- Its standout feature for *this specific script format*: **inline audio tags** like `[laughing]`,
  `[sighs]`, `[whispers]`, `[excited]` for delivery control — which map almost one-to-one onto the
  bracketed stage directions already in these scripts (`[laughing]`, `[smiling]`, `[mock outrage]`,
  `[relieved]`, `[panicked]`). That's a meaningful production-time win: less manual SSML tuning.
- Caveat: **true mid-sentence** code-switching (a French word dropped into the middle of an
  English sentence) is "hit or miss" per current guidance — mitigated by either (a) adding
  explicit language tags to force the boundary, or (b) generating short segments and
  concatenating. In practice, our scripts already switch at line/sentence boundaries almost
  everywhere (e.g., "Il n'en reste plus" — "Qu'est-ce que vous en pensez de..." — "Pourquoi pas !"
  are each full French sentences), so this caveat rarely bites us.
- Enormous voice library for casting the native French dialogue characters too.

### 3. Gradium — worth a look, more niche
- Purpose-built for native mid-sentence code-switching across EN/FR/DE/ES/PT, no config needed.
- Newer/smaller vendor than the two above — good as a fallback or A/B test if Azure/ElevenLabs
  output on a mixed-language line ever sounds off, but not where I'd start.

## Recommendation

- **Hosts (Clara & Max):** start with **ElevenLabs** — the audio-tag support is a direct match
  for this script's stage directions, and our line-level (not mid-word) language switching avoids
  its main weak spot. Azure's Multilingual/Dragon HD Omni voices are the strong second choice,
  and worth an A/B test if ElevenLabs' French pronunciation on a given line isn't clean.
- **Dialogue-clip characters (Client/Boulanger, Léa/Camille, street voices):** pick distinct
  native French voices from either vendor's library — no code-switching needed here, so it's
  purely a casting/quality choice. Both vendors have deep French voice catalogs.
- **Practical workflow either way:** generate per-line (or per-turn) audio clips rather than one
  giant multi-speaker render, then assemble/mix in an audio tool — gives control over pacing,
  the `[PAUSE]`/`[SFX]` cues, and lets you swap a single bad line without re-rendering the whole
  lesson.

## Open questions for you
1. Budget/volume expectations — this affects whether Azure's cheaper-per-character pricing or
   ElevenLabs' better expressiveness-per-dollar wins out at scale.
2. Do you want to clone specific human voices for Clara/Max (both vendors support voice
   cloning) or pick from stock voices?
3. Who's doing the assembly/mixing — a DAW (Audacity/Reaction/Descript) or a script-driven
   pipeline (e.g., stitching clips with ffmpeg based on the `<START/END AUDIO FILE>` markers in
   these scripts)?
