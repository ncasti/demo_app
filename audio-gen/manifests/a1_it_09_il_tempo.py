"""Manifest for scripts/a1-it-09-il-tempo.md

Ninth Italian A1 episode -- talking about the weather. Uses
lesson_segments.py for the repeating drill blocks.

Luca/Sara reuse the Stefano Ca / Carlotta pairing under new character
names -- recurring native cast, new scenario. The round-trip section is a
structural variant: Sara asks her question in-character first, then Max
narrates the instruction, since the natural trigger here is hearing her ask
it (see production notes in the .md for why this doesn't use
roundtrip_step's usual instruction-first shape).
"""

from lesson_segments import speaking_challenge, reverse_translate_item

NAME = "a1_it_09_il_tempo"

CAST = {
    "Clara": "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":   "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Luca":  "CEZqCqfrPU34IkHzkV30",  # Stefano Ca - native Italian
    "Sara":  "Z9LM7NBnQ8aOZKIXkd5S",  # Carlotta - native Italian
}

OUTDOOR_SCENE = {
    "key": "OUTDOOR",
    "lang": "it",
    "ambience_prompt": "continuous loopable outdoor ambience, light breeze, distant birds, quiet, no music, no words",
    "start_prompt": "brief outdoor ambience begins, light breeze and birds fade in",
    "end_prompt": "brief pause, outdoor ambience continues",
    "start_dur": 1.5,
    "end_dur": 1.3,
    "lead": 0.8,
    "tail": 1.0,
    "turn_gap": 0.5,
    "lines": [
        ("Luca", "Che tempo fa oggi?"),
        ("Sara", "Fa caldo! C'è il sole"),
        ("Luca", "Perfetto per una passeggiata"),
    ],
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: a single short bright acoustic guitar and light mandolin phrase, played once only, does not loop or repeat, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Clara", "Ciao, Max!", "it"),
    ("speech_multi", "Max", [
        ("it", "Ciao, Clara!"),
        ("en", "Today — the most universal small talk there is: the weather."),
    ]),
    ("speech", "Clara", "Let's listen in. Two friends outside.", "en"),
    ("silence", 0.8),

    ("scene", OUTDOOR_SCENE),

    ("silence", 2.0),
    ("speech", "Max", "Three phrases in there. Let's break them down.", "en"),
    ("speech_multi", "Clara", [
        ("en", "First —"),
        ("it", "Che tempo fa?"),
        ("en", "\"What's the weather like?\" Simple, and you'll hear it as small talk everywhere."),
    ]),
    ("speech", "Clara", "Repeat after Max.", "en"),
    *speaking_challenge("Max", "Che tempo fa ?", "it"),

    ("speech_multi", "Max", [
        ("en", "Second —"),
        ("it", "Fa caldo"),
        ("en", "\"It's hot.\" The opposite is \"Fa freddo\" — good to recognize even if we don't drill it today."),
    ]),
    ("speech", "Clara", "Fa caldo", "it"),
    ("speech", "Max", "Your turn. Repeat after Clara.", "en"),
    *speaking_challenge("Clara", "Fa caldo.", "it"),

    ("speech_multi", "Clara", [
        ("en", "Third —"),
        ("it", "C'è il sole"),
        ("en", "\"It's sunny.\" Literally \"there's the sun.\""),
    ]),
    ("speech", "Max", "C'è il sole", "it"),
    ("speech", "Clara", "Repeat after Max.", "en"),
    *speaking_challenge("Max", "C'è il sole.", "it"),
    ("speech", "Clara", "Perfetto !", "it"),
    ("silence", 3.0),

    ("speech", "Max", "Now backwards — I'll say it in English, you say it in Italian.", "en"),
    *reverse_translate_item("Clara", "How do you ask what the weather's like?", "Max", "Che tempo fa ?"),
    *reverse_translate_item("Clara", "How do you say \"it's hot\"?", "Max", "Fa caldo."),
    *reverse_translate_item("Clara", "And how do you say \"it's sunny\"?", "Max", "C'è il sole."),

    ("speech", "Clara", "Now put it together — Sara's asking you about the weather.", "en"),
    ("silence", 1.0),

    ("speech", "Sara", "Che tempo fa oggi ?", "it"),
    ("speech", "Max", "She's asking you. Tell her it's hot, and sunny.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Fa caldo! C'è il sole", "it"),
    ("speech", "Sara", "Perfetto per una passeggiata !", "it"),
    ("silence", 2.0),

    ("speech", "Clara", "That's it — you can talk about the weather anywhere in Italy now.", "en"),
    ("silence", 2.5),

    ("speech_multi", "Clara", [("en", "So today:"), ("it", "Che tempo fa,"), ("en", "to ask...")]),
    ("speech_multi", "Max", [("it", "Fa caldo,"), ("en", "when it's hot...")]),
    ("speech_multi", "Clara", [("en", "And"), ("it", "C'è il sole"), ("en", "— it's sunny.")]),
    ("speech", "Max", "Next time: asking someone for help.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: a single short bright acoustic guitar and mandolin phrase like the intro, played once only, does not loop or repeat, winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
