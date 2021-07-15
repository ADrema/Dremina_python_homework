"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f'] -- incorrect sample
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""

import itertools
from typing import Iterable


def get_custom_range(source: Iterable, *args):
    start_index, stop_index, step = parse_args(source, args)

    if step < 0:
        return list(itertools.islice(source[::-1], start_index, stop_index + 1, -step))
    else:
        return list(itertools.islice(source, start_index, stop_index, step))


def parse_args(source, args) -> list:
    step = 1 if not args[2] else args[2]

    if step < 0:
        source = source[::-1]

    start_index = source.index(args[0]) if args[0] else 0
    stop_index = source.index(args[1]) if args[1] else len(source)

    return [start_index, stop_index, step]
