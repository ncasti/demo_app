"""Reusable segment-builders for the repeat-after-me / reverse-translate /
round-trip patterns used by every A1 Italian episode since a1_it_01_bar.

Factored out after episode 5: five episodes of hand-copying the same three
block shapes turned up a real bug (episodes 1-2's first draft played the
answer before SPEAKER_SFX ever fired, see audio-gen/README.md). Centralizing
the shapes here means that class of bug can only happen once, not once per
episode. A manifest builds SEGMENTS from unique content (intro banter, scene
dialogue, phrase-breakdown narration, recap) plus calls into these for the
repeating drill blocks.

All three follow the same cue contract, fixed after the episode 1/2 bug:
    prompt/instruction -> SPEAKER_SFX -> silence (attempt) -> CORRECT_SFX -> answer
SPEAKER_SFX is the cue to speak, not a cue that speaking is already over.
"""


def speaking_challenge(speaker, text, lang, reps=2, attempt_gap=2.5, between_gap=1.5, tail_gap=1.8):
    """Listen-then-repeat drill: model says the phrase, listener repeats it.

    Unlike reverse_translate_item/roundtrip_step, the model's line comes
    FIRST here on purpose -- this is a listening/repetition drill, not a
    recall test, so hearing the target phrase modeled before attempting it
    is correct, not a spoiler.
    """
    segs = []
    for i in range(reps):
        segs.append(("speech", speaker, text, lang))
        segs.append(("sfx", "SPEAKER_SFX", "", 0.7))
        segs.append(("silence", attempt_gap))
        segs.append(("sfx", "CORRECT_SFX", "", 0.7))
        segs.append(("silence", tail_gap if i == reps - 1 else between_gap))
    return segs


def reverse_translate_item(prompt_speaker, prompt_text, answer_speaker, answer_it, attempt_gap=3.0, tail_gap=1.8):
    """English prompt -> listener attempts Italian -> host confirms with the answer."""
    return [
        ("speech", prompt_speaker, prompt_text, "en"),
        ("sfx", "SPEAKER_SFX", "", 0.7),
        ("silence", attempt_gap),
        ("sfx", "CORRECT_SFX", "", 0.7),
        ("speech_multi", answer_speaker, [("en", "That's right —"), ("it", answer_it)]),
        ("silence", tail_gap),
    ]


def roundtrip_step(instr_speaker, instr_text, listener_speaker, listener_it,
                    attempt_gap=3.5, narration=None, char_speaker=None, char_it=None, tail_gap=1.2):
    """One beat of a "join the conversation" round-trip: instruction -> attempt
    -> the listener's line (voiced by a host standing in for the listener) ->
    optional narration -> optional native character's in-scene response.
    """
    segs = [
        ("speech", instr_speaker, instr_text, "en"),
        ("sfx", "SPEAKER_SFX", "", 0.7),
        ("silence", attempt_gap),
        ("sfx", "CORRECT_SFX", "", 0.7),
        ("speech", listener_speaker, listener_it, "it"),
    ]
    if narration:
        segs.append(("speech", instr_speaker, narration, "en"))
    if char_speaker:
        segs.append(("speech", char_speaker, char_it, "it"))
    segs.append(("silence", tail_gap))
    return segs
