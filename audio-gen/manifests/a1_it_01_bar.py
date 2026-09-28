"""Manifest for scripts/a1-it-01-buongiorno-al-bar.md

Adapted from the .md script's syllable-by-syllable breakdown ("buon-" /
"-giorno") to avoid isolating bare fragments in TTS -- per audio-gen/README.md,
that pattern works when voiced by a human actor but not reliably via AI TTS
(confirmed by the same failure mode on French bare words like "en"/"va").
Every Italian audio chunk here is either a complete real word ("giorno",
"Buongiorno", "Ciao") or the full phrase -- the syllable teaching now happens
entirely in English narration, illustrated by repeating the full word rather
than by isolating an unpronounceable fragment.

Uses eleven_v3 (the model confirmed by ear to handle French phonetics
correctly, unlike turbo_v2_5) with an explicit language_code="it" per call.
Clara/Max reuse the same voice IDs as the French scripts for brand
consistency; Matilda is ElevenLabs-verified for Italian, Chris isn't
explicitly verified for it -- worth an A/B listen before trusting it fully.
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
    ("speech_multi", "Clara", [("en", "Bonjour... oh wait, wrong language!"), ("it", "Ciao, Max!")]),
    ("speech_multi", "Max", [("it", "Ciao, Clara!"), ("en", "Today we're starting something new — Italian.")]),
    ("speech", "Clara", "That's right. And we're going to practice with a scene everyone in Italy knows by heart: standing at the counter of a bar, first thing in the morning.", "en"),
    ("speech_multi", "Max", [
        ("en", "Not \"bar\" like a nightclub — in Italy,"),
        ("it", "il bar"),
        ("en", "is where you grab your morning coffee, standing up, usually in about ninety seconds flat."),
    ]),
    ("speech", "Clara", "Let's listen in.", "en"),
    ("silence", 0.8),

    ("scene", BAR_SCENE),

    ("silence", 2.0),
    ("speech_multi", "Max", [
        ("en", "That word you heard twice —"),
        ("it", "buongiorno"),
        ("en", "— is the single most useful word you'll say in Italy before noon."),
    ]),
    ("speech_multi", "Clara", [
        ("en", "Let's break it down. It's actually two pieces stuck together:"),
        ("it", "buon"),
        ("en", ", meaning good, and"),
        ("it", "giorno"),
        ("en", ", meaning day."),
    ]),
    ("speech_multi", "Max", [("en", "That second piece —"), ("it", "giorno"), ("en", "— is a real word all on its own, so let's start there.")]),
    ("speech", "Clara", "giorno", "it"),
    ("speech", "Max", "Notice that \"gi\" at the start — in Italian, \"g\" before \"i\" or \"e\" sounds like the English \"j\" in \"jump.\" Not a hard \"g\" like in \"go.\"", "en"),
    ("speech", "Clara", "giorno", "it"),
    ("speech", "Clara", "Try it.", "en"),
    ("speech", "Max", "giorno", "it"),
    ("silence", 3.5),

    ("speech", "Max", "giorno", "it"),
    ("sfx", "SPEAKER_SFX", "loud clear electronic beep, short attention tone, like a recording-start alert, bright and audible", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "bright cheerful bell chime, unmistakably a correct-answer ding, loud and clear, upbeat", 0.7),
    ("silence", 1.8),

    ("speech_multi", "Clara", [("en", "Bravo! Now let's put"), ("it", "buon"), ("en", "in front of it.")]),
    ("speech_multi", "Max", [
        ("en", "That \"uo\" in"),
        ("it", "buon"),
        ("en", "isn't two separate sounds like in English \"duo\" — in Italian it glides together into one smooth syllable. And the \"n\" at the end is just a light, clean \"n,\" no nasal trick like in French."),
    ]),
    ("speech", "Clara", "Buongiorno", "it"),
    ("speech", "Max", "Buongiorno", "it"),
    ("speech", "Clara", "One more time, together.", "en"),
    ("speech", "Max", "Buongiorno !", "it"),
    ("silence", 3.5),

    ("speech", "Max", "Buongiorno !", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.8),
    ("speech", "Clara", "Ottimo !", "it"),
    ("silence", 3.0),

    ("speech", "Max", "One more thing before we go — in Italian, the stress matters a lot. It's not on the first part, and it's not spread out evenly either — it's a clear, even push right in the middle.", "en"),
    ("speech", "Clara", "Listen for it.", "en"),
    ("speech", "Clara", "Buongiorno", "it"),
    ("speech", "Max", "Buongiorno", "it"),
    ("speech", "Clara", "Let's hear it a few more times, from different voices around the bar.", "en"),
    ("silence", 0.6),
    ("speech", "Voice1", "Buongiorno !", "it"),
    ("speech", "Voice2", "Buongiorno, buongiorno !", "it"),
    ("speech", "Barista", "Buongiorno, signora !", "it"),
    ("speech", "Max", "Now you know how to walk into any bar in Italy and sound like you belong there.", "en"),
    ("speech_multi", "Clara", [("en", "And next time... we'll actually order that coffee. Two words:"), ("it", "un caffè.")]),
    ("speech", "Max", "Can't wait.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: same bright acoustic guitar and mandolin melody as the intro, but winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
