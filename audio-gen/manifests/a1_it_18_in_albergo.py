"""Manifest for scripts/a1-it-18-in-albergo.md

Eighteenth Italian A1 episode -- checking into a hotel. Uses
lesson_segments.py for the repeating drill blocks.

Receptionist reuses the Alessandro actor -- recurring native cast, new
scenario. "A nome..." echoes the phone episode's "Sono..." as another
identification idiom.
"""

from lesson_segments import speaking_challenge, reverse_translate_item

NAME = "a1_it_18_in_albergo"

CAST = {
    "Clara":        "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":          "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Receptionist": "JfznbVXrGXYh0gZo9Lcp",  # Alessandro - native Italian
}

HOTEL_SCENE = {
    "key": "ALBERGO",
    "lang": "it",
    "ambience_prompt": "continuous loopable quiet hotel lobby ambience, distant elevator chime, soft footsteps, no music, no words",
    "start_prompt": "brief hotel lobby ambience begins, distant elevator chime fades in",
    "end_prompt": "brief pause, lobby ambience continues",
    "start_dur": 1.5,
    "end_dur": 1.3,
    "lead": 0.8,
    "tail": 1.0,
    "turn_gap": 0.5,
    "lines": [
        ("Clara", "Buonasera. Ho una prenotazione"),
        ("Receptionist", "A che nome?"),
        ("Clara", "A nome Clara"),
        ("Receptionist", "Ecco la chiave. Camera trecento"),
        ("Clara", "A che piano?"),
        ("Receptionist", "Terzo piano"),
    ],
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: a single short bright acoustic guitar and light mandolin phrase, played once only, does not loop or repeat, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Max", "Ciao, Clara!", "it"),
    ("speech_multi", "Clara", [
        ("it", "Ciao, Max!"),
        ("en", "Today — arriving at a hotel and checking in."),
    ]),
    ("speech", "Max", "Let's listen in.", "en"),
    ("silence", 0.8),

    ("scene", HOTEL_SCENE),

    ("silence", 2.0),
    ("speech", "Clara", "Three phrases in there. Let's break them down.", "en"),
    ("speech_multi", "Max", [
        ("en", "First —"),
        ("it", "Ho una prenotazione"),
        ("en", "\"I have a reservation.\" The first thing to say at any front desk."),
    ]),
    ("speech", "Clara", "Repeat after Max.", "en"),
    *speaking_challenge("Max", "Ho una prenotazione.", "it"),

    ("speech_multi", "Max", [
        ("en", "Second — when he asks the name:"),
        ("it", "A nome,"),
        ("en", "followed by your name. \"Under the name...\""),
    ]),
    ("speech", "Clara", "A nome Clara", "it"),
    ("speech", "Max", "Your turn. Repeat after Clara.", "en"),
    *speaking_challenge("Clara", "A nome Clara.", "it"),

    ("speech_multi", "Clara", [
        ("en", "Third — once you have the key:"),
        ("it", "A che piano?"),
        ("en", "\"What floor?\""),
    ]),
    ("speech", "Max", "A che piano ?", "it"),
    ("speech", "Clara", "Repeat after Max.", "en"),
    *speaking_challenge("Max", "A che piano ?", "it"),
    ("speech", "Clara", "Perfetto !", "it"),
    ("silence", 3.0),

    ("speech", "Max", "Now backwards — I'll say it in English, you say it in Italian.", "en"),
    *reverse_translate_item("Clara", "How do you say you have a reservation?", "Max", "Ho una prenotazione."),
    *reverse_translate_item("Clara", "How do you say what name it's under?", "Max", "A nome..."),
    *reverse_translate_item("Clara", "And how do you ask what floor?", "Max", "A che piano ?"),

    ("speech", "Clara", "Now put it together — you've just arrived at the front desk.", "en"),
    ("silence", 1.0),

    ("speech", "Max", "Tell him you have a reservation.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Ho una prenotazione", "it"),
    ("speech", "Max", "He asks the name:", "en"),
    ("speech", "Receptionist", "A che nome ?", "it"),
    ("silence", 1.0),

    ("speech", "Max", "Give your name.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "A nome Clara", "it"),
    ("speech", "Receptionist", "Ecco la chiave", "it"),
    ("silence", 1.0),

    ("speech", "Max", "Ask what floor.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "A che piano ?", "it"),
    ("speech", "Receptionist", "Terzo piano", "it"),
    ("silence", 2.0),

    ("speech", "Clara", "That's it — you're checked in.", "en"),
    ("silence", 2.5),

    ("speech_multi", "Clara", [("en", "So today:"), ("it", "Ho una prenotazione,"), ("en", "to check in...")]),
    ("speech_multi", "Max", [("it", "A nome,"), ("en", "for your name...")]),
    ("speech_multi", "Clara", [("en", "And"), ("it", "A che piano"), ("en", "— to find your room.")]),
    ("speech", "Max", "Next time: small talk, and how are you feeling.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: a single short bright acoustic guitar and mandolin phrase like the intro, played once only, does not loop or repeat, winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
