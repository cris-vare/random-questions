# 003 — Word Frequency

**Difficulty:** Easy

---

## Problem

Given a sentence as a string, return a **dictionary** where each key is a word and its value is how many times that word appears.

Words are **case-insensitive** — `"The"` and `"the"` count as the same word.

---

## Examples

**Example 1:**
```
Input:  "the cat sat on the mat"
Output: {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}
```

**Example 2:**
```
Input:  "hello hello hello"
Output: {"hello": 3}
```

**Example 3:**
```
Input:  "one"
Output: {"one": 1}
```

**Example 4:**
```
Input:  "The the THE"
Output: {"the": 3}
Explanation: all three are the same word after lowercasing.
```

---

## Constraints

- `1 <= len(sentence) <= 10^4`
- The sentence contains only letters and spaces
- Words are separated by a single space
- No punctuation

---

## Hint

A dictionary in Python lets you store key-value pairs:
```python
d = {}
d["cat"] = 1    # adds key "cat" with value 1
d["cat"] += 1   # now "cat" is 2
```

But be careful — if you try to do `d["cat"] += 1` when `"cat"` doesn't exist yet, Python will crash.
You need to check if the key exists first.

---

## Signature

```python
def word_frequency(sentence: str) -> dict:
```
