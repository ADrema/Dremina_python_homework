from hw.homework1.task01.calc import check_value_is_power_of_2


def test_correct_value_case():
    """Check that actual powers of 2 returns True"""
    assert check_value_is_power_of_2(65536)


def test_one_value_case():
    """Check that 1 returns True"""
    assert check_value_is_power_of_2(1)


def test_non_power_value_case():
    """Check that non-powers of 2 returns False"""
    assert not check_value_is_power_of_2(12)


def test_zero_case():
    """Check that 0 returns False"""
    assert not check_value_is_power_of_2(0)


def test_negative_value_case():
    """Check that  negative value returns False"""
    assert not check_value_is_power_of_2(-2)
