"""Pre-generation linter for manifests -- catches the mechanical production-rule
violations documented in README.md's "Curriculum structure"/production-rules
sections before spending an API call on them, instead of catching them by ear
after the fact (which is how all of these were found the first time).

Usage:
    python3 lint_manifest.py manifests/a1_it_28_whatever.py
    python3 lint_manifest.py manifests/*.py          # lint everything
    python3 lint_manifest.py manifests/*.py --strict  # exit 1 if anything found

Checks (see README.md for the full story behind each):
1. Trailing period(s) on a short isolated Italian TTS string -- risks the
   model reading the period aloud as "dot."
2. A single bare Italian word used as its own isolated chunk, unless it's on
   the allowlist of words already confirmed safe by ear (complete
   greetings/exclamations like "Buongiorno," "Grazie"). Everything else
   (verb/preposition stems like "Sono," "Vorrei," "Cerco," "Dov'è") is
   flagged -- these need a filler to form a natural 2-3 word phrase.
3. An Italian word from the phrase registry's own vocabulary appearing
   (quoted or not) inside an English-tagged chunk -- the chunk's `lang`
   governs the whole chunk, so this reads with English phonetics.

This is deliberately NOT a check for content/narrative consistency (e.g. the
Florence/Firenze mixup) -- nothing here is syntactically wrong in that class
of bug, it needs an actual read-through, not a pattern match. That's what
the editorial pass is for.
"""
import argparse
import importlib.util
import json
import os
import re
import sys

# Complete, idiomatically-whole Italian words/exclamations confirmed safe
# alone by ear across episodes 1-27. Grammatically "thin" stems (a verb or
# preposition that needs an object to be a full phrase) are deliberately NOT
# on this list even if short, per the "Sono" finding.
SAFE_BARE_WORDS = {
    "buongiorno", "grazie", "prego", "scusi", "pronto", "piacere", "ciao",
    "perfetto", "ecco", "ottimo", "certo", "sì", "subito",
    # Not greetings/courtesy words like the rest of this list -- "bar" is a
    # complete noun (not a verb/preposition stem needing an object), added
    # when episode 1's script review asked for it to be spoken in Italian
    # specifically because it's a false-friend vocabulary word under
    # discussion, not translated English.
    "bar",
}

REGISTRY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "phrase_registry.json")


def load_italian_vocab():
    """Every distinct Italian word appearing in phrase_registry.json, for the
    English-chunk-leakage check. Lowercased, punctuation stripped."""
    if not os.path.exists(REGISTRY_PATH):
        return set()
    with open(REGISTRY_PATH) as f:
        data = json.load(f)
    words = set()
    for p in data["phrases"]:
        for w in re.findall(r"[A-Za-zÀ-ÿ']+", p["it"]):
            if len(w) >= 4:  # skip short words like "un", "a", "ho" -- too many false positives
                words.add(w.lower())
    return words


def word_count(text):
    return len(re.findall(r"[A-Za-zÀ-ÿ']+", text))


def strip_punct(text):
    return text.strip().rstrip(",;:")


def check_trailing_period(text, loc, findings):
    stripped = strip_punct(text)
    if re.search(r"\.+$", stripped):
        findings.append(f"{loc}: trailing period(s) on Italian text {text!r} -- risks being read as \"dot\"")


def check_bare_word(text, loc, findings):
    stripped = strip_punct(text)
    core = re.sub(r"[.!?]+$", "", stripped).strip()
    if word_count(core) == 1 and core.lower() not in SAFE_BARE_WORDS:
        findings.append(f"{loc}: bare single Italian word {text!r} not on the safe list -- needs a filler (e.g. \"Sono\" -> \"Sono Clara\")")


def check_english_leakage(text, loc, vocab, findings):
    for w in re.findall(r"[A-Za-zÀ-ÿ']+", text):
        if w.lower() in vocab:
            findings.append(f"{loc}: possible Italian word {w!r} inside an English-tagged chunk {text!r} -- pull it into its own (\"it\", ...) chunk")


def lint_segments(segments, name, vocab):
    findings = []
    for i, seg in enumerate(segments):
        kind = seg[0]
        loc_base = f"{name}[{i}]"
        if kind == "speech":
            _, speaker, text, lang = seg
            loc = f"{loc_base} speech/{speaker}"
            if lang == "it":
                check_trailing_period(text, loc, findings)
                check_bare_word(text, loc, findings)
            elif lang == "en":
                check_english_leakage(text, loc, vocab, findings)
        elif kind == "speech_multi":
            _, speaker, chunks = seg
            for j, (lang, text) in enumerate(chunks):
                loc = f"{loc_base} speech_multi/{speaker}[{j}]"
                if lang == "it":
                    check_trailing_period(text, loc, findings)
                    check_bare_word(text, loc, findings)
                elif lang == "en":
                    check_english_leakage(text, loc, vocab, findings)
        elif kind == "scene":
            _, scene = seg
            lang = scene.get("lang", "it")
            for j, (speaker, text) in enumerate(scene.get("lines", [])):
                loc = f"{loc_base} scene/{scene['key']}/{speaker}[{j}]"
                if lang == "it":
                    check_trailing_period(text, loc, findings)
                    check_bare_word(text, loc, findings)
    return findings


def lint_file(path, vocab):
    spec = importlib.util.spec_from_file_location("m", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return lint_segments(mod.SEGMENTS, os.path.basename(path), vocab)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("manifests", nargs="+")
    parser.add_argument("--strict", action="store_true", help="exit 1 if any findings")
    args = parser.parse_args()

    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    vocab = load_italian_vocab()

    total = 0
    for path in args.manifests:
        findings = lint_file(path, vocab)
        if findings:
            print(f"\n{os.path.basename(path)}: {len(findings)} finding(s)")
            for f in findings:
                print(f"  - {f}")
            total += len(findings)

    print(f"\n{total} total finding(s) across {len(args.manifests)} file(s).")
    if args.strict and total:
        sys.exit(1)
