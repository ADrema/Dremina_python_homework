from hw.homework1.task03 import find_maximum_and_minimum


def test_one_line_file():
    """Check that one line file is processed correctly"""
    result = (1, 5)
    assert find_maximum_and_minimum("../task03/oneLine.txt") == result


def test_multiple_line_file():
    """Check that multiple line file is processed correctly"""
    result = (0, 10)
    assert find_maximum_and_minimum("../task03/multipleFile.txt") == result


def test_single_value_file():
    """Check that single value file is processed correctly"""
    result = (5, 5)
    assert find_maximum_and_minimum("../task03/singleValueFile.txt") == result


def test_negative_values_file():
    """Check that file with negative values is processed correctly"""
    result = (-6, -1)
    assert find_maximum_and_minimum("../task03/negativeValuesFile.txt") == result
