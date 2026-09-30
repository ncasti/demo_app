"""Manifest for scripts/a1-it-07-al-ristorante.md

Seventh Italian A1 episode -- a restaurant visit. Uses lesson_segments.py
for the repeating drill blocks (see that module's docstring).

Cameriere reuses the Alessandro actor (Barista/Venditore in earlier
episodes), Cliente reuses Carla -- recurring native cast, new scenario.
"Vorrei" is a deliberate callback to episode 3's market scenario for spaced
repetition.
"""

from lesson_segments import speaking_challenge, reverse_translate_item, roundtrip_step

NAME = "a1_it_07_al_ristorante"

CAST = {
    "Clara":     "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":       "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Cameriere": "JfznbVXrGXYh0gZo9Lcp",  # Alessandro - native Italian
    "Cliente":   "litDcG1avVppv4R90BLu",  # Carla - native Italian
}

RESTAURANT_SCENE = {
    "key": "RISTORANTE",
    "lang": "it",
    "ambience_prompt": "continuous loopable quiet restaurant ambience, clinking cutlery, low chatter, no music, no words",
    "start_prompt": "brief restaurant ambience begins, cutlery and low chatter fade in",
    "end_prompt": "brief pause, restaurant ambience continues, quiet chatter",
    "start_dur": 1.5,
    "end_dur": 1.3,
    "lead": 0.8,
    "tail": 1.0,
    "turn_gap": 0.5,
    "lines": [
        ("Cameriere", "Buonasera! Un tavolo per due?"),
        ("Cliente", "Sì, per favore"),
        ("Cameriere", "Cosa desidera?"),
        ("Cliente", "Vorrei la pasta"),
        ("Cameriere", "Subito!"),
        ("Cliente", "Il conto, per favore"),
    ],
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: a single short bright acoustic guitar and light mandolin phrase, played once only, does not loop or repeat, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Max", "Ciao, Clara!", "it"),
    ("speech_multi", "Clara", [
        ("it", "Ciao, Max!"),
        ("en", "Time to eat. Let's go to a restaurant."),
    ]),
    ("speech", "Max", "Let's listen in.", "en"),
    ("silence", 0.8),

    ("scene", RESTAURANT_SCENE),

    ("silence", 2.0),
    ("speech", "Clara", "Three phrases in there. Let's break them down.", "en"),
    ("speech_multi", "Max", [
        ("en", "First —"),
        ("it", "Un tavolo per due, per favore"),
        ("en", "\"A table for two, please.\" Swap in any number."),
    ]),
    ("speech", "Clara", "Repeat after Max.", "en"),
    *speaking_challenge("Max", "Un tavolo per due, per favore", "it"),

    ("speech_multi", "Max", [
        ("en", "Second — ordering. Same word as the market —"),
        ("it", "Vorrei la pasta"),
        ("en", "— \"I'd like the pasta.\" Swap in whatever you're having."),
    ]),
    ("speech", "Clara", "Vorrei la pasta", "it"),
    ("speech", "Max", "Your turn. Repeat after Clara.", "en"),
    *speaking_challenge("Clara", "Vorrei la pasta", "it"),

    ("speech_multi", "Clara", [
        ("en", "Third — when you're done,"),
        ("it", "Il conto, per favore"),
        ("en", "\"The check, please.\" The phrase that ends every meal."),
    ]),
    ("speech", "Max", "Il conto, per favore", "it"),
    ("speech", "Clara", "Repeat after Max.", "en"),
    *speaking_challenge("Max", "Il conto, per favore", "it"),
    ("speech", "Clara", "Perfetto !", "it"),
    ("silence", 3.0),

    ("speech", "Max", "Now backwards — I'll say it in English, you say it in Italian.", "en"),
    *reverse_translate_item("Clara", "How do you ask for a table for two?", "Max", "Un tavolo per due, per favore"),
    *reverse_translate_item("Clara", "How do you order the pasta?", "Max", "Vorrei la pasta"),
    *reverse_translate_item("Clara", "And how do you ask for the check?", "Max", "Il conto, per favore"),

    ("speech", "Clara", "Now put it together — you've just walked into the restaurant.", "en"),
    ("silence", 1.0),
    *roundtrip_step("Max", "Ask for a table for two.", "Clara", "Un tavolo per due, per favore",
                     narration="He seats you and asks what you'd like:", char_speaker="Cameriere", char_it="Cosa desidera ?"),
    *roundtrip_step("Max", "Order the pasta.", "Clara", "Vorrei la pasta",
                     narration="He nods:", char_speaker="Cameriere", char_it="Subito !"),
    *roundtrip_step("Max", "Later, ask for the check.", "Clara", "Il conto, per favore", tail_gap=2.0),

    ("speech", "Clara", "That's it — you just ordered a whole meal in Italian.", "en"),
    ("silence", 2.5),

    ("speech_multi", "Clara", [("en", "So today:"), ("it", "Un tavolo per due,"), ("en", "for a table...")]),
    ("speech_multi", "Max", [("it", "Vorrei la pasta,"), ("en", "to order...")]),
    ("speech_multi", "Clara", [("en", "And"), ("it", "Il conto, per favore,"), ("en", "to close it out.")]),
    ("speech", "Max", "Next time, we're back with a practice episode — directions, time, and dinner, all together.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: a single short bright acoustic guitar and mandolin phrase like the intro, played once only, does not loop or repeat, winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
