# CP-31 Problem 004 — Sliding Window (Sum Window)

## Problem Statement

You are given:
- an integer **N**
- an array of **N** positive integers
- an integer **S**

Your task is to find the **length of the longest contiguous subarray** whose **sum is ≤ S**.

Print a single integer — the maximum window length.

---

## Input Format

- First line: N S  
- Second line: N positive integers

---

## Constraints

- 1 ≤ N ≤ 200000  
- 1 ≤ array[i] ≤ 10^9  
- 1 ≤ S ≤ 10^18  
- Must run in under **1 second** in Python

---

## Explanation

This problem introduces the second major sliding window type:

### ✔ Distinct Window  
Expand until invalid (duplicate encountered) — shrink until valid.

### ✔ Sum Window (THIS PROBLEM)  
Expand until sum exceeds S — shrink until sum becomes ≤ S again.

This pattern is very common in:
- subarray sum problems  
- two-pointer optimizations  
- greedy + sliding window hybrids  
- AtCoder ABC tasks  
- Codeforces Div2 B/C  

---

## Your Goal (Before Coding)

1. Explain why positive integers allow a sliding window solution  
2. Describe how the window should expand and contract  
3. Decide what variable(s) you maintain (hint: sum)  
4. State the optimal time and space complexity  
5. List at least 2 edge cases

Only reason — do NOT code yet.

---

## Hints (Do Not Delete)

- Keep a running sum  
- Expand right pointer  
- While sum > S, shrink left pointer  
- Track best window size  

---

## Expected Output Format

Print exactly one integer — the answer.

---

## Example (Not a solution)

Input:
