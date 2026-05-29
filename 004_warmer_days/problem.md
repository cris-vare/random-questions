# 004 — Warmer Days

**Difficulty:** Easy

---

## Problem

You are given a list of integers `temps` representing the temperature on each day, in order.

Return the number of days that were **strictly warmer than the day before**.

The very first day has no day before it, so it never counts.

---

## Examples

**Example 1:**
```
Input:  [70, 72, 68, 75, 75]
Output: 2
Explanation:
  day 1: 72 > 70  → warmer ✔
  day 2: 68 > 72  → not warmer
  day 3: 75 > 68  → warmer ✔
  day 4: 75 > 75  → not warmer (equal is not strictly warmer)
```

**Example 2:**
```
Input:  [60, 61, 62, 63]
Output: 3
Explanation: every day is warmer than the one before it.
```

**Example 3:**
```
Input:  [80, 79, 78]
Output: 0
Explanation: it only gets colder.
```

**Example 4:**
```
Input:  [50]
Output: 0
Explanation: a single day has no previous day to compare against.
```

---

## Constraints

- `1 <= len(temps) <= 10^4`
- `-100 <= temps[i] <= 100`

---

## Hint

Compare each day to the one right before it. You can loop starting from
index `1` and look back at index `i - 1`:

```python
for i in range(1, len(temps)):
    if temps[i] > temps[i - 1]:
        ...
```

"Strictly warmer" means `>`, not `>=` — an equal temperature does not count.

---

## Signature

```python
def warmer_days(temps: list[int]) -> int:
```
