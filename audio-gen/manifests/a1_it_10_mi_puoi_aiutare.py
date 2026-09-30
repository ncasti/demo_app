"""Manifest for scripts/a1-it-10-mi-puoi-aiutare.md

Tenth Italian A1 episode -- asking a stranger for help. Uses
lesson_segments.py for the repeating drill blocks.

Turista/Passante reuse Carla and Alessandro -- recurring native cast, new
scenario.
"""

from lesson_segments import speaking_challenge, reverse_translate_item, roundtrip_step

NAME = "a1_it_10_mi_puoi_aiutare"

CAST = {
    "Clara":    "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":      "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Turista":  "litDcG1avVppv4R90BLu",  # Carla - native Italian
    "Passante": "JfznbVXrGXYh0gZo9Lcp",  # Alessandro - native Italian
}

STREET_SCENE = {
    "key": "STREET2",
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
        ("Turista", "Mi scusi, mi può aiutare?"),
        ("Passante", "Certo, dica pure"),
        ("Turista", "Cerco una farmacia"),
        ("Passante", "È qui vicino"),
    ],
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: a single short bright acoustic guitar and light mandolin phrase, played once only, does not loop or repeat, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Max", "Ciao, Clara!", "it"),
    ("speech_multi", "Clara", [
        ("it", "Ciao, Max!"),
        ("en", "Today — what to say when you actually need help."),
    ]),
    ("speech", "Max", "Let's listen in.", "en"),
    ("silence", 0.8),

    ("scene", STREET_SCENE),

    ("silence", 2.0),
    ("speech", "Clara", "Three phrases in there. Let's break them down.", "en"),
    ("speech_multi", "Max", [
        ("en", "First —"),
        ("it", "Mi può aiutare?"),
        ("en", "\"Can you help me?\" One step up from just \"Scusi\" — this actually asks for something."),
    ]),
    ("speech", "Clara", "Repeat after Max.", "en"),
    *speaking_challenge("Max", "Mi può aiutare ?", "it"),

    ("speech_multi", "Max", [
        ("en", "Second — say what you need:"),
        ("it", "Cerco,"),
        ("en", "followed by what you're looking for. \"I'm looking for.\""),
    ]),
    ("speech", "Clara", "Cerco una farmacia", "it"),
    ("speech", "Max", "Your turn. Repeat after Clara.", "en"),
    *speaking_challenge("Clara", "Cerco una farmacia", "it"),

    ("speech_multi", "Clara", [
        ("en", "Third — the answer you're hoping for:"),
        ("it", "È qui vicino"),
        ("en", "\"It's nearby.\" Good news either way."),
    ]),
    ("speech", "Max", "È qui vicino", "it"),
    ("speech", "Clara", "Repeat after Max.", "en"),
    *speaking_challenge("Max", "È qui vicino", "it"),
    ("speech", "Clara", "Perfetto !", "it"),
    ("silence", 3.0),

    ("speech", "Max", "Now backwards — I'll say it in English, you say it in Italian.", "en"),
    *reverse_translate_item("Clara", "How do you ask someone to help you?", "Max", "Mi può aiutare ?"),
    *reverse_translate_item("Clara", "How do you say you're looking for a pharmacy?", "Max", "Cerco una farmacia"),
    *reverse_translate_item("Clara", "And how do you say \"it's nearby\"?", "Max", "È qui vicino"),

    ("speech", "Clara", "Now put it together — you need help, and this time you're the one asking.", "en"),
    ("silence", 1.0),
    *roundtrip_step("Max", "Ask him to help you.", "Clara", "Mi può aiutare ?",
                     narration="He's happy to:", char_speaker="Passante", char_it="Certo, dica pure"),
    *roundtrip_step("Max", "Tell him you're looking for a pharmacy.", "Clara", "Cerco una farmacia",
                     char_speaker="Passante", char_it="È qui vicino", tail_gap=2.0),

    ("speech", "Clara", "That's it — you can get help anywhere in Italy now.", "en"),
    ("silence", 2.5),

    ("speech_multi", "Clara", [("en", "So today:"), ("it", "Mi può aiutare,"), ("en", "to ask for help...")]),
    ("speech_multi", "Max", [("it", "Cerco una farmacia,"), ("en", "to say what you need...")]),
    ("speech_multi", "Clara", [("en", "And"), ("it", "È qui vicino"), ("en", "— it's nearby.")]),
    ("speech", "Max", "Next time, another practice episode — weather and asking for help, together.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: a single short bright acoustic guitar and mandolin phrase like the intro, played once only, does not loop or repeat, winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
