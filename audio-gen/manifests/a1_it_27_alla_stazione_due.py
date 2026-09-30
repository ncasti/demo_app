"""Manifest for scripts/a1-it-27-alla-stazione-due.md

Part 2 of the chapter pilot (see a1_it_26_alla_stazione_uno.py). Opens by
reviewing part 1's two phrases with a fresh filler (Torino) never drilled
before -- tests the pattern, not memory of a fixed sentence -- then adds one
new phrase with no forced substitution pair (not every phrase needs one;
"Da che binario?" has no natural filler slot). Closes by chaining all three
phrases from both parts into one transaction with a fourth fresh city
(Firenze).
"""

from lesson_segments import speaking_challenge, reverse_translate_item, roundtrip_step

NAME = "a1_it_27_alla_stazione_due"

CAST = {
    "Clara":     "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":       "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Impiegato": "JfznbVXrGXYh0gZo9Lcp",  # Alessandro - native Italian
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: a single short bright acoustic guitar and light mandolin phrase, played once only, does not loop or repeat, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Max", "Ciao, Clara!", "it"),
    ("speech", "Clara", "Ciao, Max! Last time, we were at the ticket window. Let's pick up right where we left off — but first, let's see what stuck.", "en"),
    ("silence", 2.0),

    *reverse_translate_item("Max", "How do you ask for a ticket to Torino?", "Clara", "Un biglietto per Torino, per favore"),
    *reverse_translate_item("Max", "And if you only want to go one way this time?", "Clara", "Solo andata", tail_gap=3.0),

    ("speech", "Max", "Still holding up. Good.", "en"),
    ("silence", 2.0),

    ("speech", "Clara", "Now — one more piece. You've got your ticket. The one thing everyone forgets to ask before walking off.", "en"),
    ("speech_multi", "Max", [
        ("it", "Da che binario?"),
        ("en", "\"From which platform?\""),
    ]),
    ("speech", "Clara", "Repeat after Max.", "en"),
    *speaking_challenge("Max", "Da che binario ?", "it"),
    ("speech", "Clara", "Perfetto !", "it"),
    ("silence", 3.0),

    *reverse_translate_item("Max", "How do you ask which platform?", "Clara", "Da che binario ?"),

    ("speech", "Clara", "Now everything together — a city we haven't used at all yet: Florence. One trip, start to finish.", "en"),
    ("silence", 1.0),
    *roundtrip_step("Max", "Ask for a ticket to Florence.", "Clara", "Un biglietto per Firenze, per favore",
                     narration="He asks round-trip or one-way:", char_speaker="Impiegato", char_it="Andata o andata e ritorno ?"),
    *roundtrip_step("Max", "Tell him round-trip.", "Clara", "Andata e ritorno",
                     attempt_gap=3.0, char_speaker="Impiegato", char_it="Sono trentacinque euro", tail_gap=1.0),
    *roundtrip_step("Max", "Now ask the platform.", "Clara", "Da che binario ?",
                     attempt_gap=2.5, char_speaker="Impiegato", char_it="Binario otto", tail_gap=2.0),

    ("speech", "Clara", "That's the whole transaction — any city, either ticket type, and you know where you're going.", "en"),
    ("speech", "Max", "Two episodes, three phrases, and none of it forgotten. That's the idea.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: a single short bright acoustic guitar and mandolin phrase like the intro, played once only, does not loop or repeat, winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
