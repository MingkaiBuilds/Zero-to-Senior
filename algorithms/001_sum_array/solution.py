"""
Problem 001: Sum Array

Write a function `sum_array(nums: list[int]) -> int` that returns the sum of
all integers in the list.

Examples:
- sum_array([1, 2, 3]) -> 6
- sum_array([]) -> 0
- sum_array([-1, 5]) -> 4
"""

from typing import List


def sum_array(nums: List[int]) -> int:
    array_sum = 0

    for num in nums:
        array_sum += num
    
    return array_sum


def run_tests():
    # Basic tests
    assert sum_array([1, 2, 3]) == 6
    assert sum_array([]) == 0
    assert sum_array([-1, 5]) == 4

    # You will add more tests here as you think of edge cases
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
