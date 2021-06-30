import string

import pytest

from hw.homework2.task05 import get_custom_range

data_provider = [
    (string.ascii_lowercase, "p", "g", -2, ["p", "n", "l", "j", "h"]),
    (string.ascii_lowercase, "g", "p", 2, ["g", "i", "k", "m", "o"]),
    (string.ascii_lowercase, "t", None, None, ["t", "u", "v", "w", "x", "y", "z"]),
    (
        string.ascii_lowercase,
        "g",
        "p",
        None,
        ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
    ),
    (string.ascii_lowercase, "g", None, -1, ["g", "f", "e", "d", "c", "b", "a"]),
]


@pytest.mark.parametrize("iterable_source,start, stop, step, expected", data_provider)
def test_f(iterable_source, start, stop, step, expected):
    assert get_custom_range(iterable_source, start, stop, step) == expected
