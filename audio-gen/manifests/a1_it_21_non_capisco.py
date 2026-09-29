"""Manifest for scripts/a1-it-21-non-capisco.md

Twenty-first Italian A1 episode -- clarification/meta-communication
phrases. Uses lesson_segments.py for the repeating drill blocks.

Marco reprises his episode 2/6/19 actor (Stefano Ca); Turista reuses Carla
-- recurring native cast, new scenario.
"""

from lesson_segments import speaking_challenge, reverse_translate_item

NAME = "a1_it_21_non_capisco"

CAST = {
    "Clara":   "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":     "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Marco":   "CEZqCqfrPU34IkHzkV30",  # Stefano Ca - native Italian
    "Turista": "litDcG1avVppv4R90BLu",  # Carla - native Italian
}

STREET_SCENE = {
    "key": "STREET3",
    "lang": "it",
    "ambience_prompt": "continuous loopable outdoor Italian city street ambience, distant traffic, occasional passing footsteps, quiet, no music, no words",
    "start_prompt": "brief outdoor street ambience begins, distant traffic and footsteps fade in",
    "end_prompt": "brief pause, street ambience continues, distant traffic",
    "start_dur": 1.5,
    "end_dur": 1.3,
    "lead": 0.8,
    "tail": 1.0,
    "turn_gap": 0.5,
    "lines": [
        ("Marco", "Allora, deve andare sempre dritto, poi a sinistra."),
        ("Turista", "Scusi, non capisco. Può ripetere, per favore?"),
        ("Marco", "Certo! Sempre dritto, poi a sinistra."),
        ("Turista", "Più lentamente, per favore."),
        ("Marco", "Va bene. Sempre... dritto."),
    ],
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: bright acoustic guitar and light mandolin melody, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Max", "Ciao, Clara!", "it"),
    ("speech_multi", "Clara", [
        ("it", "Ciao, Max!"),
        ("en", "Today's the episode every beginner secretly needs first — what to say when someone talks too fast."),
    ]),
    ("speech", "Max", "Let's listen in.", "en"),
    ("silence", 0.8),

    ("scene", STREET_SCENE),

    ("silence", 2.0),
    ("speech", "Clara", "Three phrases in there. Let's break them down.", "en"),
    ("speech_multi", "Max", [
        ("en", "First —"),
        ("it", "Non capisco."),
        ("en", "\"I don't understand.\" The most important phrase in this whole series, honestly."),
    ]),
    ("speech", "Clara", "Repeat after Max.", "en"),
    ("silence", 3.0),
    *speaking_challenge("Max", "Non capisco.", "it"),

    ("speech_multi", "Max", [
        ("en", "Second —"),
        ("it", "Può ripetere?"),
        ("en", "\"Can you repeat?\" Ask for it again before you ask for it slower."),
    ]),
    ("speech", "Clara", "Può ripetere ?", "it"),
    ("speech", "Max", "Your turn. Repeat after Clara.", "en"),
    ("silence", 3.0),
    *speaking_challenge("Clara", "Può ripetere ?", "it"),

    ("speech_multi", "Clara", [
        ("en", "Third — if it's still too fast:"),
        ("it", "Più lentamente, per favore."),
        ("en", "\"More slowly, please.\""),
    ]),
    ("speech", "Max", "Più lentamente, per favore.", "it"),
    ("speech", "Clara", "Repeat after Max.", "en"),
    ("silence", 3.0),
    *speaking_challenge("Max", "Più lentamente, per favore.", "it"),
    ("speech", "Clara", "Perfetto !", "it"),
    ("silence", 3.0),

    ("speech", "Max", "Now backwards — I'll say it in English, you say it in Italian.", "en"),
    *reverse_translate_item("Clara", "How do you say you don't understand?", "Max", "Non capisco."),
    *reverse_translate_item("Clara", "How do you ask someone to repeat?", "Max", "Può ripetere ?"),
    *reverse_translate_item("Clara", "And how do you ask them to slow down?", "Max", "Più lentamente, per favore."),

    ("speech", "Clara", "Now put it together — Marco's giving you directions again, too fast.", "en"),
    ("silence", 1.0),

    ("speech", "Marco", "Allora, deve andare sempre dritto, poi a sinistra, poi a destra, poi...", "it"),
    ("speech", "Max", "Stop him. Tell him you don't understand, and ask him to repeat.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Non capisco. Può ripetere?", "it"),
    ("speech", "Marco", "Certo! Sempre dritto, poi a sinistra.", "it"),
    ("silence", 1.0),

    ("speech", "Max", "Still too fast. Ask him to slow down.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Più lentamente, per favore.", "it"),
    ("speech", "Marco", "Va bene. Sempre... dritto.", "it"),
    ("silence", 2.0),

    ("speech", "Clara", "That's it — now you can survive any conversation, even the ones that go too fast.", "en"),
    ("silence", 2.5),

    ("speech_multi", "Clara", [("en", "So today:"), ("it", "Non capisco,"), ("en", "when you're lost...")]),
    ("speech_multi", "Max", [("it", "Può ripetere,"), ("en", "to hear it again...")]),
    ("speech_multi", "Clara", [("en", "And"), ("it", "Più lentamente, per favore"), ("en", "— to slow it all down.")]),
    ("speech", "Max", "Next time: meeting someone's family.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: same bright acoustic guitar and mandolin melody as the intro, but winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
