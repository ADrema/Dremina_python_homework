import pytest

from hw.homework1.task05 import find_max_sub_array_sum

data_provider = [
    ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
    ([3, 6, 7], 3, 16),
    ([3, 6], 3, 9),
    ([26, -1, 0, -3], 3, 26),
    ([11, -1, 0, 26], 3, 26),
    ([-2, -1, 0, 1, 2, 3, -4, -5], 3, 6),
    ([-5, -4, -3, -2, -1], 3, -1)

]


@pytest.mark.parametrize("nums, k, expected", data_provider)
def test_function_returns_max_sub_array_sum(nums, k, expected):
    assert find_max_sub_array_sum(nums, k) == expected
