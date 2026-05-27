# 002 — First Unique Character

**Difficulty:** Easy

---

## Problem

Given a string `s`, return the **first character** that appears **exactly once** in the string.

If every character repeats at least twice, return `""` (empty string).

Uppercase and lowercase letters are treated as **different characters** (`'A' != 'a'`).

---

## Examples

**Example 1:**
```
Input:  "leetcode"
Output: "l"
Explanation: 'l' appears once, and it's the first such character.
```

**Example 2:**
```
Input:  "aabb"
Output: ""
Explanation: 'a' appears twice, 'b' appears twice — no unique character.
```

**Example 3:**
```
Input:  "aabbc"
Output: "c"
Explanation: 'a' and 'b' both repeat, 'c' appears only once.
```

**Example 4:**
```
Input:  "abacabad"
Output: "c"
Explanation: 'a' appears 4 times, 'b' appears 2 times, 'c' appears once first at index 4.
             Wait — scan in order: 'a'(4x), 'b'(2x), 'c'(1x) ✔
```

---

## Constraints

- `1 <= len(s) <= 10^5`
- `s` contains only printable ASCII characters (letters, digits, symbols)

---

## Signature

```python
def first_unique_char(s: str) -> str:
```
