"""Manifest for scripts/a1-it-05-scusi-dove.md

Fifth Italian A1 episode (fourth new-content episode after the practice
episode) -- asking for directions. Follows the same production practices
established in episodes 1-3: Max is Vittorio (en+it verified), no bare
single-word isolation without a natural surrounding phrase, every
target-language word quoted in an English-tagged chunk is pulled into its
own speech_multi chunk.

Turista reuses episode 1/3's Cliente actor (Carla), Passante reuses episode
1's Voice1 / episode 2's Marco actor (Stefano Ca) -- recurring native cast,
new scenario.

Reverse-translate and round-trip sections use the corrected cue order:
prompt -> SPEAKER_SFX -> silence (attempt) -> CORRECT_SFX -> answer. See
episode 1's docstring for why -- the first draft played the answer before
SPEAKER_SFX, giving it away before the listener could attempt it.
"""

NAME = "a1_it_05_scusi_dove"

CAST = {
    "Clara":    "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":      "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Turista":  "litDcG1avVppv4R90BLu",  # Carla - native Italian
    "Passante": "CEZqCqfrPU34IkHzkV30",  # Stefano Ca - native Italian
}

STREET_SCENE = {
    "key": "STREET",
    "lang": "it",
    "ambience_prompt": "continuous loopable outdoor Italian city street ambience, distant traffic, occasional passing footsteps, quiet, no music, no words",
    "start_prompt": "brief outdoor street ambience begins, distant traffic and footsteps fade in",
    "end_prompt": "brief pause, street ambience continues, distant traffic",
    "start_dur": 1.5,
    "end_dur": 1.3,
    "lead": 0.8,
    "tail": 1.0,
    "turn_gap": 0.5,
    "lines": [
        ("Turista", "Scusi, dov'è la stazione?"),
        ("Passante", "È sempre dritto, poi a destra."),
        ("Turista", "Grazie mille!"),
        ("Passante", "Prego!"),
    ],
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: a single short bright acoustic guitar and light mandolin phrase, played once only, does not loop or repeat, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Max", "Ciao, Clara!", "it"),
    ("speech_multi", "Clara", [
        ("it", "Ciao, Max!"),
        ("en", "Coffee, introductions, the market — today, the part every tourist eventually needs: asking for directions."),
    ]),
    ("speech", "Max", "Let's listen in. A street corner, someone looking a little lost.", "en"),
    ("silence", 0.8),

    ("scene", STREET_SCENE),

    ("silence", 2.0),
    ("speech", "Clara", "Three phrases in there. Let's break them down.", "en"),
    ("speech_multi", "Max", [
        ("en", "First —"),
        ("it", "Scusi."),
        ("en", "It means \"excuse me\" — how you get a stranger's attention before asking anything."),
    ]),
    ("speech", "Clara", "Repeat after Max.", "en"),

    ("speech", "Max", "Scusi.", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.5),
    ("speech", "Max", "Scusi.", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.8),

    ("speech_multi", "Max", [
        ("en", "Second —"),
        ("it", "Dov'è,"),
        ("en", "followed by whatever you're looking for. It means \"where is.\""),
    ]),
    ("speech", "Clara", "Dov'è la stazione ?", "it"),
    ("speech", "Max", "Your turn. Repeat after Clara.", "en"),

    ("speech", "Clara", "Dov'è la stazione ?", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.5),
    ("speech", "Clara", "Dov'è la stazione ?", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.8),

    ("speech_multi", "Clara", [
        ("en", "Third — the answer you'll hear most often:"),
        ("it", "Sempre dritto."),
        ("en", "Straight ahead. Useful to recognize even before you can give directions yourself."),
    ]),
    ("speech", "Max", "Sempre dritto.", "it"),
    ("speech", "Clara", "Repeat after Max.", "en"),

    ("speech", "Max", "Sempre dritto.", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.5),
    ("speech", "Max", "Sempre dritto.", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.8),
    ("speech", "Clara", "Perfetto !", "it"),
    ("silence", 3.0),

    ("speech", "Max", "Now backwards — I'll say it in English, you say it in Italian.", "en"),

    ("speech", "Clara", "How do you get a stranger's attention?", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech_multi", "Max", [("en", "That's right —"), ("it", "Scusi.")]),
    ("silence", 1.8),

    ("speech", "Clara", "How do you ask where the station is?", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech_multi", "Max", [("en", "That's right —"), ("it", "Dov'è la stazione ?")]),
    ("silence", 1.8),

    ("speech", "Clara", "And how do you say \"straight ahead\"?", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech_multi", "Max", [("en", "That's right —"), ("it", "Sempre dritto.")]),
    ("silence", 2.0),

    ("speech", "Clara", "Now put it together — you're lost, and this time you're the one asking.", "en"),
    ("silence", 1.0),

    ("speech", "Max", "Get his attention.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Scusi !", "it"),
    ("speech", "Max", "He stops:", "en"),
    ("speech", "Passante", "Sì ?", "it"),
    ("silence", 1.2),

    ("speech", "Max", "Ask him where the station is.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Dov'è la stazione ?", "it"),
    ("speech", "Max", "He points you the way:", "en"),
    ("speech", "Passante", "È sempre dritto, poi a destra.", "it"),
    ("silence", 1.2),

    ("speech", "Max", "Thank him.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Grazie mille !", "it"),
    ("speech", "Max", "And he answers:", "en"),
    ("speech", "Passante", "Prego !", "it"),
    ("silence", 2.0),

    ("speech", "Clara", "That's it — you're no longer lost.", "en"),
    ("silence", 2.5),

    ("speech_multi", "Clara", [("en", "So today:"), ("it", "Scusi,"), ("en", "to get someone's attention...")]),
    ("speech_multi", "Max", [("it", "Dov'è,"), ("en", "to ask where something is...")]),
    ("speech_multi", "Clara", [("en", "And"), ("it", "Sempre dritto"), ("en", "— straight ahead.")]),
    ("speech", "Max", "Next time, we'll put together a full curriculum's worth of scenarios — this was just the scale test.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: a single short bright acoustic guitar and mandolin phrase like the intro, played once only, does not loop or repeat, winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
