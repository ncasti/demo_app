"""Manifest for scripts/a1-it-26-alla-stazione-uno.md

Pilot for the new chapter template (see audio-gen/README.md's "Curriculum
structure" section): 2 new phrases instead of 3, each drilled with a
substitution variant (not a verbatim repeat), reverse-translate/round-trip
using a THIRD filler never drilled directly (tests the pattern, not rote
memorization of one sentence). Part 1 of 2 -- part 2
(a1_it_27_alla_stazione_due) opens by reviewing these phrases with yet
another fresh filler, then adds one more new phrase and chains everything
into one transaction.

Same scenario and native cast as episode 13's version of this topic
(Alessandro/Impiegato, Carla/Cliente) -- this is a rebuild of that content
under the new template, not a replacement for episode 13.
"""

from lesson_segments import speaking_challenge, reverse_translate_item, roundtrip_step

NAME = "a1_it_26_alla_stazione_uno"

CAST = {
    "Clara":     "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":       "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Impiegato": "JfznbVXrGXYh0gZo9Lcp",  # Alessandro - native Italian
    "Cliente":   "litDcG1avVppv4R90BLu",  # Carla - native Italian
}

STATION_SCENE = {
    "key": "STAZIONE26",
    "lang": "it",
    "ambience_prompt": "continuous loopable train station ambience, distant announcements, rolling luggage, quiet crowd murmur, no music, no words",
    "start_prompt": "brief train station ambience begins, distant announcement and rolling luggage fade in",
    "end_prompt": "brief pause, station ambience continues, distant announcement",
    "start_dur": 1.5,
    "end_dur": 1.3,
    "lead": 0.8,
    "tail": 1.0,
    "turn_gap": 0.5,
    "lines": [
        ("Cliente", "Un biglietto per Roma, per favore"),
        ("Impiegato", "Andata o andata e ritorno?"),
        ("Cliente", "Solo andata"),
        ("Impiegato", "Sono quindici euro"),
    ],
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: a single short bright acoustic guitar and light mandolin phrase, played once only, does not loop or repeat, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Clara", "Ciao, Max!", "it"),
    ("speech_multi", "Max", [
        ("it", "Ciao, Clara!"),
        ("en", "Today we're doing something a little different — this topic gets two episodes instead of one, so we can actually drill it properly."),
    ]),
    ("speech", "Clara", "Let's listen in. The ticket window at the station.", "en"),
    ("silence", 0.8),

    ("scene", STATION_SCENE),

    ("silence", 2.0),
    ("speech", "Max", "Two phrases in there. Let's break them down — and this time, we'll practice each one two different ways.", "en"),
    ("speech_multi", "Clara", [
        ("en", "First —"),
        ("it", "Un biglietto per Roma, per favore"),
        ("en", "\"A ticket to Rome, please.\" Roma is just one destination — swap in any city."),
    ]),
    ("speech", "Clara", "Repeat after Max.", "en"),
    *speaking_challenge("Max", "Un biglietto per Roma, per favore.", "it"),

    ("speech", "Clara", "Now the same phrase, different city — this is what actually makes it useful. Say it for Milano this time.", "en"),
    *speaking_challenge("Max", "Un biglietto per Milano, per favore.", "it"),

    ("speech_multi", "Max", [
        ("en", "Second — when they ask round-trip or one-way:"),
        ("it", "Solo andata"),
        ("en", "\"One-way only.\""),
    ]),
    ("speech", "Clara", "Solo andata", "it"),
    ("speech", "Max", "Your turn. Repeat after Clara.", "en"),
    *speaking_challenge("Clara", "Solo andata.", "it"),

    ("speech_multi", "Max", [
        ("en", "And the other way to answer:"),
        ("it", "Andata e ritorno"),
        ("en", "\"Round-trip.\""),
    ]),
    *speaking_challenge("Clara", "Andata e ritorno.", "it"),
    ("speech", "Clara", "Perfetto !", "it"),
    ("silence", 3.0),

    ("speech", "Max", "Now backwards — and I'll mix up the cities and ticket types, not just repeat what you just heard.", "en"),
    *reverse_translate_item("Clara", "How do you ask for a ticket to Milan?", "Max", "Un biglietto per Milano, per favore."),
    *reverse_translate_item("Clara", "How do you ask for a round-trip?", "Max", "Andata e ritorno."),
    *reverse_translate_item("Clara", "And how do you ask for a ticket to Rome, one-way?", "Max", "Un biglietto per Roma, per favore. Solo andata.", attempt_gap=3.5),

    ("speech", "Clara", "Now put it together — you're at the window, and this time it's a city we haven't practiced yet: Napoli.", "en"),
    ("silence", 1.0),
    *roundtrip_step("Max", "Ask for a ticket to Naples.", "Clara", "Un biglietto per Napoli, per favore.",
                     narration="He asks round-trip or one-way:", char_speaker="Impiegato", char_it="Andata o andata e ritorno ?"),
    *roundtrip_step("Max", "Your choice — tell him round-trip.", "Clara", "Andata e ritorno.",
                     attempt_gap=3.0, char_speaker="Impiegato", char_it="Sono trenta euro.", tail_gap=2.0),

    ("speech", "Clara", "Two phrases, but now you can actually use them anywhere — any city, either way.", "en"),
    ("speech", "Max", "Next time — part two. We'll pick up right at this window, and add the one question everyone forgets to ask.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: a single short bright acoustic guitar and mandolin phrase like the intro, played once only, does not loop or repeat, winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
