# CP-31 Problem 003 — Sliding Window (Distinct Window)

## Problem Statement

You are given an array of **N** integers.  
Your task is to determine the **length of the longest contiguous subarray** in which **all elements are distinct**.

Print a single integer — the maximum length.

---

## Input Format

- First line: integer N  
- Second line: N integers

---

## Constraints

- 1 ≤ N ≤ 200000  
- Values may be as large as ±1e9  
- Must run in under **1 second** in Python

---

## Explanation

This problem introduces the core **sliding window** pattern:
- a window that can expand (move right pointer)
- and shrink (move left pointer)
until it satisfies a condition (all elements distinct)

This is the foundation for:
- longest unique substring  
- subarray with at most K distinct values  
- sliding sum problems  
- two-pointer interval logic  
- frequency-controlled windows  

---

## Your Goal (Before Coding)

1. Explain why a simple two-pointer window works  
2. Identify which data structure tracks which elements are in the window  
3. Determine the update rules when the window becomes invalid (duplicate found)  
4. State the ideal time and space complexity  
5. List at least 2 edge cases

Do NOT code yet — reason first.

---

## Hints (Do Not Delete)

- Window expands with `right += 1`  
- Shrinks with `left += 1`  
- A frequency map is typically involved  
- Shrink until the window is valid again  
- Track the maximum size of the window

---

## Expected Output Format

Print exactly one integer — the answer.

---

## Example (Not a solution)

Input:
