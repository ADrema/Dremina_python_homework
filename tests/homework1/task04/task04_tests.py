from hw.homework1.task04 import check_zero_sums_of_elements_in_four_lists


def test_four_length_zeroes_tuples_case():
    """Check 4 symbols tuples zeroes sum"""
    a = [0, 0, 0, 0]
    b = [0, 0, 0, 0]
    c = [0, 0, 0, 0]
    d = [0, 0, 0, 0]
    result_zero_sum_count = 256
    assert (
        check_zero_sums_of_elements_in_four_lists(a, b, c, d) == result_zero_sum_count
    )


def test_single_zero_tuples_case():
    """Check single tuples zeroes sum"""
    a = [0]
    b = [0]
    c = [0]
    d = [0]
    result_zero_sum_count = 1
    assert (
        check_zero_sums_of_elements_in_four_lists(a, b, c, d) == result_zero_sum_count
    )


def test_negative_tuples_case():
    """Check negative tuples zeroes sum"""
    a = [-1, -2, -3]
    b = [-1, -2, -3]
    c = [-1, -2, -3]
    d = [-1, -2, -3]
    result_zero_sum_count = 0
    assert (
        check_zero_sums_of_elements_in_four_lists(a, b, c, d) == result_zero_sum_count
    )


def test_multiple_tuples_case():
    """Check multiple values tuples zeroes sum"""
    a = [-5, -4, -3]
    b = [-2, -1, 0]
    c = [1, 2, 3]
    d = [4, 5, 0]
    result_zero_sum_count = 10
    assert (
        check_zero_sums_of_elements_in_four_lists(a, b, c, d) == result_zero_sum_count
    )


def test_one_single_zeroes_sum_case():
    """Check multiple values tuples zeroes sum"""
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [7, 8, 9]
    d = [10, 11, -12]
    result_zero_sum_count = 1
    assert (
        check_zero_sums_of_elements_in_four_lists(a, b, c, d) == result_zero_sum_count
    )
