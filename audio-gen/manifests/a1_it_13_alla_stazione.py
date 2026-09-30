"""Manifest for scripts/a1-it-13-alla-stazione.md

Thirteenth Italian A1 episode -- buying a train ticket. Uses
lesson_segments.py for the repeating drill blocks.

Impiegato/Cliente reuse Alessandro and Carla -- recurring native cast, new
scenario. The clerk's price line is left receptive-only since "Quanto
costa?" was already drilled in episode 3.
"""

from lesson_segments import speaking_challenge, reverse_translate_item

NAME = "a1_it_13_alla_stazione"

CAST = {
    "Clara":     "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":       "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Impiegato": "JfznbVXrGXYh0gZo9Lcp",  # Alessandro - native Italian
    "Cliente":   "litDcG1avVppv4R90BLu",  # Carla - native Italian
}

STATION_SCENE = {
    "key": "STAZIONE",
    "lang": "it",
    "ambience_prompt": "continuous loopable train station ambience, distant announcements, rolling luggage, quiet crowd murmur, no music, no words",
    "start_prompt": "brief train station ambience begins, distant announcement and rolling luggage fade in",
    "end_prompt": "brief pause, station ambience continues, distant announcement",
    "start_dur": 1.5,
    "end_dur": 1.3,
    "lead": 0.8,
    "tail": 1.0,
    "turn_gap": 0.5,
    "lines": [
        ("Cliente", "Un biglietto per Roma, per favore"),
        ("Impiegato", "Andata o andata e ritorno?"),
        ("Cliente", "Solo andata"),
        ("Impiegato", "Sono quindici euro"),
        ("Cliente", "Da che binario?"),
        ("Impiegato", "Binario cinque"),
    ],
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: a single short bright acoustic guitar and light mandolin phrase, played once only, does not loop or repeat, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Clara", "Ciao, Max!", "it"),
    ("speech_multi", "Max", [
        ("it", "Ciao, Clara!"),
        ("en", "Today — the train station, and buying a ticket."),
    ]),
    ("speech", "Clara", "Let's listen in.", "en"),
    ("silence", 0.8),

    ("scene", STATION_SCENE),

    ("silence", 2.0),
    ("speech", "Max", "Three phrases in there. Let's break them down.", "en"),
    ("speech_multi", "Clara", [
        ("en", "First —"),
        ("it", "Un biglietto per Roma, per favore"),
        ("en", "\"A ticket to Rome, please.\" Swap in any city."),
    ]),
    ("speech", "Clara", "Repeat after Max.", "en"),
    *speaking_challenge("Max", "Un biglietto per Roma, per favore", "it"),

    ("speech_multi", "Max", [
        ("en", "Second — when they ask round-trip or one-way:"),
        ("it", "Solo andata"),
        ("en", "\"One-way only.\""),
    ]),
    ("speech", "Clara", "Solo andata", "it"),
    ("speech", "Max", "Your turn. Repeat after Clara.", "en"),
    *speaking_challenge("Clara", "Solo andata", "it"),

    ("speech_multi", "Clara", [
        ("en", "Third — the one question everyone forgets to ask:"),
        ("it", "Da che binario?"),
        ("en", "\"From which platform?\""),
    ]),
    ("speech", "Max", "Da che binario ?", "it"),
    ("speech", "Clara", "Repeat after Max.", "en"),
    *speaking_challenge("Max", "Da che binario ?", "it"),
    ("speech", "Clara", "Perfetto !", "it"),
    ("silence", 3.0),

    ("speech", "Max", "Now backwards — I'll say it in English, you say it in Italian.", "en"),
    *reverse_translate_item("Clara", "How do you ask for a ticket to Rome?", "Max", "Un biglietto per Roma, per favore"),
    *reverse_translate_item("Clara", "How do you say \"one-way only\"?", "Max", "Solo andata"),
    *reverse_translate_item("Clara", "And how do you ask which platform?", "Max", "Da che binario ?"),

    ("speech", "Clara", "Now put it together — you're at the window, and this time you're buying the ticket.", "en"),
    ("silence", 1.0),

    ("speech", "Max", "Ask for a ticket to Rome.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Un biglietto per Roma, per favore", "it"),
    ("speech", "Max", "He asks round-trip or one-way:", "en"),
    ("speech", "Impiegato", "Andata o andata e ritorno ?", "it"),
    ("silence", 1.0),

    ("speech", "Max", "Tell him one-way.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Solo andata", "it"),
    ("speech", "Max", "And now, the question everyone forgets:", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Da che binario ?", "it"),
    ("speech", "Impiegato", "Binario cinque", "it"),
    ("silence", 2.0),

    ("speech", "Clara", "That's it — you've got your ticket and your platform.", "en"),
    ("silence", 2.5),

    ("speech_multi", "Clara", [("en", "So today:"), ("it", "Un biglietto per Roma,"), ("en", "to buy a ticket...")]),
    ("speech_multi", "Max", [("it", "Solo andata,"), ("en", "one-way...")]),
    ("speech_multi", "Clara", [("en", "And"), ("it", "Da che binario"), ("en", "— the question everyone forgets.")]),
    ("speech", "Max", "Next time, a practice episode — the phone and the train station together.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: a single short bright acoustic guitar and mandolin phrase like the intro, played once only, does not loop or repeat, winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
