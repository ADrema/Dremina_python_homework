from hw.homework1.task01.sample_project.calculator.calc import check_value_is_power_of_2

def test_correct_value_case():
    """Check that actual powers of 2 returns True"""
    assert check_value_is_power_of_2(65536)
    
def test_non_power_value_case():
    """Check that non-powers of 2 returns False"""
    assert not check_value_is_power_of_2(12)
