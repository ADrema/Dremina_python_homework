import pytest

from hw.homework1.task04 import check_zero_sums_of_elements_in_four_lists

data_provider = [
    ([0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], 256),
    ([0], [0], [0], [0], 1),
    ([-1, -2, -3], [-1, -2, -3], [-1, -2, -3], [-1, -2, -3], 0),
    ([-5, -4, -3], [-2, -1, 0], [1, 2, 3], [4, 5, 0], 10),
    ([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, -12], 1),
]


@pytest.mark.parametrize("a, b, c, d, expected", data_provider)
def test_zero_sums_calculated_correctly(a, b, c, d, expected):
    assert check_zero_sums_of_elements_in_four_lists(a, b, c, d) == expected
