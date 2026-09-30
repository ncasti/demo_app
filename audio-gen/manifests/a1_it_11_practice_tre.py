"""Manifest for scripts/a1-it-11-practice-tre.md

Third spaced-repetition practice episode -- recombines episodes 9-10
(weather, asking for help). Shorter than episodes 4/8 since there are only
two source episodes to recap this time -- a practice episode should run as
long as the material warrants, not be padded to match earlier ones.
"""

from lesson_segments import reverse_translate_item

NAME = "a1_it_11_practice_tre"

CAST = {
    "Clara":    "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":      "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Sara":     "Z9LM7NBnQ8aOZKIXkd5S",  # Carlotta - native Italian
    "Passante": "JfznbVXrGXYh0gZo9Lcp",  # Alessandro - native Italian
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: a single short bright acoustic guitar and light mandolin phrase, played once only, does not loop or repeat, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Clara", "Ciao, Max!", "it"),
    ("speech", "Max", "Ciao, Clara! Quick one today — weather, and asking for help. Fast round first.", "en"),
    ("silence", 2.0),

    *reverse_translate_item("Max", "How do you ask what the weather's like?", "Clara", "Che tempo fa ?", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you say \"it's hot\"?", "Clara", "Fa caldo.", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you say \"it's sunny\"?", "Clara", "C'è il sole.", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you ask someone to help you?", "Clara", "Mi può aiutare ?", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you say you're looking for something?", "Clara", "Cerco...", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you say \"it's nearby\"?", "Clara", "È qui vicino.", attempt_gap=2.0, tail_gap=3.0),

    ("speech", "Max", "Perfetto! Now put it together.", "en"),
    ("silence", 2.0),

    ("speech", "Max", "Sara asks about the weather. Tell her it's hot and sunny.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Sara", "Che tempo fa oggi ?", "it"),
    ("speech", "Clara", "Fa caldo! C'è il sole", "it"),
    ("silence", 1.5),

    ("speech", "Max", "Now you need a pharmacy. Ask a passerby for help.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Mi può aiutare? Cerco una farmacia", "it"),
    ("speech", "Passante", "È qui vicino", "it"),
    ("silence", 2.0),

    ("speech", "Clara", "Good instincts either way — small talk, and a favor, both handled.", "en"),
    ("speech", "Max", "Next time: making a phone call.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: a single short bright acoustic guitar and mandolin phrase like the intro, played once only, does not loop or repeat, winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
