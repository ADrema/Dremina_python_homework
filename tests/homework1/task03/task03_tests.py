import pytest

from hw.homework1.task03 import find_maximum_and_minimum

data_provider = [
    ("../task03/oneLine.txt", (1, 5)),
    ("../task03/multipleFile.txt", (0, 10)),
    ("../task03/singleValueFile.txt", (5, 5)),
    ("../task03/negativeValuesFile.txt", (-6, -1)),
]


@pytest.mark.parametrize("file_path, expected", data_provider)
def test_calculated_max_and_min_values(file_path, expected):
    assert find_maximum_and_minimum(file_path) == expected
