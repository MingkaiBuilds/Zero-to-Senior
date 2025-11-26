# Puzzle 000 — Pair Sum Feasibility

## Problem Statement

You are given an integer N, followed by N integers, and then a target value T.
Your task is to determine whether any pair of numbers in the list sums exactly to T.

Output:
- "YES" if such a pair exists
- "NO" otherwise

---

## Input Constraints

- 1 ≤ N ≤ 200000
- Each number is in the range [-1e9, +1e9]
- The solution must run within 1 second in Python
- Memory is sufficient for standard CP solutions, but not for O(N^2) approaches

---

## Your Goal (Before Coding)

Before writing a single line of Python:

1. Identify the underlying pattern
2. Determine the ideal time complexity
3. Choose the correct data structure
4. List edge cases that could break naive logic

Think about:
- fast lookups
- avoiding nested loops
- linear vs quadratic complexity
- duplicate values
- large negative or positive integers

Do NOT implement the solution yet.

---

## Mini Self-Hints (Do NOT delete)

- What operation needs to be repeated many times?
- What structure gives you O(1) average lookup?
- Could sorting help? What trade-offs would it introduce?
- How do you avoid using the same element twice?
- What about negative numbers?

---

## Expected Output Format

Print exactly one line:

YES
or
NO

---

## Example (Not a Solution)

Input:
5
2 7 11 15 4
9

Output:
YES

Explanation: 2 + 7 = 9
