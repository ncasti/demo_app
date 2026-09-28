"""Manifest for scripts/a1-it-14-practice-quattro.md

Fourth spaced-repetition practice episode -- recombines episodes 12-13
(phone, train station).
"""

from lesson_segments import reverse_translate_item

NAME = "a1_it_14_practice_quattro"

CAST = {
    "Clara":     "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":       "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Elena":     "Z9LM7NBnQ8aOZKIXkd5S",  # Carlotta - native Italian
    "Impiegato": "JfznbVXrGXYh0gZo9Lcp",  # Alessandro - native Italian
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: bright acoustic guitar and light mandolin melody, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Max", "Ciao, Clara!", "it"),
    ("speech", "Clara", "Ciao, Max! Phone call, then train station. Fast round first.", "en"),
    ("silence", 2.0),

    *reverse_translate_item("Max", "How do you answer the phone?", "Clara", "Pronto ?", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you say who you are, on the phone?", "Clara", "Sono...", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you ask to leave a message?", "Clara", "Posso lasciare un messaggio ?", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you ask for a ticket to Rome?", "Clara", "Un biglietto per Roma, per favore.", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you say \"one-way only\"?", "Clara", "Solo andata.", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you ask which platform?", "Clara", "Da che binario ?", attempt_gap=2.0, tail_gap=3.0),

    ("speech", "Max", "Perfetto! Now put it together.", "en"),
    ("silence", 2.0),

    ("speech", "Max", "The phone rings. Answer it, and say who you are.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Pronto? Sono Clara.", "it"),
    ("speech", "Elena", "Ciao, Clara !", "it"),
    ("silence", 1.5),

    ("speech", "Max", "Now you're at the station. Buy a one-way ticket to Rome, and ask the platform.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 4.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Un biglietto per Roma, per favore. Solo andata. Da che binario?", "it"),
    ("speech", "Impiegato", "Binario cinque.", "it"),
    ("silence", 2.0),

    ("speech", "Clara", "A call and a ticket, back to back — you're moving fast now.", "en"),
    ("speech", "Max", "Next time: shopping for clothes.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: same bright acoustic guitar and mandolin melody as the intro, but winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
