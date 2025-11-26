# CP-31 Problem 002 — Frequency Map Basics

## Problem Statement

You are given an array of **N** integers.  
Your task is to determine whether **any value appears at least twice** in the array.

Print:
- "YES" if any duplicate exists  
- "NO" otherwise

---

## Input Format

- First line: integer N  
- Second line: N integers

---

## Constraints

- 1 ≤ N ≤ 200000  
- Values lie in the range [-1e9, 1e9]

Must run in under **1 second** in Python.

---

## Explanation

This problem introduces the foundational **frequency map pattern**, used in nearly all contest problems involving:

- duplicate detection  
- counts  
- grouping  
- hashing  
- sliding window  
- greedy heuristics  
- parity logic  
- prefix sum extensions  

A value appears twice **iff** we encounter it again after seeing it once before.

---

## Your Goal (Before Coding)

1. Describe the optimal time complexity  
2. Identify the best data structure to track frequencies  
3. Reason about why your approach guarantees correctness  
4. List at least 2 edge cases

Do **NOT** implement yet.  
Think in terms of pattern recognition.

---

## Hints (Do Not Delete)

- What operation must be fast?  
- Is full counting necessary?  
- Do you need to store indices?  
- What structure yields O(1) membership tests?

---

## Expected Output Format

Print exactly:

