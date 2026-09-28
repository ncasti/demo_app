"""Manifest for scripts/a1-it-04-practice-uno.md

First spaced-repetition practice episode -- no new vocabulary. Recombines
the eight repertoire phrases from episodes 1-3 (bar, introductions, market)
into one continuous "day in Italy" so the listener has to produce them from
memory. Per the curriculum's spaced-repetition plan, a practice episode goes
in every 2-3 new episodes.

Deliberately lighter production than the teaching episodes: no persistent
scene ambience (recall-focused, not atmosphere-focused), single-pass drills
instead of double reps, shorter pauses -- a review should move faster than a
lesson. Reuses the same native voices as episodes 1-3 (Barista/Alessandro,
Giulia/Carlotta, Venditore/Alessandro) for a consistent recurring cast.

Both the rapid-review and full-day sections use the corrected cue order:
prompt -> SPEAKER_SFX -> silence (attempt) -> CORRECT_SFX -> answer. See
episode 1's docstring for why -- the first draft played the answer before
SPEAKER_SFX, giving it away before the listener could attempt it.
"""

NAME = "a1_it_04_practice_uno"

CAST = {
    "Clara":     "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":       "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Barista":   "JfznbVXrGXYh0gZo9Lcp",  # Alessandro - native Italian
    "Giulia":    "Z9LM7NBnQ8aOZKIXkd5S",  # Carlotta - native Italian
    "Venditore": "JfznbVXrGXYh0gZo9Lcp",  # Alessandro - native Italian
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: bright acoustic guitar and light mandolin melody, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Clara", "Ciao, Max!", "it"),
    ("speech", "Max", "Ciao, Clara! No new words today — this one's a practice episode. Everything you've learned so far, in one day.", "en"),
    ("speech", "Clara", "Coffee, introducing yourself, and the market. Let's warm up first — fast round, English to Italian, no repeats this time.", "en"),
    ("silence", 2.0),

    ("speech", "Max", "How do you greet someone, before evening?", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech_multi", "Clara", [("en", "That's right —"), ("it", "Buongiorno !")]),
    ("silence", 1.5),

    ("speech", "Max", "How do you order a coffee, politely?", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech_multi", "Clara", [("en", "That's right —"), ("it", "Un caffè, per favore.")]),
    ("silence", 1.5),

    ("speech", "Max", "And how do you say thank you — and you're welcome?", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech_multi", "Clara", [("en", "That's right —"), ("it", "Grazie ! ... Prego !")]),
    ("silence", 1.5),

    ("speech", "Max", "How do you give your name?", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech_multi", "Clara", [("en", "That's right —"), ("it", "Mi chiamo...")]),
    ("silence", 1.5),

    ("speech", "Max", "How do you say \"nice to meet you\"?", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech_multi", "Clara", [("en", "That's right —"), ("it", "Piacere !")]),
    ("silence", 1.5),

    ("speech", "Max", "And the other way to say \"I am\"?", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech_multi", "Clara", [("en", "That's right —"), ("it", "Io sono...")]),
    ("silence", 1.5),

    ("speech", "Max", "How do you politely ask for something?", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech_multi", "Clara", [("en", "That's right —"), ("it", "Vorrei...")]),
    ("silence", 1.5),

    ("speech", "Max", "How do you ask the price?", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech_multi", "Clara", [("en", "That's right —"), ("it", "Quanto costa ?")]),
    ("silence", 3.0),

    ("speech", "Max", "Perfetto! Now let's use all of it — one full day, start to finish. You're doing every part this time.", "en"),
    ("silence", 2.0),

    ("speech", "Max", "You walk up to the counter. Greet the barista.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Buongiorno !", "it"),
    ("speech", "Barista", "Buongiorno !", "it"),

    ("speech", "Max", "Order a coffee.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Un caffè, per favore.", "it"),
    ("speech", "Barista", "Ecco a lei.", "it"),
    ("speech", "Clara", "Grazie !", "it"),
    ("speech", "Barista", "Prego !", "it"),
    ("silence", 1.5),

    ("speech", "Max", "Coffee in hand, you meet someone in the piazza. Introduce yourself.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Mi chiamo Clara.", "it"),
    ("speech", "Giulia", "Piacere, Clara! Io sono Giulia.", "it"),
    ("speech", "Clara", "Piacere, Giulia !", "it"),
    ("silence", 1.5),

    ("speech", "Max", "Now you're at the market. Ask for some apples.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Vorrei delle mele, per favore.", "it"),
    ("speech", "Venditore", "Certo !", "it"),

    ("speech", "Max", "Ask the price.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Quanto costa ?", "it"),
    ("speech", "Venditore", "Sono due euro.", "it"),
    ("speech", "Clara", "Ecco a lei. Grazie !", "it"),
    ("speech", "Venditore", "Prego !", "it"),
    ("silence", 2.0),

    ("speech", "Clara", "That's a whole day — coffee, a new friend, and a trip to the market — all in Italian.", "en"),
    ("speech", "Max", "No new words next time either — well, almost. We'll pick it back up with a practice-free episode after this one: asking for directions.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: same bright acoustic guitar and mandolin melody as the intro, but winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
