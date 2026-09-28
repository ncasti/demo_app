"""Manifest for scripts/a1-it-17-practice-cinque.md

Fifth spaced-repetition practice episode -- recombines episodes 15-16
(shopping, likes/dislikes).
"""

from lesson_segments import reverse_translate_item

NAME = "a1_it_17_practice_cinque"

CAST = {
    "Clara":    "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":      "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Commessa": "litDcG1avVppv4R90BLu",  # Carla - native Italian
    "Luca":     "CEZqCqfrPU34IkHzkV30",  # Stefano Ca - native Italian
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: bright acoustic guitar and light mandolin melody, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Clara", "Ciao, Max!", "it"),
    ("speech", "Max", "Ciao, Clara! Shopping, then talking about what you like. Fast round first.", "en"),
    ("silence", 2.0),

    *reverse_translate_item("Max", "How do you ask for a t-shirt?", "Clara", "Vorrei una maglietta.", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How does someone ask your size?", "Clara", "Che taglia ?", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you say \"medium\"?", "Clara", "Taglia media.", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you say you like something?", "Clara", "Mi piace...", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you say you don't like it?", "Clara", "Non mi piace.", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you ask if someone likes something?", "Clara", "Ti piace...?", attempt_gap=2.0, tail_gap=3.0),

    ("speech", "Max", "Perfetto! Now put it together.", "en"),
    ("silence", 2.0),

    ("speech", "Max", "You're in the shop. Ask for a t-shirt, and give your size when she asks.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 4.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Vorrei una maglietta.", "it"),
    ("speech", "Commessa", "Che taglia ?", "it"),
    ("speech", "Clara", "Taglia media.", "it"),
    ("silence", 1.5),

    ("speech", "Luca", "Ti piace ?", "it"),
    ("speech", "Max", "He's asking if you like it. Tell him yes, a lot.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Sì, mi piace molto !", "it"),
    ("silence", 2.0),

    ("speech", "Clara", "Shopping and opinions, both handled — nice work.", "en"),
    ("speech", "Max", "Next time: a hotel check-in.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: same bright acoustic guitar and mandolin melody as the intro, but winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
