import pytest

from hw.homework2.task02 import get_major_and_minor_list_elements

arrays_data_provider = [
    ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
    ([1, 1, 1], (1, 1)),
    ([5], (5, 5)),
]


@pytest.mark.parametrize("input_list, expected", arrays_data_provider)
def test_(input_list, expected):
    assert get_major_and_minor_list_elements(input_list) == expected
