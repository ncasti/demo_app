"""Manifest for scripts/a1-it-06-che-ore-sono.md

Sixth Italian A1 episode -- telling time. Uses lesson_segments.py for the
speaking-challenge / reverse-translate / round-trip blocks (see that
module's docstring for why -- factored out after episode 5 to stop
hand-copying the same three shapes into every manifest).

Marco/Giulia reprise their episode 2 actors (Stefano Ca, Carlotta) for
listener continuity.
"""

from lesson_segments import speaking_challenge, reverse_translate_item, roundtrip_step

NAME = "a1_it_06_che_ore_sono"

CAST = {
    "Clara":  "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":    "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Marco":  "CEZqCqfrPU34IkHzkV30",  # Stefano Ca - native Italian
    "Giulia": "Z9LM7NBnQ8aOZKIXkd5S",  # Carlotta - native Italian
}

PIAZZA_SCENE = {
    "key": "PIAZZA2",
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
        ("Giulia", "Scusi, che ore sono?"),
        ("Marco", "Sono le tre."),
        ("Giulia", "Devo andare! Grazie mille."),
        ("Marco", "Prego!"),
    ],
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: a single short bright acoustic guitar and light mandolin phrase, played once only, does not loop or repeat, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Clara", "Ciao, Max!", "it"),
    ("speech_multi", "Max", [
        ("it", "Ciao, Clara!"),
        ("en", "Remember Marco and Giulia from the piazza? Let's catch back up with them."),
    ]),
    ("speech", "Clara", "Let's listen in.", "en"),
    ("silence", 0.8),

    ("scene", PIAZZA_SCENE),

    ("silence", 2.0),
    ("speech", "Max", "Three phrases in there. Let's break them down.", "en"),
    ("speech_multi", "Clara", [
        ("en", "First —"),
        ("it", "Che ore sono?"),
        ("en", "It means \"what time is it?\" — the question you'll ask constantly."),
    ]),
    ("speech", "Clara", "Repeat after Max.", "en"),
    *speaking_challenge("Max", "Che ore sono ?", "it"),

    ("speech_multi", "Max", [
        ("en", "Second — the answer:"),
        ("it", "Sono le tre."),
        ("en", "\"It's three o'clock.\" Swap in any number for the time."),
    ]),
    ("speech", "Clara", "Sono le tre.", "it"),
    ("speech", "Max", "Your turn. Repeat after Clara.", "en"),
    *speaking_challenge("Clara", "Sono le tre.", "it"),

    ("speech_multi", "Clara", [
        ("en", "Third — Giulia's reaction to the time:"),
        ("it", "Devo andare."),
        ("en", "\"I have to go.\" Perfect for wrapping up any conversation."),
    ]),
    ("speech", "Max", "Devo andare.", "it"),
    ("speech", "Clara", "Repeat after Max.", "en"),
    *speaking_challenge("Max", "Devo andare.", "it"),
    ("speech", "Clara", "Perfetto !", "it"),
    ("silence", 3.0),

    ("speech", "Max", "Now backwards — I'll say it in English, you say it in Italian.", "en"),
    *reverse_translate_item("Clara", "How do you ask what time it is?", "Max", "Che ore sono ?"),
    *reverse_translate_item("Clara", "How do you say \"it's three o'clock\"?", "Max", "Sono le tre."),
    *reverse_translate_item("Clara", "And how do you say \"I have to go\"?", "Max", "Devo andare."),

    ("speech", "Clara", "Now put it together — you're the one Giulia stops in the piazza.", "en"),
    ("silence", 1.0),
    *roundtrip_step("Max", "Giulia asks you the time. Answer her — it's three o'clock.", "Clara", "Sono le tre.",
                     narration="And she reacts:", char_speaker="Giulia", char_it="Devo andare! Grazie mille.", tail_gap=2.0),

    ("speech", "Clara", "That's it — you can tell anyone the time now.", "en"),
    ("silence", 2.5),

    ("speech_multi", "Clara", [("en", "So today:"), ("it", "Che ore sono,"), ("en", "to ask the time...")]),
    ("speech_multi", "Max", [("it", "Sono le tre,"), ("en", "to answer it...")]),
    ("speech_multi", "Clara", [("en", "And"), ("it", "Devo andare,"), ("en", "when it's time to go.")]),
    ("speech", "Max", "Next time: dinner. We're going to a restaurant.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: a single short bright acoustic guitar and mandolin phrase like the intro, played once only, does not loop or repeat, winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
