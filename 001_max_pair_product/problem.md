# 001 — Max Pair Product

**Difficulty:** Easy

---

## Problem

Given a list of integers, return the **maximum product** you can make by multiplying any two elements at **different indices**.

---

## Examples

**Example 1:**
```
Input:  [3, 5, 2, 8]
Output: 40
Explanation: 5 * 8 = 40
```

**Example 2:**
```
Input:  [-5, -3, 1, 2]
Output: 15
Explanation: -5 * -3 = 15  (two negatives make a positive)
```

**Example 3:**
```
Input:  [0, 0, 5]
Output: 0
Explanation: best you can do is 5 * 0 = 0
```

---

## Constraints

- `2 <= len(nums) <= 10^4`
- `-10^4 <= nums[i] <= 10^4`

---

## Signature

```python
def max_pair_product(nums: list[int]) -> int:
```
