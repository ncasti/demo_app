"""Manifest for scripts/a1-it-02-piacere.md

Second Italian A1 episode -- introducing yourself. Written to test whether
the episode-1 pedagogy and production pipeline scale to new content, after
episode 1's listening-feedback fixes were already folded into standing
practice:
- Max's voice is Vittorio (en+it verified) from the start, not Chris --
  verified_languages was checked before writing a line of dialogue this
  time, not discovered as a bug after generating.
- Marco/Giulia reuse the already-verified native voices from episode 1's
  montage (Stefano Ca, Carlotta), recast as named characters -- same actors,
  different scenario, same as a recurring bit-part voice cast.
- Every target-language word/phrase quoted inside an English-tagged chunk is
  pulled into its own speech_multi chunk, and no chunk is isolated below
  2-3 words (see audio-gen/README.md's two production rules).
- Reverse-translate and round-trip sections use the corrected cue order
  from episode 1's fix: prompt -> SPEAKER_SFX -> silence (attempt) ->
  CORRECT_SFX -> answer. Written this way from the start here, not patched
  in after generating.
"""

NAME = "a1_it_02_piacere"

CAST = {
    "Clara":  "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":    "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Marco":  "CEZqCqfrPU34IkHzkV30",  # Stefano Ca - native Italian
    "Giulia": "Z9LM7NBnQ8aOZKIXkd5S",  # Carlotta - native Italian
}

PIAZZA_SCENE = {
    "key": "PIAZZA",
    "lang": "it",
    "ambience_prompt": "continuous loopable outdoor Italian piazza ambience, distant fountain, occasional footsteps and pigeons, quiet murmur, no music, no words",
    "start_prompt": "brief outdoor city square ambience begins, fountain and distant footsteps fade in",
    "end_prompt": "brief pause, piazza ambience continues, footsteps receding",
    "start_dur": 1.5,
    "end_dur": 1.3,
    "lead": 0.8,
    "tail": 1.0,
    "turn_gap": 0.5,
    "lines": [
        ("Marco", "Ciao, mi chiamo Marco."),
        ("Giulia", "Piacere, Marco! Io sono Giulia."),
        ("Marco", "Piacere, Giulia!"),
    ],
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: a single short bright acoustic guitar and light mandolin phrase, played once only, does not loop or repeat, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Max", "Ciao, Clara!", "it"),
    ("speech_multi", "Clara", [
        ("it", "Ciao, Max!"),
        ("en", "Last time we ordered a coffee. Today — the next thing you'll need: introducing yourself."),
    ]),
    ("speech", "Max", "Let's listen in. Two people meeting for the first time in a piazza.", "en"),
    ("silence", 0.8),

    ("scene", PIAZZA_SCENE),

    ("silence", 2.0),
    ("speech", "Clara", "Three phrases in there. Let's break them down.", "en"),
    ("speech_multi", "Max", [
        ("en", "First —"),
        ("it", "Mi chiamo,"),
        ("en", "followed by your name. It literally means \"I call myself,\" but it's just how you say \"my name is.\""),
    ]),
    ("speech", "Clara", "Repeat after Max.", "en"),

    ("speech", "Max", "Mi chiamo Max.", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.5),
    ("speech", "Max", "Mi chiamo Max.", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.8),

    ("speech_multi", "Max", [
        ("en", "Second —"),
        ("it", "Piacere."),
        ("en", "You heard both Marco and Giulia say it. It means \"nice to meet you\" — or literally, \"pleasure.\""),
    ]),
    ("speech", "Clara", "Piacere.", "it"),
    ("speech", "Max", "Your turn. Repeat after Clara.", "en"),

    ("speech", "Clara", "Piacere !", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.5),
    ("speech", "Clara", "Piacere !", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.8),

    ("speech_multi", "Clara", [
        ("en", "Third — Giulia also said"),
        ("it", "Io sono Giulia."),
        ("en", "Same meaning as \"mi chiamo,\" just a different way to say it — \"I am Giulia.\" Italians use both, so you'll hear this one just as often."),
    ]),
    ("speech", "Max", "Io sono Max.", "it"),
    ("speech", "Clara", "Repeat after Max.", "en"),

    ("speech", "Max", "Io sono Max.", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.5),
    ("speech", "Max", "Io sono Max.", "it"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("silence", 1.8),
    ("speech", "Clara", "Perfetto !", "it"),
    ("silence", 3.0),

    ("speech", "Max", "Now backwards — I'll say it in English, you say it in Italian.", "en"),

    ("speech", "Clara", "How do you say \"my name is,\" before your name?", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech_multi", "Max", [("en", "That's right —"), ("it", "Mi chiamo.")]),
    ("silence", 1.8),

    ("speech", "Clara", "How do you say \"nice to meet you\"?", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech_multi", "Max", [("en", "That's right —"), ("it", "Piacere !")]),
    ("silence", 1.8),

    ("speech", "Clara", "And the other way to say \"I am,\" before your name?", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech_multi", "Max", [("en", "That's right —"), ("it", "Io sono.")]),
    ("silence", 2.0),

    ("speech", "Clara", "Now put it together — you've just walked up to someone in a piazza.", "en"),
    ("silence", 1.0),

    ("speech", "Max", "Introduce yourself. Say \"my name is,\" and your name.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Mi chiamo Clara.", "it"),
    ("speech", "Max", "And Giulia answers:", "en"),
    ("speech", "Giulia", "Piacere, Clara! Io sono Giulia.", "it"),
    ("silence", 1.2),

    ("speech", "Max", "Now say it back to her — \"nice to meet you.\"", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 2.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Piacere, Giulia !", "it"),
    ("silence", 2.0),

    ("speech", "Clara", "That's it — you can walk up to anyone in Italy and introduce yourself now.", "en"),
    ("silence", 2.5),

    ("speech_multi", "Clara", [("en", "So today:"), ("it", "Mi chiamo,"), ("en", "to give your name...")]),
    ("speech_multi", "Max", [("it", "Piacere,"), ("en", "when you meet someone...")]),
    ("speech_multi", "Clara", [("en", "And"), ("it", "Io sono"), ("en", "— the other way to say \"I am.\"")]),
    ("speech", "Max", "Next time: shopping at the market, and asking how much something costs.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: a single short bright acoustic guitar and mandolin phrase like the intro, played once only, does not loop or repeat, winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
