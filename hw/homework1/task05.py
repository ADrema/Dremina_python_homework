"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less or equal to "k" and  with max sum.
List may contain only negative numbers

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_max_sub_array_sum(nums: List[int], k: int) -> int:
    max_sum = nums[0]

    for i in range(len(nums)):
        curr_max_sum = find_max_array_sum(nums[i : i + k])
        max_sum = curr_max_sum if curr_max_sum > max_sum else max_sum

    return max_sum


# Finds max elements sum of array
#
# Parameters:
#
# array: list to define max sum
def find_max_array_sum(array: List[int]) -> int:
    max_sum = max(array)
    curr_sum = int()

    for i in array:
        curr_sum += i
        max_sum = curr_sum if curr_sum > max_sum else max_sum

    return max_sum
