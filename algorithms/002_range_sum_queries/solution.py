"""
Problem 002: Range Sum Queries (Prefix Sums)

Given an array nums and a list of queries (l, r), return the sum of nums[l..r]
for each query, efficiently.
"""

from typing import List, Tuple


def range_sums(nums: List[int], queries: List[Tuple[int, int]]) -> List[int]:
    # TODO: implement this using an efficient approach
    # Hint: Think about reusing work between queries instead of
    # recomputing sums from scratch each time.
    raise NotImplementedError


def run_tests():
    # Example 1
    nums = [1, 2, 3, 4]
    queries = [(0, 0), (0, 1), (1, 3), (0, 3)]
    expected = [1, 3, 9, 10]
    assert range_sums(nums, queries) == expected

    # Example 2
    nums = [5, -2, 7]
    queries = [(0, 2), (1, 2)]
    expected = [10, 5]
    assert range_sums(nums, queries) == expected

    # Example 3
    nums = [0, 0, 0]
    queries = [(0, 2)]
    expected = [0]
    assert range_sums(nums, queries) == expected

    # Edge case: single element
    nums = [42]
    queries = [(0, 0)]
    expected = [42]
    assert range_sums(nums, queries) == expected

    # Edge case: multiple queries on same range
    nums = [1, 2, 3]
    queries = [(0, 2), (0, 2), (0, 2)]
    expected = [6, 6, 6]
    assert range_sums(nums, queries) == expected

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
