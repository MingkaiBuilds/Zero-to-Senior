# CP-31 Problem 001 — Prefix Sum Existence

## Problem Statement

You are given an array of **N** integers.  
Your task is to determine whether **any non-empty subarray** has a total sum equal to **0**.

Output:
- "YES" if such a subarray exists  
- "NO" otherwise  

---

## Input Format

- First line: integer N  
- Second line: N integers (array values)

---

## Constraints

- 1 ≤ N ≤ 200000  
- Each integer lies in the range [-1e9, 1e9]  
- Must run in under 1 second in Python  

---

## Explanation

A subarray has sum 0 if (and only if):

1. A prefix sum repeats  
   (i.e., prefix[i] == prefix[j] for some i < j)  
2. OR any prefix sum itself is 0  

This is the foundational **prefix sum existence** pattern.

---

## Your Goal (Before Coding)

1. Explain why a repeated prefix sum means a zero-sum subarray exists  
2. Determine what data structure is best for checking this efficiently  
3. Determine the ideal time complexity  
4. List potential edge cases

Do **NOT** write code yet.  
Reason about the pattern.

---

## Hints (Do Not Delete)

- What does prefix[j] − prefix[i] represent?  
- What happens if prefix[j] == prefix[i]?  
- What structure supports fast repeated-checking?  
- What if an element itself is 0?

---

## Expected Output Format

Print exactly:

