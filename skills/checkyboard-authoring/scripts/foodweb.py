#!/usr/bin/env python3
"""Inspect food-to-consumer paths; never predict survival or population sizes."""
import argparse
from collections import deque
import json
from pathlib import Path
import sys


def analyze(data, removed):
    nodes, producers, edges = data["nodes"], data["producers"], data["edges"]
    if not isinstance(nodes, list) or any(not isinstance(n, str) or not n for n in nodes) or len(nodes) != len(set(nodes)):
        raise ValueError("nodes must be unique nonempty strings")
    if not isinstance(producers, list) or not set(producers) <= set(nodes) or len(producers) != len(set(producers)):
        raise ValueError("producers must be unique known nodes")
    removed = set(removed)
    if not removed <= set(producers):
        raise ValueError("this helper only removes known producers")
    if not isinstance(edges, list) or any(not isinstance(e, list) or len(e) != 2 or any(n not in nodes for n in e) or e[0] == e[1] for e in edges):
        raise ValueError("edges must be food-to-consumer node pairs without self edges")
    incoming = {n: set() for n in nodes}
    outgoing = {n: set() for n in nodes}
    for food, consumer in edges:
        if consumer in producers:
            raise ValueError("producer cannot have an incoming food edge in this model")
        incoming[consumer].add(food)
        outgoing[food].add(consumer)
    animals = set(nodes) - set(producers)
    direct = sorted(n for n in animals if incoming[n] and incoming[n] <= removed)
    path = {p: [p] for p in sorted(set(producers) - removed)}
    queue = deque(path)
    while queue:
        n = queue.popleft()
        for consumer in sorted(outgoing[n]):
            if consumer not in removed and consumer not in path:
                path[consumer] = path[n] + [consumer]
                queue.append(consumer)
    return {"removed_producers": sorted(removed), "direct_food_loss": direct,
            "no_remaining_producer_path": sorted(animals - set(path)),
            "supported_paths": {n: path[n] for n in sorted(animals & set(path))},
            "unfed_nodes": sorted(n for n in animals if not incoming[n]),
            "limits": "A remaining path is not evidence of guaranteed survival or stable population. Direct and indirect effects differ."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--remove", action="append", required=True)
    args = parser.parse_args()
    try:
        result = analyze(json.loads(args.source.read_text(encoding="utf-8-sig")), args.remove)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
