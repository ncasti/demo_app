"""Manifest for scripts/a1-it-01-buongiorno-al-bar.md

NOT YET RENDERED -- this is ready to run (`python3 generate.py
audio-gen/manifests/a1_it_01_bar.py`) but hasn't been executed, so the cast
below hasn't been ear-tested for Italian the way the French casts have.
Clara/Max reuse the same voice IDs as the French scripts for brand
consistency across languages; Matilda is ElevenLabs-verified for Italian,
Chris isn't explicitly verified for it (still likely fine via the
multilingual model, but worth an A/B listen before trusting it).
"""

NAME = "a1_it_01_bar"

CAST = {
    "Clara":    "XrExE9yKIg1WjnnlVkGX",  # Matilda - warm, professional host (F, IT-verified, multilingual)
    "Max":      "iP95p4xoKVk53GoZ742B",  # Chris - charming, down-to-earth host (M, multilingual, IT not verified -- spot check)
    "Barista":  "JfznbVXrGXYh0gZo9Lcp",  # Antonio - natural, balanced, calm (M, native Italian)
    "Cliente":  "litDcG1avVppv4R90BLu",  # Carla - natural, reflective, narrative (F, native Italian)
    "Voice1":   "CEZqCqfrPU34IkHzkV30",  # Stefano Ca - energetic & friendly (M, native Italian, "older man" line)
    "Voice2":   "Z9LM7NBnQ8aOZKIXkd5S",  # Carlotta - fresh, fun (F, native Italian, "young woman" line)
}

BAR_SCENE = {
    "key": "BAR",
    "lang": "it",
    "ambience_prompt": "continuous loopable ambience inside a small Italian coffee bar, espresso machine hiss, cups clinking on saucers, quiet morning chatter, no music, no words",
    "start_prompt": "espresso machine hiss and a cup set down on a saucer, morning bar ambience begins",
    "end_prompt": "coffee cup set down on a saucer, brief pause, bar ambience continues",
    "start_dur": 1.5,
    "end_dur": 1.5,
    "lead": 0.8,
    "tail": 1.2,
    "turn_gap": 0.5,
    "lines": [
        ("Barista", "Buongiorno !"),
        ("Cliente", "Buongiorno !"),
    ],
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: bright acoustic guitar and light mandolin melody, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Clara", "Bonjour... oh wait, wrong language! Ciao, Max!", "en"),
    ("speech", "Max", "Ciao, Clara! Today we're starting something new — Italian.", "en"),
    ("speech", "Clara", "That's right. And we're going to practice with a scene everyone in Italy knows by heart: standing at the counter of a bar, first thing in the morning.", "en"),
    ("speech", "Max", "Not \"bar\" like a nightclub — in Italy, \"il bar\" is where you grab your morning coffee, standing up, usually in about ninety seconds flat.", "en"),
    ("speech", "Clara", "Let's listen in.", "en"),
    ("silence", 0.8),

    ("scene", BAR_SCENE),

    ("silence", 2.0),
    ("speech", "Max", "That word you heard twice — \"buongiorno\" — is the single most useful word you'll say in Italy before noon.", "en"),
    ("speech", "Clara", "Let's break it down. It's actually two pieces stuck together: \"buon-\" and \"-giorno.\"", "en"),
    ("speech", "Max", "Buon- means \"good.\"", "en"),
    ("speech", "Clara", "Buon-", "it"),
    ("speech", "Max", "Buon-", "it"),
    ("speech", "Clara", "Good. Now, that \"uo\" in the middle isn't two separate sounds like in English \"duo\" — in Italian it glides together into one smooth syllable.", "en"),
    ("speech", "Clara", "buon-", "it"),
    ("speech", "Max", "buon-", "it"),
    ("speech", "Clara", "And the \"n\" at the end — just a light, clean \"n,\" no nasal trick like in French. Straightforward.", "en"),
    ("speech", "Max", "buon-", "it"),
    ("silence", 3.5),

    ("speech", "Max", "buon-", "it"),
    ("sfx", "SPEAKER_SFX", "loud clear electronic beep, short attention tone, like a recording-start alert, bright and audible", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "bright cheerful bell chime, unmistakably a correct-answer ding, loud and clear, upbeat", 0.7),
    ("silence", 1.8),

    ("speech", "Clara", "Bravo! Now the second half — \"-giorno.\"", "en"),
    ("speech", "Max", "-giorno. Notice that \"gi\" at the start — in Italian, \"g\" before \"i\" or \"e\" sounds like the English \"j\" in \"jump.\" Not a hard \"g\" like in \"go.\"", "en"),
    ("speech", "Clara", "-giorno", "it"),
    ("speech", "Clara", "Try it.", "en"),
    ("speech", "Max", "-giorno", "it"),
    ("speech", "Clara", "And \"-orno\" at the end — round, open vowels, nothing swallowed. Every vowel in Italian gets its full, clear sound.", "en"),
    ("speech", "Clara", "-orno", "it"),
    ("speech", "Max", "-orno", "it"),
    ("speech", "Max", "giorno", "it"),
    ("silence", 3.5),

    ("speech", "Max", "buon-", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.8),
    ("speech", "Max", "-giorno", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.8),
    ("speech", "Max", "Buongiorno !", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.8),
    ("speech", "Clara", "Ottimo !", "it"),
    ("silence", 3.0),

    ("speech", "Max", "One more thing before we go — in Italian, the stress matters a lot. It's not BUON-giorno and it's not buon-GIOR-no dragged out...", "en"),
    ("speech", "Clara", "It's buonGIORno — a clean, even push right on that middle syllable.", "en"),
    ("speech", "Clara", "buonGIORno", "it"),
    ("speech", "Max", "buonGIORno", "it"),
    ("speech", "Clara", "Let's hear it a few more times, from different voices around the bar.", "en"),
    ("silence", 0.6),
    ("speech", "Voice1", "Buongiorno !", "it"),
    ("speech", "Voice2", "Buongiorno, buongiorno !", "it"),
    ("speech", "Barista", "Buongiorno, signora !", "it"),
    ("speech", "Max", "Now you know how to walk into any bar in Italy and sound like you belong there.", "en"),
    ("speech", "Clara", "And next time... we'll actually order that coffee. Two words: \"un caffè.\"", "en"),
    ("speech", "Max", "Can't wait.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: same bright acoustic guitar and mandolin melody as the intro, but winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
