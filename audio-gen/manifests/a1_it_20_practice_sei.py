"""Manifest for scripts/a1-it-20-practice-sei.md

Sixth and final spaced-repetition practice episode of this batch -- recaps
episodes 18-19 (hotel, small talk) in the rapid review, then closes with a
"victory lap" round-trip that pulls callbacks from across the whole
20-episode run (episodes 1, 2/6/19, 3, 18) instead of just the immediately
preceding ones, since this is the arc's closing note.
"""

from lesson_segments import reverse_translate_item

NAME = "a1_it_20_practice_sei"

CAST = {
    "Clara":        "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":          "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Receptionist": "JfznbVXrGXYh0gZo9Lcp",  # Alessandro - native Italian
    "Barista":      "JfznbVXrGXYh0gZo9Lcp",  # Alessandro - native Italian
    "Giulia":       "Z9LM7NBnQ8aOZKIXkd5S",  # Carlotta - native Italian
    "Venditore":    "JfznbVXrGXYh0gZo9Lcp",  # Alessandro - native Italian
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: a single short bright acoustic guitar and light mandolin phrase, played once only, does not loop or repeat, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Max", "Ciao, Clara!", "it"),
    ("speech", "Clara", "Ciao, Max! Last one for this run — hotel, small talk, and then a proper victory lap.", "en"),
    ("speech", "Max", "Fast round first.", "en"),
    ("silence", 2.0),

    *reverse_translate_item("Max", "How do you say you have a reservation?", "Clara", "Ho una prenotazione", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you say what name it's under?", "Clara", "A nome", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you ask what floor?", "Clara", "A che piano ?", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you ask how someone's doing?", "Clara", "Come stai ?", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you say you're well?", "Clara", "Sto bene", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "And how do you ask them back?", "Clara", "E tu ?", attempt_gap=2.0, tail_gap=3.0),

    ("speech", "Max", "Perfetto! Now — the victory lap. One whole trip, start to finish, pulling from everything this run has covered.", "en"),
    ("silence", 2.0),

    ("speech", "Max", "You arrive at the hotel. Check in.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Ho una prenotazione. A nome Clara", "it"),
    ("speech", "Receptionist", "Ecco la chiave. Terzo piano", "it"),
    ("silence", 1.5),

    ("speech", "Max", "Next morning, at the bar. Greet the barista and order a coffee.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Buongiorno! Un caffè, per favore", "it"),
    ("speech", "Barista", "Ecco a lei", "it"),
    ("silence", 1.5),

    ("speech", "Giulia", "Ciao! Come stai ?", "it"),
    ("speech", "Max", "It's Giulia. Answer her, and ask her back.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Sto bene, grazie! E tu?", "it"),
    ("speech", "Giulia", "Non c'è male !", "it"),
    ("silence", 1.5),

    ("speech", "Max", "On the way back, stop at the market. Ask for some apples, and their price.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 4.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Vorrei delle mele, per favore. Quanto costa?", "it"),
    ("speech", "Venditore", "Sono due euro", "it"),
    ("speech", "Clara", "Ecco a lei. Grazie!", "it"),
    ("speech", "Venditore", "Prego !", "it"),
    ("silence", 2.0),

    ("speech", "Clara", "Checked in, caffeinated, caught up with a friend, and shopped at the market — a whole trip, entirely in Italian.", "en"),
    ("speech", "Max", "Twenty episodes ago, this was one word: Buongiorno. Look how far that's gone.", "en"),
    ("speech", "Clara", "That's the sample. From here — real feedback, real speech recognition, and a full curriculum.", "en"),
    ("speech", "Max", "Ciao !", "it"),
    ("speech", "Clara", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: a single short bright acoustic guitar and mandolin phrase like the intro, played once only, does not loop or repeat, winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
