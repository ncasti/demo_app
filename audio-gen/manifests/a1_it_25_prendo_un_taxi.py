"""Manifest for scripts/a1-it-25-prendo-un-taxi.md

Twenty-fifth Italian A1 episode -- catching a taxi. Uses lesson_segments.py
for the repeating drill blocks.

Tassista reuses the Alessandro actor -- recurring native cast, new
scenario. Closes the batch without a "next time" teaser since the next
topic isn't decided yet.
"""

from lesson_segments import speaking_challenge, reverse_translate_item, roundtrip_step

NAME = "a1_it_25_prendo_un_taxi"

CAST = {
    "Clara":    "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":      "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Tassista": "JfznbVXrGXYh0gZo9Lcp",  # Alessandro - native Italian
}

TAXI_SCENE = {
    "key": "TAXI",
    "lang": "it",
    "ambience_prompt": "continuous loopable quiet car interior ambience, engine idling, road noise, no music, no words",
    "start_prompt": "car door closes and engine starts, brief idle",
    "end_prompt": "turn indicator clicking off, engine idle continues",
    "start_dur": 1.5,
    "end_dur": 1.3,
    "lead": 0.8,
    "tail": 1.0,
    "turn_gap": 0.5,
    "lines": [
        ("Clara", "Mi porta all'aeroporto, per favore?"),
        ("Tassista", "Certo, saliamo!"),
        ("Clara", "Quanto ci vuole?"),
        ("Tassista", "Venti minuti."),
        ("Clara", "Può aspettare, per favore?"),
        ("Tassista", "Va bene."),
    ],
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: bright acoustic guitar and light mandolin melody, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Max", "Ciao, Clara!", "it"),
    ("speech_multi", "Clara", [
        ("it", "Ciao, Max!"),
        ("en", "Today — catching a taxi."),
    ]),
    ("speech", "Max", "Let's listen in.", "en"),
    ("silence", 0.8),

    ("scene", TAXI_SCENE),

    ("silence", 2.0),
    ("speech", "Clara", "Three phrases in there. Let's break them down.", "en"),
    ("speech_multi", "Max", [
        ("en", "First —"),
        ("it", "Mi porta a...?"),
        ("en", "\"Can you take me to...?\" Swap in any destination."),
    ]),
    ("speech", "Clara", "Repeat after Max.", "en"),
    ("silence", 3.0),
    *speaking_challenge("Max", "Mi porta all'aeroporto ?", "it"),

    ("speech_multi", "Max", [
        ("en", "Second —"),
        ("it", "Quanto ci vuole?"),
        ("en", "\"How long does it take?\""),
    ]),
    ("speech", "Clara", "Quanto ci vuole ?", "it"),
    ("speech", "Max", "Your turn. Repeat after Clara.", "en"),
    ("silence", 3.0),
    *speaking_challenge("Clara", "Quanto ci vuole ?", "it"),

    ("speech_multi", "Clara", [
        ("en", "Third — if you need a quick stop:"),
        ("it", "Può aspettare?"),
        ("en", "\"Can you wait?\""),
    ]),
    ("speech", "Max", "Può aspettare ?", "it"),
    ("speech", "Clara", "Repeat after Max.", "en"),
    ("silence", 3.0),
    *speaking_challenge("Max", "Può aspettare ?", "it"),
    ("speech", "Clara", "Perfetto !", "it"),
    ("silence", 3.0),

    ("speech", "Max", "Now backwards — I'll say it in English, you say it in Italian.", "en"),
    *reverse_translate_item("Clara", "How do you ask him to take you to the airport?", "Max", "Mi porta all'aeroporto ?"),
    *reverse_translate_item("Clara", "How do you ask how long it takes?", "Max", "Quanto ci vuole ?"),
    *reverse_translate_item("Clara", "And how do you ask him to wait?", "Max", "Può aspettare ?"),

    ("speech", "Clara", "Now put it together — you've just hopped in the taxi.", "en"),
    ("silence", 1.0),
    *roundtrip_step("Max", "Ask him to take you to the airport.", "Clara", "Mi porta all'aeroporto, per favore?",
                     char_speaker="Tassista", char_it="Certo, saliamo !"),
    *roundtrip_step("Max", "Ask how long it'll take.", "Clara", "Quanto ci vuole ?",
                     attempt_gap=3.0, char_speaker="Tassista", char_it="Venti minuti."),
    *roundtrip_step("Max", "You need to grab something quickly. Ask him to wait.", "Clara", "Può aspettare, per favore?",
                     attempt_gap=3.0, char_speaker="Tassista", char_it="Va bene.", tail_gap=2.0),

    ("speech", "Clara", "That's it — you can catch a taxi anywhere in Italy now.", "en"),
    ("silence", 2.5),

    ("speech_multi", "Clara", [("en", "So today:"), ("it", "Mi porta a,"), ("en", "for a destination...")]),
    ("speech_multi", "Max", [("it", "Quanto ci vuole,"), ("en", "for the time...")]),
    ("speech_multi", "Clara", [("en", "And"), ("it", "Può aspettare"), ("en", "— to ask him to wait.")]),
    ("speech", "Max", "Ciao !", "it"),
    ("speech", "Clara", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: same bright acoustic guitar and mandolin melody as the intro, but winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
