"""Manifest for scripts/a1-it-19-come-stai.md

Nineteenth Italian A1 episode -- small talk and feelings. Last new-content
episode of the arc; episode 20 closes it out with a cumulative practice
episode. Uses lesson_segments.py for the repeating drill blocks.

Marco/Giulia reprise their episode 2/6 actors (Stefano Ca, Carlotta) as a
deliberate bookend. Round-trip variant like episodes 9/16: Giulia opens
in-character since that's the natural trigger for a greeting question.
"""

from lesson_segments import speaking_challenge, reverse_translate_item

NAME = "a1_it_19_come_stai"

CAST = {
    "Clara":  "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":    "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Marco":  "CEZqCqfrPU34IkHzkV30",  # Stefano Ca - native Italian
    "Giulia": "Z9LM7NBnQ8aOZKIXkd5S",  # Carlotta - native Italian
}

PIAZZA_SCENE = {
    "key": "PIAZZA3",
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
        ("Marco", "Ciao Giulia, come stai?"),
        ("Giulia", "Sto bene, grazie! E tu?"),
        ("Marco", "Non c'è male."),
    ],
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: a single short bright acoustic guitar and light mandolin phrase, played once only, does not loop or repeat, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Clara", "Ciao, Max!", "it"),
    ("speech_multi", "Max", [
        ("it", "Ciao, Clara!"),
        ("en", "One more piece before we wrap this up — asking how someone's doing."),
    ]),
    ("speech", "Clara", "Let's listen in. Marco and Giulia, one more time.", "en"),
    ("silence", 0.8),

    ("scene", PIAZZA_SCENE),

    ("silence", 2.0),
    ("speech", "Max", "Three phrases in there. Let's break them down.", "en"),
    ("speech_multi", "Clara", [
        ("en", "First —"),
        ("it", "Come stai?"),
        ("en", "\"How are you?\" The question that opens almost every conversation with someone you know."),
    ]),
    ("speech", "Clara", "Repeat after Max.", "en"),
    *speaking_challenge("Max", "Come stai ?", "it"),

    ("speech_multi", "Max", [
        ("en", "Second — the easy answer:"),
        ("it", "Sto bene."),
        ("en", "\"I'm well.\""),
    ]),
    ("speech", "Clara", "Sto bene.", "it"),
    ("speech", "Max", "Your turn. Repeat after Clara.", "en"),
    *speaking_challenge("Clara", "Sto bene.", "it"),

    ("speech_multi", "Clara", [
        ("en", "Third — and hand it back:"),
        ("it", "E tu?"),
        ("en", "\"And you?\" Two words, and the conversation keeps going."),
    ]),
    ("speech", "Max", "E tu ?", "it"),
    ("speech", "Clara", "Repeat after Max.", "en"),
    *speaking_challenge("Max", "E tu ?", "it"),
    ("speech", "Clara", "Perfetto !", "it"),
    ("silence", 3.0),

    ("speech", "Max", "Now backwards — I'll say it in English, you say it in Italian.", "en"),
    *reverse_translate_item("Clara", "How do you ask how someone's doing?", "Max", "Come stai ?"),
    *reverse_translate_item("Clara", "How do you say you're well?", "Max", "Sto bene."),
    *reverse_translate_item("Clara", "And how do you ask them back?", "Max", "E tu ?"),

    ("speech", "Clara", "Now put it together — Giulia's the one asking this time.", "en"),
    ("silence", 1.0),

    ("speech", "Giulia", "Ciao! Come stai ?", "it"),
    ("speech", "Max", "Tell her you're well, and ask her back.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Sto bene, grazie! E tu?", "it"),
    ("speech", "Giulia", "Non c'è male !", "it"),
    ("silence", 2.0),

    ("speech", "Clara", "That's it — you can open and carry a whole conversation in Italian now.", "en"),
    ("silence", 2.5),

    ("speech_multi", "Clara", [("en", "So today:"), ("it", "Come stai,"), ("en", "to ask...")]),
    ("speech_multi", "Max", [("it", "Sto bene,"), ("en", "to answer...")]),
    ("speech_multi", "Clara", [("en", "And"), ("it", "E tu"), ("en", "— to keep it going.")]),
    ("speech", "Max", "Next time — the last episode of this run, a big practice pulling everything together.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: a single short bright acoustic guitar and mandolin phrase like the intro, played once only, does not loop or repeat, winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
