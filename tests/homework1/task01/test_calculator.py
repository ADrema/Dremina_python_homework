import pytest

from hw.homework1.task01.calc import check_value_is_power_of_2

data_provider = [(65536, True), (1, True), (12, False), (0, False), (-2, False)]


@pytest.mark.parametrize("value_to_check, expected", data_provider)
def test_if_value_is_power_of_two(value_to_check, expected):
    assert check_value_is_power_of_2(value_to_check) == expected
