from hw.homework1.task05 import find_max_sub_array_sum


def test_provided_in_task_case():
    """Check"""
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = 16
    assert find_max_sub_array_sum(nums, k) == result


def test_array_with_length_equal_to_k_case():
    """Check list with length equal to K"""
    nums = [3, 6, 7]
    k = 3
    result = 16
    assert find_max_sub_array_sum(nums, k) == result


def test_array_with_length_less_than_k_case():
    """Check list with length less than K"""
    nums = [3, 6]
    k = 3
    result = 9
    assert find_max_sub_array_sum(nums, k) == result


def test_array_with_single_first_positive_value_case():
    """Check list negative values and one max first element"""
    nums = [26, -1, 0, -3]
    k = 3
    result = 26
    assert find_max_sub_array_sum(nums, k) == result


def test_array_with_single_last_positive_value_case():
    """Check list negative values and one max last element"""
    nums = [11, -1, 0, 26]
    k = 3
    result = 26
    assert find_max_sub_array_sum(nums, k) == result


def test_case_with_max_sum_in_the_middle_case():
    """Check list negative values and middle max sum element"""
    nums = [-2, -1, 0, 1, 2, 3, -4, -5]
    k = 3
    result = 6
    assert find_max_sub_array_sum(nums, k) == result


def test_negative_elements_array_case():
    """Check negative list result"""
    nums = [-5, -4, -3, -2, -1]
    k = 3
    result = -1
    assert find_max_sub_array_sum(nums, k) == result
