"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


# Calculates zero sums in arrays
#
# Example:
# Given integer lists: A, B, C, D
# compute how many tuple's elements have (i, j, k, l) A[i] + B[j] + C[k] + D[l] zero sum.
#
# Parameters:
# a,b,c,d : integer lists
#
# Returns: number of zeroes sums in tuples of the lists
def check_zero_sums_of_elements_in_four_lists(
    a: List[int], b: List[int], c: List[int], d: List[int]
) -> int:
    counter = int()  # zero sums counter

    for i in a:
        for j in b:
            for k in c:
                for l in d:
                    if i + j + k + l == 0:
                        counter += 1
    return counter
