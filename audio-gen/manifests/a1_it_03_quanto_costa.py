"""Manifest for scripts/a1-it-03-quanto-costa.md

Third Italian A1 episode -- asking for something and asking its price at a
market stall. Follows the same production practices established (and
fixed) in episodes 1-2: Max is Vittorio (en+it verified), no bare
single-word isolation, every target-language word quoted in an
English-tagged chunk is pulled into its own speech_multi chunk.

Venditore reuses episode 1's Barista actor (Alessandro), Cliente reuses
episode 1's Cliente actor (Carla) -- recurring native cast, new scenario.

Reverse-translate and round-trip sections use the corrected cue order:
prompt -> SPEAKER_SFX -> silence (attempt) -> CORRECT_SFX -> answer. See
episode 1's docstring for why -- the first draft played the answer before
SPEAKER_SFX, giving it away before the listener could attempt it.
"""

NAME = "a1_it_03_quanto_costa"

CAST = {
    "Clara":     "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":       "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Venditore": "JfznbVXrGXYh0gZo9Lcp",  # Alessandro - native Italian
    "Cliente":   "litDcG1avVppv4R90BLu",  # Carla - native Italian
}

MARKET_SCENE = {
    "key": "MARKET",
    "lang": "it",
    "ambience_prompt": "continuous loopable outdoor Italian market ambience, distant vendors calling out, crates shifting, quiet bustle, no music, no words",
    "start_prompt": "brief outdoor market ambience begins, crates and distant vendor calls fade in",
    "end_prompt": "brief pause, market ambience continues, distant chatter",
    "start_dur": 1.5,
    "end_dur": 1.3,
    "lead": 0.8,
    "tail": 1.0,
    "turn_gap": 0.5,
    "lines": [
        ("Cliente", "Vorrei delle mele, per favore"),
        ("Venditore", "Certo !"),
        ("Cliente", "Quanto costa ?"),
        ("Venditore", "Sono due euro"),
        ("Cliente", "Ecco a lei. Grazie !"),
        ("Venditore", "Prego !"),
    ],
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: a single short bright acoustic guitar and light mandolin phrase, played once only, does not loop or repeat, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Clara", "Ciao, Max!", "it"),
    ("speech_multi", "Max", [
        ("it", "Ciao, Clara!"),
        ("en", "You can order coffee, and you can introduce yourself. Today — the market."),
    ]),
    ("speech", "Clara", "Let's listen in. A fruit stall, mid-morning.", "en"),
    ("silence", 0.8),

    ("scene", MARKET_SCENE),

    ("silence", 2.0),
    ("speech", "Max", "Three useful phrases in there. Let's take them one at a time.", "en"),
    ("speech_multi", "Clara", [
        ("en", "First —"),
        ("it", "Vorrei delle mele,"),
        ("en", "\"I would like some apples\" — much more polite than just naming the thing. Swap in whatever you want after that first word."),
    ]),
    ("speech", "Clara", "Repeat after Max.", "en"),

    ("speech", "Max", "Vorrei delle mele", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.5),
    ("speech", "Max", "Vorrei delle mele", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.8),

    ("speech_multi", "Max", [
        ("en", "Second —"),
        ("it", "Quanto costa?"),
        ("en", "That's \"how much does it cost?\" — ask it about anything, one item or the whole stall."),
    ]),
    ("speech", "Clara", "Quanto costa ?", "it"),
    ("speech", "Max", "Your turn. Repeat after Clara.", "en"),

    ("speech", "Clara", "Quanto costa ?", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.5),
    ("speech", "Clara", "Quanto costa ?", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.8),

    ("speech_multi", "Clara", [
        ("en", "Third — once you pay, you hand it over with"),
        ("it", "Ecco"),
        ("en", "It just means \"here you go\" — you'll use it constantly, for money, for anything you're passing to someone."),
    ]),
    ("speech", "Max", "Ecco", "it"),
    ("speech", "Clara", "Repeat after Max.", "en"),

    ("speech", "Max", "Ecco", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.5),
    ("speech", "Max", "Ecco", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.8),
    ("speech", "Clara", "Perfetto !", "it"),
    ("silence", 3.0),

    ("speech", "Max", "Now backwards — I'll say it in English, you say it in Italian.", "en"),

    ("speech", "Clara", "How do you politely ask for something?", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech_multi", "Max", [("en", "That's right —"), ("it", "Vorrei delle mele")]),
    ("silence", 1.8),

    ("speech", "Clara", "How do you ask how much something costs?", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech_multi", "Max", [("en", "That's right —"), ("it", "Quanto costa ?")]),
    ("silence", 1.8),

    ("speech", "Clara", "And what do you say handing something over?", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech_multi", "Max", [("en", "That's right —"), ("it", "Ecco")]),
    ("silence", 2.0),

    ("speech", "Clara", "Now put it together — you're at the stall, and this time you're in the conversation.", "en"),
    ("silence", 1.0),

    ("speech", "Max", "Ask for some apples, politely.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Vorrei delle mele, per favore", "it"),
    ("speech", "Max", "And the vendor says:", "en"),
    ("speech", "Venditore", "Certo !", "it"),
    ("silence", 1.2),

    ("speech", "Max", "Now ask how much.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Quanto costa ?", "it"),
    ("speech", "Max", "He tells you the price:", "en"),
    ("speech", "Venditore", "Sono due euro", "it"),
    ("silence", 1.2),

    ("speech", "Max", "Hand over the money.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Ecco a lei. Grazie !", "it"),
    ("speech", "Max", "And he answers:", "en"),
    ("speech", "Venditore", "Prego !", "it"),
    ("silence", 2.0),

    ("speech", "Clara", "That's it — you just bought something at an Italian market.", "en"),
    ("silence", 2.5),

    ("speech_multi", "Clara", [("en", "So today:"), ("it", "Vorrei delle mele,"), ("en", "to ask for something...")]),
    ("speech_multi", "Max", [("it", "Quanto costa,"), ("en", "to ask the price...")]),
    ("speech_multi", "Clara", [("en", "And"), ("it", "Ecco,"), ("en", "when you hand something over.")]),
    ("speech", "Max", "Next time, we'll put a whole day together — everything you've learned so far, in one trip.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: a single short bright acoustic guitar and mandolin phrase like the intro, played once only, does not loop or repeat, winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
