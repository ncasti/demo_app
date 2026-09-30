"""Manifest for scripts/a1-it-23-practice-sette.md

Seventh spaced-repetition practice episode -- recombines episodes 21-22
(clarification, family).
"""

from lesson_segments import reverse_translate_item

NAME = "a1_it_23_practice_sette"

CAST = {
    "Clara":  "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":    "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Marco":  "CEZqCqfrPU34IkHzkV30",  # Stefano Ca - native Italian
    "Giulia": "Z9LM7NBnQ8aOZKIXkd5S",  # Carlotta - native Italian
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: a single short bright acoustic guitar and light mandolin phrase, played once only, does not loop or repeat, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Max", "Ciao, Clara!", "it"),
    ("speech", "Clara", "Ciao, Max! Understanding, then family. Fast round first.", "en"),
    ("silence", 2.0),

    *reverse_translate_item("Max", "How do you say you don't understand?", "Clara", "Non capisco.", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you ask someone to repeat?", "Clara", "Può ripetere ?", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you ask someone to slow down?", "Clara", "Più lentamente, per favore.", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you introduce your sister?", "Clara", "Questa è mia sorella.", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you say you have a brother?", "Clara", "Ho un fratello.", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you ask if someone has siblings?", "Clara", "Hai fratelli ?", attempt_gap=2.0, tail_gap=3.0),

    ("speech", "Max", "Perfetto! Now put it together.", "en"),
    ("silence", 2.0),

    ("speech", "Marco", "Allora, questa è mia sorella, e questo è mio fratello, e", "it"),
    ("speech", "Max", "Too much at once. Tell him you don't understand, and ask him to slow down.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Non capisco. Più lentamente, per favore", "it"),
    ("speech", "Marco", "Va bene. Questa è mia sorella", "it"),
    ("silence", 1.5),

    ("speech", "Max", "Now ask him if he has other siblings.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Hai fratelli ?", "it"),
    ("speech", "Marco", "Sì, ho un fratello", "it"),
    ("silence", 2.0),

    ("speech", "Clara", "Understanding and family — two very different skills, both holding up.", "en"),
    ("speech", "Max", "Next time: how old are you, and when's your birthday.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: a single short bright acoustic guitar and mandolin phrase like the intro, played once only, does not loop or repeat, winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
