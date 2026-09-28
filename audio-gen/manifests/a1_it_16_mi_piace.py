"""Manifest for scripts/a1-it-16-mi-piace.md

Sixteenth Italian A1 episode -- likes and dislikes. Uses lesson_segments.py
for the repeating drill blocks.

Luca/Sara reprise their episode 9 actors (Stefano Ca, Carlotta). Like
episode 9, the round-trip has Luca ask in-character first, since that's the
natural conversational trigger.
"""

from lesson_segments import speaking_challenge, reverse_translate_item

NAME = "a1_it_16_mi_piace"

CAST = {
    "Clara": "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":   "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Luca":  "CEZqCqfrPU34IkHzkV30",  # Stefano Ca - native Italian
    "Sara":  "Z9LM7NBnQ8aOZKIXkd5S",  # Carlotta - native Italian
}

OUTDOOR_SCENE = {
    "key": "OUTDOOR2",
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
        ("Sara", "Ti piace il gelato?"),
        ("Luca", "Sì, mi piace molto!"),
        ("Sara", "A me piace di più la pizza."),
    ],
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: bright acoustic guitar and light mandolin melody, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Max", "Ciao, Clara!", "it"),
    ("speech_multi", "Clara", [
        ("it", "Ciao, Max!"),
        ("en", "Remember Luca and Sara from the weather episode? Today they're talking about food."),
    ]),
    ("speech", "Max", "Let's listen in.", "en"),
    ("silence", 0.8),

    ("scene", OUTDOOR_SCENE),

    ("silence", 2.0),
    ("speech", "Clara", "Three phrases in there. Let's break them down.", "en"),
    ("speech_multi", "Max", [
        ("en", "First —"),
        ("it", "Mi piace,"),
        ("en", "followed by the thing. \"I like it.\" Literally closer to \"it's pleasing to me,\" but just use it like \"I like.\""),
    ]),
    ("speech", "Clara", "Repeat after Max.", "en"),
    ("silence", 3.0),
    *speaking_challenge("Max", "Mi piace il gelato.", "it"),

    ("speech_multi", "Max", [
        ("en", "Second — the opposite:"),
        ("it", "Non mi piace."),
        ("en", "\"I don't like it.\" Just add \"non\" in front."),
    ]),
    ("speech", "Clara", "Non mi piace.", "it"),
    ("speech", "Max", "Your turn. Repeat after Clara.", "en"),
    ("silence", 3.0),
    *speaking_challenge("Clara", "Non mi piace.", "it"),

    ("speech_multi", "Clara", [
        ("en", "Third — asking someone else:"),
        ("it", "Ti piace...?"),
        ("en", "\"Do you like...?\" That's how Sara started the whole conversation."),
    ]),
    ("speech", "Max", "Ti piace il gelato ?", "it"),
    ("speech", "Clara", "Repeat after Max.", "en"),
    ("silence", 3.0),
    *speaking_challenge("Max", "Ti piace il gelato ?", "it"),
    ("speech", "Clara", "Perfetto !", "it"),
    ("silence", 3.0),

    ("speech", "Max", "Now backwards — I'll say it in English, you say it in Italian.", "en"),
    *reverse_translate_item("Clara", "How do you say you like something?", "Max", "Mi piace..."),
    *reverse_translate_item("Clara", "How do you say you don't like it?", "Max", "Non mi piace."),
    *reverse_translate_item("Clara", "And how do you ask if someone likes something?", "Max", "Ti piace...?"),

    ("speech", "Clara", "Now put it together — Luca's asking you this time.", "en"),
    ("silence", 1.0),

    ("speech", "Luca", "Ti piace la pizza ?", "it"),
    ("speech", "Max", "Tell him yes, you like it a lot.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Sì, mi piace molto !", "it"),
    ("speech", "Max", "Now ask him back — does he like gelato?", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Ti piace il gelato ?", "it"),
    ("speech", "Luca", "Sì, mi piace !", "it"),
    ("silence", 2.0),

    ("speech", "Clara", "That's it — you can talk about what you like in Italian now.", "en"),
    ("silence", 2.5),

    ("speech_multi", "Clara", [("en", "So today:"), ("it", "Mi piace,"), ("en", "to say you like something...")]),
    ("speech_multi", "Max", [("it", "Non mi piace,"), ("en", "when you don't...")]),
    ("speech_multi", "Clara", [("en", "And"), ("it", "Ti piace"), ("en", "— to ask someone else.")]),
    ("speech", "Max", "Next time, a practice episode — shopping and preferences together.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: same bright acoustic guitar and mandolin melody as the intro, but winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
