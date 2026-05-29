# leetcode-ish

A personal practice repo for getting better at **Python** through "leetcode-ish"
coding questions.

## What this is

Every question in here is **completely original** — not copied from LeetCode or any
other site. They're invented fresh, kept in the "easy-ish" range, and meant to build
up Python fundamentals (loops, strings, lists, dicts, indexing, edge cases) one step
at a time.

This is an ongoing thing. New original questions get added over time, and the
difficulty will grow as the fundamentals get solid.

> **Note to Claude:** the user is practicing Python with original "leetcode-ish"
> problems and will keep doing this regularly to improve. When asked for "another
> question," invent a brand-new original problem (never copy real LeetCode ones),
> keep it easy-ish unless told otherwise, and follow the folder layout below.

## Layout

Each problem lives in its own numbered folder:

```
NNN_problem_name/
├── problem.md     # the problem statement, examples, constraints, hint, signature
├── solution.py    # starts as a stub for the user to fill in
└── tests.py       # colorful test runner — run it to check the solution
```

`solution.py` always starts as a stub like:

```python
def some_function(args) -> ...:
    # Write your solution here
    pass
```

The user writes the solution themselves — that's the whole point.

## Problems

| #   | Name              | Difficulty | Topic                        |
| --- | ----------------- | ---------- | ---------------------------- |
| 001 | Max Pair Product  | Easy       | lists, nested loops          |
| 002 | First Unique Char | Easy       | strings, counting            |
| 003 | Word Frequency    | Easy       | dictionaries, counting       |
| 004 | Warmer Days       | Easy       | lists, comparing neighbors   |

## Running the tests

From inside a problem folder:

```bash
cd 004_warmer_days
python tests.py
```

Green ✔ means it passes, red ✘ means it fails.
