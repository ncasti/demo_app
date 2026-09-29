"""Manifest for scripts/a1-it-22-la-mia-famiglia.md

Twenty-second Italian A1 episode -- talking about family. Uses
lesson_segments.py for the repeating drill blocks.

Marco/Giulia reprise their episode 2/6/19 actors (Stefano Ca, Carlotta).
"Ho un fratello" is a deliberate callback to episode 18's "Ho una
prenotazione" -- same "ho" construction, new domain.
"""

from lesson_segments import speaking_challenge, reverse_translate_item, roundtrip_step

NAME = "a1_it_22_la_mia_famiglia"

CAST = {
    "Clara":  "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":    "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Marco":  "CEZqCqfrPU34IkHzkV30",  # Stefano Ca - native Italian
    "Giulia": "Z9LM7NBnQ8aOZKIXkd5S",  # Carlotta - native Italian
}

PIAZZA_SCENE = {
    "key": "PIAZZA4",
    "lang": "it",
    "ambience_prompt": "continuous loopable outdoor Italian piazza ambience, distant fountain, occasional footsteps and pigeons, quiet murmur, no music, no words",
    "start_prompt": "brief outdoor city square ambience begins, fountain and distant footsteps fade in",
    "end_prompt": "brief pause, piazza ambience continues, footsteps receding",
    "start_dur": 1.5,
    "end_dur": 1.3,
    "lead": 0.8,
    "tail": 1.0,
    "turn_gap": 0.5,
    "lines": [
        ("Marco", "Giulia, questa è mia sorella."),
        ("Giulia", "Piacere! Hai altri fratelli?"),
        ("Marco", "Sì, ho un fratello."),
    ],
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: bright acoustic guitar and light mandolin melody, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Clara", "Ciao, Max!", "it"),
    ("speech_multi", "Max", [
        ("it", "Ciao, Clara!"),
        ("en", "Today — family. Marco's introducing someone."),
    ]),
    ("speech", "Clara", "Let's listen in.", "en"),
    ("silence", 0.8),

    ("scene", PIAZZA_SCENE),

    ("silence", 2.0),
    ("speech", "Max", "Three phrases in there. Let's break them down.", "en"),
    ("speech_multi", "Clara", [
        ("en", "First —"),
        ("it", "Questa è mia sorella."),
        ("en", "\"This is my sister.\" Swap in any family member."),
    ]),
    ("speech", "Clara", "Repeat after Max.", "en"),
    ("silence", 3.0),
    *speaking_challenge("Max", "Questa è mia sorella.", "it"),

    ("speech_multi", "Max", [
        ("en", "Second —"),
        ("it", "Ho un fratello."),
        ("en", "\"I have a brother.\" Same pattern as \"Ho una prenotazione\" from the hotel — \"ho\" just means \"I have.\""),
    ]),
    ("speech", "Clara", "Ho un fratello.", "it"),
    ("speech", "Max", "Your turn. Repeat after Clara.", "en"),
    ("silence", 3.0),
    *speaking_challenge("Clara", "Ho un fratello.", "it"),

    ("speech_multi", "Clara", [
        ("en", "Third — asking someone else:"),
        ("it", "Hai fratelli?"),
        ("en", "\"Do you have siblings?\""),
    ]),
    ("speech", "Max", "Hai fratelli ?", "it"),
    ("speech", "Clara", "Repeat after Max.", "en"),
    ("silence", 3.0),
    *speaking_challenge("Max", "Hai fratelli ?", "it"),
    ("speech", "Clara", "Perfetto !", "it"),
    ("silence", 3.0),

    ("speech", "Max", "Now backwards — I'll say it in English, you say it in Italian.", "en"),
    *reverse_translate_item("Clara", "How do you introduce your sister?", "Max", "Questa è mia sorella."),
    *reverse_translate_item("Clara", "How do you say you have a brother?", "Max", "Ho un fratello."),
    *reverse_translate_item("Clara", "And how do you ask if someone has siblings?", "Max", "Hai fratelli ?"),

    ("speech", "Clara", "Now put it together — you're the one introducing your sister to Giulia this time.", "en"),
    ("silence", 1.0),
    *roundtrip_step("Max", "Introduce your sister.", "Clara", "Giulia, questa è mia sorella.",
                     char_speaker="Giulia", char_it="Piacere! Hai altri fratelli?"),
    *roundtrip_step("Max", "Tell her — yes, one brother.", "Clara", "Sì, ho un fratello.",
                     attempt_gap=3.0, tail_gap=2.0),

    ("speech", "Clara", "That's it — you can talk about your family in Italian now.", "en"),
    ("silence", 2.5),

    ("speech_multi", "Clara", [("en", "So today:"), ("it", "Questa è mia sorella,"), ("en", "to introduce family...")]),
    ("speech_multi", "Max", [("it", "Ho un fratello,"), ("en", "to say who you have...")]),
    ("speech_multi", "Clara", [("en", "And"), ("it", "Hai fratelli"), ("en", "— to ask.")]),
    ("speech", "Max", "Next time, a practice episode — understanding and family, together.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: same bright acoustic guitar and mandolin melody as the intro, but winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
