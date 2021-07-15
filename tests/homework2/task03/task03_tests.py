import pytest

from hw.homework2.task03 import get_lists_of_possible_combinations

test_input_params = [1, 2], [3, 4]
data_provider = [
    (
        test_input_params,
        [
            [1, 3],
            [1, 4],
            [2, 3],
            [2, 4],
        ],
    )
]


@pytest.mark.parametrize("input_data, expected", data_provider)
def test_function_which_generates_lists_combinations(input_data, expected):
    assert get_lists_of_possible_combinations([1, 2], [3, 4]) == expected
