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
"""

NAME = "a1_it_01_bar"

CAST = {
    "Clara":    "XrExE9yKIg1WjnnlVkGX",  # Matilda - warm, professional host (F, IT-verified, multilingual)
    "Max":      "iP95p4xoKVk53GoZ742B",  # Chris - charming, down-to-earth host (M, multilingual, IT not verified -- spot check)
    "Barista":  "JfznbVXrGXYh0gZo9Lcp",  # Antonio - natural, balanced, calm (M, native Italian)
    "Cliente":  "litDcG1avVppv4R90BLu",  # Carla - natural, reflective, narrative (F, native Italian)
    "Voice1":   "CEZqCqfrPU34IkHzkV30",  # Stefano Ca - energetic & friendly (M, native Italian, "older man" line)
    "Voice2":   "Z9LM7NBnQ8aOZKIXkd5S",  # Carlotta - fresh, fun (F, native Italian, "young woman" line)
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
    ("sfx", "INTRO_STING", "podcast intro jingle: bright acoustic guitar and light mandolin melody, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Clara", "Ciao, Max!", "it"),
    ("speech_multi", "Max", [
        ("it", "Ciao, Clara!"),
        ("en", "Today: a scene every visitor to Italy runs into on day one — standing at the counter of a bar, ordering your coffee."),
    ]),
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
    ("silence", 3.0),

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
    ("sfx", "LISTEN_IN_STING", "brief soft transition sound, a quick swell of ambient crowd murmur fading in, like tuning into a real conversation, no music, no words", 1.0),
    ("speech", "Voice1", "Buongiorno !", "it"),
    ("speech", "Voice2", "Buongiorno, buongiorno !", "it"),
    ("speech", "Barista", "Buongiorno, signora !", "it"),
    ("silence", 2.0),

    ("speech_multi", "Max", [
        ("en", "Second — how she ordered."),
        ("it", "Un caffè, per favore."),
        ("en", "\"Un caffè\" is simply \"a coffee.\" And \"per favore\" means \"please\" — you can stick it onto almost anything you order."),
    ]),
    ("speech", "Clara", "Un caffè, per favore.", "it"),
    ("speech", "Max", "Your turn. Repeat after Clara.", "en"),
    ("silence", 3.0),

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
        ("it", "Ottimo !"),
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
        ("it", "Prego"),
        ("en", "— you're welcome. That pair goes together everywhere in Italy, not just at the bar."),
    ]),
    ("speech", "Clara", "Grazie.", "it"),
    ("speech", "Max", "Prego.", "it"),
    ("speech", "Clara", "Repeat after Max.", "en"),
    ("silence", 3.0),

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

    ("speech", "Max", "Now put it together. You walk up to the bar. Greet the barista, and order a coffee, politely.", "en"),
    ("silence", 5.0),
    ("speech", "Clara", "Here's one way to say it:", "en"),
    ("speech", "Max", "Buongiorno ! Un caffè, per favore.", "it"),
    ("silence", 3.0),

    ("speech_multi", "Clara", [("en", "So today:"), ("it", "Buongiorno"), ("en", "to greet...")]),
    ("speech_multi", "Max", [("it", "Un caffè, per favore"), ("en", "to order, politely...")]),
    ("speech_multi", "Clara", [("en", "And"), ("it", "Grazie — Prego"), ("en", "to finish it off.")]),
    ("speech", "Max", "Next time, we'll handle the part everyone forgets to learn — asking what something costs.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: same bright acoustic guitar and mandolin melody as the intro, but winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
