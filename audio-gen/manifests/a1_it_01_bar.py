"""Manifest for scripts/a1-it-01-buongiorno-al-bar.md

Redesigned from the first draft after listening feedback: less English banter
and phonetic explanation, more actual Italian content. This version covers
three repertoire phrases forming one complete transaction (greet, order,
thank) instead of just one isolated greeting, and drops proactive
pronunciation coaching entirely -- see the top-level README's pedagogy
section. That policy shift also means the fragment-isolation risk from the
first draft doesn't apply here: there's no syllable breakdown left to isolate.

Still applies both AI-TTS production rules from audio-gen/README.md:
- never isolate a chunk below 2-3 words (every Italian chunk here is a
  complete word or phrase: "Buongiorno", "Un caffè, per favore", "Grazie",
  "Prego", "Ottimo", "Perfetto")
- never leave a target-language word/phrase quoted inside an English-tagged
  chunk -- every one is pulled into its own ("it", ...) chunk via speech_multi

Uses eleven_v3 with an explicit language_code="it" per call (the model
confirmed by ear to handle target-language phonetics correctly, unlike
turbo_v2_5). Clara/Max reuse the same voice IDs as the French scripts for
brand consistency; Matilda is ElevenLabs-verified for Italian, Chris isn't
explicitly verified for it -- worth an A/B listen before trusting it fully.

Two later revisions:
- The "hear it around town" Voice1/Voice2/Barista montage was a standalone
  sting + bare lines with no ambience under them. Replaced with VOICES_SCENE,
  a proper `scene` block, so the bar ambience persists under all three lines
  instead of dropping to silence.
- The ending was redesigned into two parts: a reverse-translate challenge
  section (English prompt -> Italian recall, all three phrases, same
  SPEAKER_SFX/CORRECT_SFX cue pattern as the earlier repeat-after-me
  challenges) followed by a full round-trip "join the conversation" section
  where the listener produces each phrase and then hears the Barista's actual
  in-character response, covering the whole greet/order/thank transaction.
- Added a one-line "bar" false-friend note right when the scene is
  introduced -- Italian "bar" means cafe, not an English pub.
- SPEAKER_SFX and CORRECT_SFX are both user-picked fixed assets now (see
  FIXED_SFX_ASSETS in generate.py), not AI-generated. An INCORRECT_SFX asset
  is registered from the same upload but isn't referenced by SEGMENTS yet --
  this script has no live grading branch to trigger it on.
- Max's voice was swapped from Chris to Vittorio (nH7uLS5UdEnvKEOAXtlQ).
  Chris has no Italian verified_languages entry at all (checked via
  /v2/voices -- only en/fr/ar/pt/sv/hi), which is almost certainly why his
  Italian lines, especially bare words like "Prego", intermittently came out
  with English phonetics -- confirmed by ear. Vittorio is verified in
  exactly en+it. This breaks strict voice-ID consistency with the French
  Max (Chris still voices Max there), but "Max" the character stays
  consistent; the underlying voice per language is now picked for verified
  competency in that language first, like dubbing a recurring character
  with a different voice actor per language. Clara stays Matilda in both --
  she's actually it-verified, unlike Chris.
- Fixed two he/she mismatches: the narration called the Barista "she" in the
  closing round-trip section even though Barista is voiced by a male native
  speaker (Alessandro).
- Lengthened two bare single-word Italian chunks inside speech_multi
  narration ("Ottimo !" -> "Ottimo, ottimo !", "Prego" -> "Prego, prego !")
  per the project's own isolation rule -- these were incidental narration
  insertions, not core teaching content, so doubling them costs nothing
  pedagogically while giving the model more signal.
- Reordered the reverse-translate and round-trip sections: SPEAKER_SFX now
  comes right after the prompt (before any silence), so it functions as a
  cue to speak, not a cue that speaking is already over. The old order
  played the model answer before SPEAKER_SFX ever fired, which gave the
  answer away before the listener had a chance to attempt it. New order is
  prompt -> SPEAKER_SFX -> silence (attempt) -> CORRECT_SFX -> answer
  (a host's "That's right -- ..." for reverse-translate, Clara's in-scene
  line for the round-trip, since the barista's response depends on it
  having been said).
"""

NAME = "a1_it_01_bar"

CAST = {
    "Clara":    "XrExE9yKIg1WjnnlVkGX",  # Matilda - warm, professional host (F, IT-verified, multilingual)
    "Max":      "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - "Believable, Friendly and Rich" (M, verified in exactly en+it)
    "Barista":  "JfznbVXrGXYh0gZo9Lcp",  # Alessandro - natural, balanced, calm (M, native Italian)
    "Cliente":  "litDcG1avVppv4R90BLu",  # Carla - natural, reflective, narrative (F, native Italian)
    "Voice1":   "CEZqCqfrPU34IkHzkV30",  # Stefano Ca - energetic & friendly (M, native Italian, "older man" line)
    "Voice2":   "Z9LM7NBnQ8aOZKIXkd5S",  # Carlotta - fresh, fun (F, native Italian, "young woman" line)
}

VOICES_SCENE = {
    "key": "BAR_VOICES",
    "lang": "it",
    "ambience_prompt": "continuous loopable ambience inside a small Italian coffee bar, espresso machine hiss, cups clinking on saucers, quiet morning chatter, no music, no words",
    "start_prompt": "brief soft transition sound, a quick swell of ambient crowd murmur fading in, like tuning into a real conversation, no music, no words",
    "end_prompt": "quick fade of crowd murmur, brief soft transition back to a quiet studio, no music, no words",
    "start_dur": 1.2,
    "end_dur": 1.0,
    "lead": 0.6,
    "tail": 0.8,
    "turn_gap": 0.35,
    "lines": [
        ("Voice1", "Buongiorno !"),
        ("Voice2", "Buongiorno, buongiorno !"),
        ("Barista", "Buongiorno, signora !"),
    ],
}

BAR_SCENE = {
    "key": "BAR",
    "lang": "it",
    "ambience_prompt": "continuous loopable ambience inside a small Italian coffee bar, espresso machine hiss, cups clinking on saucers, quiet morning chatter, no music, no words",
    "start_prompt": "espresso machine hiss and a cup set down on a saucer, morning bar ambience begins",
    "end_prompt": "coffee cup set down on a saucer, brief pause, bar ambience continues",
    "start_dur": 1.5,
    "end_dur": 1.5,
    "lead": 0.8,
    "tail": 1.2,
    "turn_gap": 0.5,
    "lines": [
        ("Barista", "Buongiorno !"),
        ("Cliente", "Buongiorno ! Un caffè, per favore."),
        ("Barista", "Ecco a lei."),
        ("Cliente", "Grazie !"),
        ("Barista", "Prego !"),
    ],
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: a single short bright acoustic guitar and light mandolin phrase, played once only, does not loop or repeat, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Clara", "Ciao, Max!", "it"),
    ("speech_multi", "Max", [
        ("it", "Ciao, Clara!"),
        ("en", "Today: a scene every visitor to Italy runs into on day one — standing at the counter of a bar, ordering your coffee."),
    ]),
    ("speech", "Clara", "Quick note — an Italian \"bar\" isn't an English one. No alcohol required; it's just their word for a café.", "en"),
    ("speech", "Clara", "Let's listen in.", "en"),
    ("silence", 0.8),

    ("scene", BAR_SCENE),

    ("silence", 2.0),
    ("speech", "Max", "Three things in there you'll use every single day in Italy. Let's take them one at a time.", "en"),
    ("speech_multi", "Clara", [
        ("en", "First —"),
        ("it", "Buongiorno."),
        ("en", "You'll hear it constantly, any time from morning until early evening. It just means \"good day.\""),
    ]),
    ("speech", "Clara", "Repeat after Max.", "en"),

    ("speech", "Max", "Buongiorno !", "it"),
    ("sfx", "SPEAKER_SFX", "loud clear electronic beep, short attention tone, like a recording-start alert, bright and audible", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "bright cheerful bell chime, unmistakably a correct-answer ding, loud and clear, upbeat", 0.7),
    ("silence", 1.5),
    ("speech", "Max", "Buongiorno !", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.8),

    ("speech", "Clara", "Bravo! Let's hear a few more people say it around the bar.", "en"),
    ("scene", VOICES_SCENE),
    ("silence", 2.0),

    ("speech_multi", "Max", [
        ("en", "Second — how she ordered."),
        ("it", "Un caffè, per favore."),
        ("en", "\"Un caffè\" is simply \"a coffee.\" And \"per favore\" means \"please\" — you can stick it onto almost anything you order."),
    ]),
    ("speech", "Clara", "Un caffè, per favore.", "it"),
    ("speech", "Max", "Your turn. Repeat after Clara.", "en"),

    ("speech", "Clara", "Un caffè, per favore.", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.5),
    ("speech", "Clara", "Un caffè, per favore.", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.8),

    ("speech_multi", "Max", [
        ("it", "Ottimo, ottimo !"),
        ("en", "And whatever you order, just add"),
        ("it", "per favore"),
        ("en", "at the end — it works everywhere."),
    ]),
    ("silence", 2.0),

    ("speech_multi", "Clara", [
        ("en", "Third — after the barista hands it over, she says"),
        ("it", "Grazie."),
        ("en", "Thank you."),
    ]),
    ("speech_multi", "Max", [
        ("en", "And he answers"),
        ("it", "Prego, prego !"),
        ("en", "— you're welcome. That pair goes together everywhere in Italy, not just at the bar."),
    ]),
    ("speech", "Clara", "Grazie.", "it"),
    ("speech", "Max", "Prego.", "it"),
    ("speech", "Clara", "Repeat after Max.", "en"),

    ("speech", "Max", "Grazie !", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.5),
    ("speech", "Max", "Prego !", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.8),
    ("speech", "Clara", "Perfetto !", "it"),
    ("silence", 3.0),

    ("speech", "Max", "Now let's test what you remember — but backwards. I'll say it in English, you say it in Italian.", "en"),

    ("speech", "Clara", "How do you greet someone, before evening?", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech_multi", "Max", [("en", "That's right —"), ("it", "Buongiorno !")]),
    ("silence", 1.8),

    ("speech", "Clara", "How do you order a coffee, politely?", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech_multi", "Max", [("en", "That's right —"), ("it", "Un caffè, per favore.")]),
    ("silence", 1.8),

    ("speech", "Clara", "And how do you say thank you?", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech_multi", "Max", [("en", "That's right —"), ("it", "Grazie !")]),
    ("silence", 2.0),

    ("speech", "Clara", "Now put it all together — you're at the bar, and this time you're in the conversation.", "en"),
    ("silence", 1.0),

    ("speech", "Max", "Greet the barista.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Buongiorno !", "it"),
    ("speech", "Max", "And the barista greets you back:", "en"),
    ("speech", "Barista", "Buongiorno !", "it"),
    ("silence", 1.2),

    ("speech", "Max", "Now order a coffee, politely.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Un caffè, per favore.", "it"),
    ("speech", "Max", "He gets it ready and hands it over:", "en"),
    ("speech", "Barista", "Ecco a lei.", "it"),
    ("silence", 1.2),

    ("speech", "Max", "What do you say?", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Grazie !", "it"),
    ("speech", "Max", "And he answers:", "en"),
    ("speech", "Barista", "Prego !", "it"),
    ("silence", 2.0),

    ("speech", "Clara", "That's it — you just had your first real conversation in Italian.", "en"),
    ("silence", 2.5),

    ("speech_multi", "Clara", [("en", "So today:"), ("it", "Buongiorno"), ("en", "to greet...")]),
    ("speech_multi", "Max", [("it", "Un caffè, per favore"), ("en", "to order, politely...")]),
    ("speech_multi", "Clara", [("en", "And"), ("it", "Grazie — Prego"), ("en", "to finish it off.")]),
    ("speech", "Max", "Next time, we'll handle the part everyone forgets to learn — asking what something costs.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: a single short bright acoustic guitar and mandolin phrase like the intro, played once only, does not loop or repeat, winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
