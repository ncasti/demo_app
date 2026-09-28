"""Manifest for scripts/a1-it-08-practice-due.md

Second spaced-repetition practice episode -- no new vocabulary. Recombines
the nine repertoire phrases from episodes 5-7 (directions, time, restaurant)
into one afternoon. Same lighter production as episode 4: no scene ambience,
single-pass drills, tighter gaps than a teaching episode.

Reuses lesson_segments.py's reverse_translate_item/roundtrip_step with
shorter gap overrides for the faster review pace.
"""

from lesson_segments import reverse_translate_item, roundtrip_step

NAME = "a1_it_08_practice_due"

CAST = {
    "Clara":     "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":       "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Passante":  "JfznbVXrGXYh0gZo9Lcp",  # Alessandro - native Italian
    "Giulia":    "Z9LM7NBnQ8aOZKIXkd5S",  # Carlotta - native Italian
    "Cameriere": "JfznbVXrGXYh0gZo9Lcp",  # Alessandro - native Italian
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: bright acoustic guitar and light mandolin melody, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Max", "Ciao, Clara!", "it"),
    ("speech", "Clara", "Ciao, Max! No new words today — directions, time, and dinner, all together.", "en"),
    ("speech", "Max", "Fast round first, no repeats.", "en"),
    ("silence", 2.0),

    *reverse_translate_item("Max", "How do you get a stranger's attention?", "Clara", "Scusi !", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you ask where the station is?", "Clara", "Dov'è la stazione ?", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you say \"straight ahead\"?", "Clara", "Sempre dritto.", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you ask what time it is?", "Clara", "Che ore sono ?", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you say \"it's three o'clock\"?", "Clara", "Sono le tre.", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you say \"I have to go\"?", "Clara", "Devo andare.", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you ask for a table for two?", "Clara", "Un tavolo per due, per favore.", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you order the pasta?", "Clara", "Vorrei la pasta.", attempt_gap=2.0, tail_gap=1.5),
    *reverse_translate_item("Max", "How do you ask for the check?", "Clara", "Il conto, per favore.", attempt_gap=2.0, tail_gap=3.0),

    ("speech", "Max", "Perfetto! Now a whole afternoon, start to finish.", "en"),
    ("silence", 2.0),

    *roundtrip_step("Max", "You're lost. Get a passerby's attention.", "Clara", "Scusi !",
                     attempt_gap=2.5, char_speaker="Passante", char_it="Sì ?", tail_gap=0.8),
    *roundtrip_step("Max", "Ask him where the restaurant is.", "Clara", "Dov'è il ristorante ?",
                     attempt_gap=3.0, char_speaker="Passante", char_it="Sempre dritto !", tail_gap=1.5),
    *roundtrip_step("Max", "On the way, Giulia asks you the time.", "Clara", "Sono le tre.",
                     attempt_gap=2.5, char_speaker="Giulia", char_it="Devo andare! Grazie mille.", tail_gap=1.5),
    *roundtrip_step("Max", "You arrive. Ask for a table for two.", "Clara", "Un tavolo per due, per favore.",
                     attempt_gap=2.5, char_speaker="Cameriere", char_it="Cosa desidera ?", tail_gap=0.8),
    *roundtrip_step("Max", "Order the pasta.", "Clara", "Vorrei la pasta.",
                     attempt_gap=2.5, tail_gap=0.8),
    *roundtrip_step("Max", "And when you're done, ask for the check.", "Clara", "Il conto, per favore.",
                     attempt_gap=2.0, tail_gap=2.0),

    ("speech", "Clara", "A whole afternoon — lost, found, and fed — all in Italian.", "en"),
    ("speech", "Max", "Next time: talking about the weather, and asking for help.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: same bright acoustic guitar and mandolin melody as the intro, but winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
