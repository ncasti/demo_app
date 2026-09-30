"""Manifest for scripts/a1-it-24-quanti-anni-hai.md

Twenty-fourth Italian A1 episode -- age and birthdays. Uses
lesson_segments.py for the repeating drill blocks.

Luca/Sara reprise their episode 9/16 actors (Stefano Ca, Carlotta). "Ho
trent'anni" is the fourth domain (hotel, family, now age) for the same "ho"
construction, by design.
"""

from lesson_segments import speaking_challenge, reverse_translate_item

NAME = "a1_it_24_quanti_anni_hai"

CAST = {
    "Clara": "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":   "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Luca":  "CEZqCqfrPU34IkHzkV30",  # Stefano Ca - native Italian
    "Sara":  "Z9LM7NBnQ8aOZKIXkd5S",  # Carlotta - native Italian
}

OUTDOOR_SCENE = {
    "key": "OUTDOOR3",
    "lang": "it",
    "ambience_prompt": "continuous loopable outdoor ambience, light breeze, distant birds, quiet, no music, no words",
    "start_prompt": "brief outdoor ambience begins, light breeze fades in",
    "end_prompt": "brief pause, outdoor ambience continues",
    "start_dur": 1.5,
    "end_dur": 1.3,
    "lead": 0.8,
    "tail": 1.0,
    "turn_gap": 0.5,
    "lines": [
        ("Sara", "Quanti anni hai?"),
        ("Luca", "Ho trent'anni. E tu?"),
        ("Sara", "Ho ventotto anni"),
    ],
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: a single short bright acoustic guitar and light mandolin phrase, played once only, does not loop or repeat, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Clara", "Ciao, Max!", "it"),
    ("speech_multi", "Max", [
        ("it", "Ciao, Clara!"),
        ("en", "Today — age, and birthdays."),
    ]),
    ("speech", "Clara", "Let's listen in. Luca and Sara again.", "en"),
    ("silence", 0.8),

    ("scene", OUTDOOR_SCENE),

    ("silence", 2.0),
    ("speech", "Max", "Three phrases in there. Let's break them down.", "en"),
    ("speech_multi", "Clara", [
        ("en", "First —"),
        ("it", "Quanti anni hai?"),
        ("en", "\"How old are you?\" Literally \"how many years do you have.\""),
    ]),
    ("speech", "Clara", "Repeat after Max.", "en"),
    *speaking_challenge("Max", "Quanti anni hai ?", "it"),

    ("speech_multi", "Max", [
        ("en", "Second — the answer:"),
        ("it", "Ho trent'anni"),
        ("en", "\"I'm thirty.\" Same \"ho\" you already know — \"I have thirty years.\""),
    ]),
    ("speech", "Clara", "Ho trent'anni", "it"),
    ("speech", "Max", "Your turn. Repeat after Clara.", "en"),
    *speaking_challenge("Clara", "Ho trent'anni.", "it"),

    ("speech_multi", "Clara", [
        ("en", "Third —"),
        ("it", "Quando è il tuo compleanno?"),
        ("en", "\"When's your birthday?\""),
    ]),
    ("speech", "Max", "Quando è il tuo compleanno ?", "it"),
    ("speech", "Clara", "Repeat after Max.", "en"),
    *speaking_challenge("Max", "Quando è il tuo compleanno ?", "it"),
    ("speech", "Clara", "Perfetto !", "it"),
    ("silence", 3.0),

    ("speech", "Max", "Now backwards — I'll say it in English, you say it in Italian.", "en"),
    *reverse_translate_item("Clara", "How do you ask someone's age?", "Max", "Quanti anni hai ?"),
    *reverse_translate_item("Clara", "How do you say you're thirty?", "Max", "Ho trent'anni."),
    *reverse_translate_item("Clara", "And how do you ask when someone's birthday is?", "Max", "Quando è il tuo compleanno ?"),

    ("speech", "Clara", "Now put it together — Luca's asking you this time.", "en"),
    ("silence", 1.0),

    ("speech", "Luca", "Quanti anni hai ?", "it"),
    ("speech", "Max", "Tell him — thirty.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Ho trent'anni", "it"),
    ("speech", "Max", "Now ask him when his birthday is.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Quando è il tuo compleanno ?", "it"),
    ("speech", "Luca", "A maggio !", "it"),
    ("silence", 2.0),

    ("speech", "Clara", "That's it — age and birthdays, both handled in Italian now.", "en"),
    ("silence", 2.5),

    ("speech_multi", "Clara", [("en", "So today:"), ("it", "Quanti anni hai,"), ("en", "to ask age...")]),
    ("speech_multi", "Max", [("it", "Ho trent'anni,"), ("en", "to answer...")]),
    ("speech_multi", "Clara", [("en", "And"), ("it", "Quando è il tuo compleanno"), ("en", "— for birthdays.")]),
    ("speech", "Max", "Next time: catching a taxi.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: a single short bright acoustic guitar and mandolin phrase like the intro, played once only, does not loop or repeat, winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
