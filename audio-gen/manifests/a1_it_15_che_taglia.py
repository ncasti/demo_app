"""Manifest for scripts/a1-it-15-che-taglia.md

Fifteenth Italian A1 episode -- shopping for clothes. Uses
lesson_segments.py for the repeating drill blocks.

Commessa reuses the Carla actor -- recurring native cast, new scenario.
"Vorrei" is now the third domain this verb has appeared in (market,
restaurant, shopping) -- spaced repetition of the construction, not just the
phrase.
"""

from lesson_segments import speaking_challenge, reverse_translate_item, roundtrip_step

NAME = "a1_it_15_che_taglia"

CAST = {
    "Clara":    "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":      "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Commessa": "litDcG1avVppv4R90BLu",  # Carla - native Italian
}

SHOP_SCENE = {
    "key": "NEGOZIO",
    "lang": "it",
    "ambience_prompt": "continuous loopable quiet clothing shop ambience, hangers shifting, soft footsteps, no music, no words",
    "start_prompt": "brief clothing shop ambience begins, hangers and soft footsteps fade in",
    "end_prompt": "brief pause, shop ambience continues",
    "start_dur": 1.5,
    "end_dur": 1.3,
    "lead": 0.8,
    "tail": 1.0,
    "turn_gap": 0.5,
    "lines": [
        ("Clara", "Vorrei una maglietta"),
        ("Commessa", "Che taglia?"),
        ("Clara", "Taglia media"),
        ("Commessa", "Ecco a lei"),
    ],
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: a single short bright acoustic guitar and light mandolin phrase, played once only, does not loop or repeat, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Clara", "Ciao, Max!", "it"),
    ("speech_multi", "Max", [
        ("it", "Ciao, Clara!"),
        ("en", "Today — shopping for clothes."),
    ]),
    ("speech", "Clara", "Let's listen in.", "en"),
    ("silence", 0.8),

    ("scene", SHOP_SCENE),

    ("silence", 2.0),
    ("speech", "Max", "Three phrases in there. Let's break them down.", "en"),
    ("speech_multi", "Clara", [
        ("en", "First — you already know \"Vorrei\" from the market and the restaurant. Here:"),
        ("it", "Vorrei una maglietta"),
        ("en", "\"I'd like a t-shirt.\""),
    ]),
    ("speech", "Clara", "Repeat after Max.", "en"),
    *speaking_challenge("Max", "Vorrei una maglietta.", "it"),

    ("speech_multi", "Max", [
        ("en", "Second — she'll ask"),
        ("it", "Che taglia?"),
        ("en", "\"What size?\""),
    ]),
    ("speech", "Clara", "Che taglia ?", "it"),
    ("speech", "Max", "Your turn. Repeat after Clara.", "en"),
    *speaking_challenge("Clara", "Che taglia ?", "it"),

    ("speech_multi", "Clara", [
        ("en", "Third — your answer:"),
        ("it", "Taglia media"),
        ("en", "\"Medium size.\" Swap in small or large just as easily."),
    ]),
    ("speech", "Max", "Taglia media", "it"),
    ("speech", "Clara", "Repeat after Max.", "en"),
    *speaking_challenge("Max", "Taglia media.", "it"),
    ("speech", "Clara", "Perfetto !", "it"),
    ("silence", 3.0),

    ("speech", "Max", "Now backwards — I'll say it in English, you say it in Italian.", "en"),
    *reverse_translate_item("Clara", "How do you ask for a t-shirt?", "Max", "Vorrei una maglietta."),
    *reverse_translate_item("Clara", "How does she ask your size?", "Max", "Che taglia ?"),
    *reverse_translate_item("Clara", "And how do you say \"medium\"?", "Max", "Taglia media."),

    ("speech", "Clara", "Now put it together — you're in the shop, and this time you're buying.", "en"),
    ("silence", 1.0),
    *roundtrip_step("Max", "Ask for a t-shirt.", "Clara", "Vorrei una maglietta.",
                     narration="She asks your size:", char_speaker="Commessa", char_it="Che taglia ?"),
    *roundtrip_step("Max", "Tell her — medium.", "Clara", "Taglia media.",
                     attempt_gap=2.5, char_speaker="Commessa", char_it="Ecco a lei.", tail_gap=2.0),

    ("speech", "Clara", "That's it — you just bought clothes in Italian.", "en"),
    ("silence", 2.5),

    ("speech_multi", "Clara", [("en", "So today:"), ("it", "Vorrei una maglietta,"), ("en", "to ask for it...")]),
    ("speech_multi", "Max", [("it", "Che taglia,"), ("en", "for your size...")]),
    ("speech_multi", "Clara", [("en", "And"), ("it", "Taglia media"), ("en", "— to answer.")]),
    ("speech", "Max", "Next time: saying what you like.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: a single short bright acoustic guitar and mandolin phrase like the intro, played once only, does not loop or repeat, winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
