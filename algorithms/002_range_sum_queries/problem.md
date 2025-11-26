# Problem 002: Range Sum Queries (Prefix Sums)

You are given:
- An integer array `nums` of length `n`.
- A list of queries, where each query is a pair `(l, r)` representing **0-based** indices into `nums`.

For each query `(l, r)`, you must return the sum:

`nums[l] + nums[l+1] + ... + nums[r]`

### Requirements

- Implement a function:

  ```python
  from typing import List, Tuple

  def range_sums(nums: List[int], queries: List[Tuple[int, int]]) -> List[int]:
      ...
