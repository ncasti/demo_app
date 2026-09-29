"""Query/update phrase_registry.json when planning new episodes.

Usage:
    python3 registry_tools.py overdue [--as-of N] [--top N]
        List topical phrases most overdue for review, as of episode N
        (default: highest episode number in the registry + 1, i.e. "now").
        Overdue distance = N minus the episode it was last reviewed in (or
        introduced in, if never reviewed). Glue phrases are excluded --
        they don't need scheduling, they get reviewed for free by being
        used as connective tissue in every episode's banter.

    python3 registry_tools.py add --id foo --it "..." --en "..." \
        --category topical --introduced-in a1_it_26_foo
        Append a new phrase entry (reviewed_in starts empty).

    python3 registry_tools.py review --id foo --episode a1_it_27_bar
        Record that a phrase got a deliberate review in an episode
        (append to its reviewed_in list, if not already there).

This is a planning aid, not something generate.py reads at render time --
manifests are still hand-authored. Run `overdue` before writing a new
practice episode's rapid-review section, so it pulls from what's actually
falling out of memory rather than an arbitrary recent-episodes window.
"""
import argparse
import json
import re
import sys

REGISTRY_PATH = "phrase_registry.json"


def load(path=REGISTRY_PATH):
    with open(path) as f:
        return json.load(f)


def save(data, path=REGISTRY_PATH):
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def episode_number(name):
    m = re.search(r"_(\d+)_", name)
    if not m:
        raise ValueError(f"can't parse episode number from {name!r}")
    return int(m.group(1))


def overdue(data, as_of=None, top_n=8):
    phrases = [p for p in data["phrases"] if p["category"] == "topical"]
    if as_of is None:
        as_of = max(episode_number(p["introduced_in"]) for p in phrases) + 1
    rows = []
    for p in phrases:
        last = max(
            [episode_number(p["introduced_in"])]
            + [episode_number(e) for e in p["reviewed_in"]]
        )
        rows.append((as_of - last, p))
    rows.sort(key=lambda r: -r[0])
    return rows[:top_n]


def cmd_overdue(args):
    data = load(args.registry)
    rows = overdue(data, as_of=args.as_of, top_n=args.top)
    for dist, p in rows:
        last_seen = "never reviewed" if not p["reviewed_in"] else f"last reviewed {p['reviewed_in'][-1]}"
        print(f"  [{dist:>3} eps overdue] {p['it']:<40} ({p['en']}) -- {last_seen}, from {p['introduced_in']}")


def cmd_add(args):
    data = load(args.registry)
    if any(p["id"] == args.id for p in data["phrases"]):
        print(f"ERROR: id {args.id!r} already exists", file=sys.stderr)
        sys.exit(1)
    data["phrases"].append({
        "id": args.id, "it": args.it, "en": args.en,
        "category": args.category, "introduced_in": args.introduced_in,
        "reviewed_in": [],
    })
    save(data, args.registry)
    print(f"added {args.id}")


def cmd_review(args):
    data = load(args.registry)
    for p in data["phrases"]:
        if p["id"] == args.id:
            if args.episode not in p["reviewed_in"]:
                p["reviewed_in"].append(args.episode)
                save(data, args.registry)
                print(f"{args.id}: added review at {args.episode}")
            else:
                print(f"{args.id}: {args.episode} already recorded")
            return
    print(f"ERROR: no phrase with id {args.id!r}", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", default=REGISTRY_PATH)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_overdue = sub.add_parser("overdue")
    p_overdue.add_argument("--as-of", type=int, default=None)
    p_overdue.add_argument("--top", type=int, default=8)
    p_overdue.set_defaults(func=cmd_overdue)

    p_add = sub.add_parser("add")
    p_add.add_argument("--id", required=True)
    p_add.add_argument("--it", required=True)
    p_add.add_argument("--en", required=True)
    p_add.add_argument("--category", required=True, choices=["glue", "topical"])
    p_add.add_argument("--introduced-in", required=True)
    p_add.set_defaults(func=cmd_add)

    p_review = sub.add_parser("review")
    p_review.add_argument("--id", required=True)
    p_review.add_argument("--episode", required=True)
    p_review.set_defaults(func=cmd_review)

    args = parser.parse_args()
    args.func(args)
