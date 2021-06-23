"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence

global_previous_fib_value = int()  # stores previous fibonacci value


# Check that provided sequence is a part of fibonacci sequence
#
# Parameters:
# data : sequence to check
#
# Returns: True or False
def check_fibonacci(data: Sequence[int]) -> bool:
    expected_sequence = get_fibonacci_sequence(data[0], len(data))

    if data == expected_sequence:
        return True
    else:
        return False


def get_fibonacci_sequence(start_from: int, length: int):
    fib_sequence = []
    a, b = 0, 1
    counter = 0

    while True:
        if a < start_from:
            a, b = b, a + b
            continue

        if a > start_from:
            return fib_sequence

        if a == start_from:

            while counter < length:
                fib_sequence.append(a)
                a, b = b, a + b
                counter += 1
                continue
            break

    return fib_sequence
