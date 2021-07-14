import pytest

from hw.homework1.task02 import check_fibonacci

data_provider = [
    ([0], True),
    ([1], True),
    ([0, 1], True),
    ([0, 1, 1], True),
    ([17711], True),
    ([1597, 2584, 4181, 6765], True),
    ([1597, 2585, 4181, 6765], False),
    ([1596, 2584, 4181, 6765], False),
    ([0, 1, 1, 3, 2, 5], False),
]


@pytest.mark.parametrize("sequence_to_check, expected", data_provider)
def test_if_value_is_fibonacci_seq(sequence_to_check, expected):
    assert check_fibonacci(sequence_to_check) == expected
