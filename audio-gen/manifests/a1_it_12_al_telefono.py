"""Manifest for scripts/a1-it-12-al-telefono.md

Twelfth Italian A1 episode -- a phone call. Uses lesson_segments.py for the
repeating drill blocks.

No scene ambience for the cold open -- a phone ring/pickup SFX stands in,
since there's no physical location to hold a persistent background bed for.
Elena/Marco reuse the Carlotta / Stefano Ca actors. "Sono [name]" is a
deliberate callback to episode 2's "Io sono" grammar in a new idiomatic
context.
"""

from lesson_segments import speaking_challenge, reverse_translate_item

NAME = "a1_it_12_al_telefono"

CAST = {
    "Clara": "XrExE9yKIg1WjnnlVkGX",  # Matilda - IT-verified
    "Max":   "nH7uLS5UdEnvKEOAXtlQ",  # Vittorio - verified in exactly en+it
    "Elena": "Z9LM7NBnQ8aOZKIXkd5S",  # Carlotta - native Italian
    "Marco": "CEZqCqfrPU34IkHzkV30",  # Stefano Ca - native Italian
}

SEGMENTS = [
    ("sfx", "INTRO_STING", "podcast intro jingle: a single short bright acoustic guitar and light mandolin phrase, played once only, does not loop or repeat, warm Italian morning cafe feel, cheerful and inviting, no vocals", 3.5),
    ("speech", "Max", "Ciao, Clara!", "it"),
    ("speech_multi", "Clara", [
        ("it", "Ciao, Max!"),
        ("en", "Today — the phone. A whole different set of habits than face-to-face."),
    ]),
    ("speech", "Max", "Let's listen in.", "en"),
    ("silence", 0.5),
    ("sfx", "PHONE_RING", "classic landline telephone ringing twice, then picked up with a soft click, no music, no words", 2.5),
    ("silence", 0.3),
    ("speech", "Elena", "Pronto ?", "it"),
    ("silence", 0.3),
    ("speech", "Marco", "Ciao, sono Marco. C'è Elena ?", "it"),
    ("silence", 0.3),
    ("speech", "Elena", "Sono io !", "it"),

    ("silence", 2.0),
    ("speech", "Clara", "Three phrases in there. Let's break them down.", "en"),
    ("speech_multi", "Max", [
        ("en", "First —"),
        ("it", "Pronto?"),
        ("en", "How every Italian phone call starts. Not"),
        ("it", "ciao,"),
        ("en", "not"),
        ("it", "buongiorno"),
        ("en", "— just this."),
    ]),
    ("speech", "Clara", "Repeat after Max.", "en"),
    *speaking_challenge("Max", "Pronto ?", "it"),

    ("speech_multi", "Max", [
        ("en", "Second —"),
        ("it", "Sono Marco,"),
        ("en", "followed by your name. You already know"),
        ("it", "Io sono"),
        ("en", "from introducing yourself — on the phone, Italians just drop the \"io.\""),
    ]),
    ("speech", "Clara", "Sono Clara", "it"),
    ("speech", "Max", "Your turn. Repeat after Clara.", "en"),
    *speaking_challenge("Clara", "Sono Clara", "it"),

    ("speech_multi", "Clara", [
        ("en", "Third — if they're not there:"),
        ("it", "Posso lasciare un messaggio?"),
        ("en", "\"Can I leave a message?\""),
    ]),
    ("speech", "Max", "Posso lasciare un messaggio ?", "it"),
    ("speech", "Clara", "Repeat after Max.", "en"),
    *speaking_challenge("Max", "Posso lasciare un messaggio ?", "it"),
    ("speech", "Clara", "Perfetto !", "it"),
    ("silence", 3.0),

    ("speech", "Max", "Now backwards — I'll say it in English, you say it in Italian.", "en"),
    *reverse_translate_item("Clara", "How do you answer the phone?", "Max", "Pronto ?"),
    *reverse_translate_item("Clara", "How do you say who you are, on the phone?", "Max", "Sono Clara"),
    *reverse_translate_item("Clara", "And how do you ask to leave a message?", "Max", "Posso lasciare un messaggio ?"),

    ("speech", "Clara", "Now put it together — the phone's ringing, and this time you pick up.", "en"),
    ("silence", 1.0),

    ("speech", "Max", "Answer the phone.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.0),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Pronto ?", "it"),
    ("speech", "Max", "It's Elena, asking for you by name. Tell her who you are.", "en"),
    ("sfx", "SPEAKER_SFX", "", 0.7),
    ("silence", 3.5),
    ("sfx", "CORRECT_SFX", "", 0.7),
    ("speech", "Clara", "Sono Clara", "it"),
    ("speech", "Elena", "Ciao, Clara !", "it"),
    ("silence", 2.0),

    ("speech", "Clara", "That's it — you can handle a phone call in Italian now.", "en"),
    ("silence", 2.5),

    ("speech_multi", "Clara", [("en", "So today:"), ("it", "Pronto,"), ("en", "to answer...")]),
    ("speech_multi", "Max", [("it", "Sono Clara,"), ("en", "to say who you are...")]),
    ("speech_multi", "Clara", [("en", "And"), ("it", "Posso lasciare un messaggio"), ("en", "— if they're not in.")]),
    ("speech", "Max", "Next time: the train station.", "en"),
    ("speech", "Clara", "Ciao !", "it"),
    ("speech", "Max", "Ciao !", "it"),
    ("sfx", "OUTRO_STING", "podcast outro jingle: a single short bright acoustic guitar and mandolin phrase like the intro, played once only, does not loop or repeat, winding down gently, warm Italian morning cafe feel, friendly close, no vocals", 3.5),
]
