from hw.homework1.task02 import check_fibonacci


def test_zero_value_is_fibonacci_seq():
    """Check that 0 is fibonacci seq-ce"""
    list_to_check = [0]
    assert check_fibonacci(list_to_check) == True


def test_one_value_is_fibonacci_seq():
    """Check that 1 is fibonacci seq-ce"""
    list_to_check = [1]
    assert check_fibonacci(list_to_check) == True


def test_first_two_fib_values_seq():
    """Check that 0 is fibonacci seq-ce"""
    list_to_check = [0, 1]
    assert check_fibonacci(list_to_check) == True


def test_first_three_fib_values_seq():
    """Check that correct fib sequences is fibonacci seq-ce"""
    list_to_check = [0, 1, 1]
    assert check_fibonacci(list_to_check) == True


def test_one_value_from_middle_of_fib_seq():
    """Check that correct fib sequences is fibonacci seq-ce"""
    list_to_check = [17711]
    assert check_fibonacci(list_to_check) == True


def test_sequence_not_from_start():
    """Check that correct fib sequences is fibonacci seq-ce"""
    list_to_check = [1597, 2584, 4181, 6765]
    assert check_fibonacci(list_to_check) == True


def test_incorrect_sequence():
    """Check that incorrect fib sequences is fibonacci seq-ce"""
    list_to_check = [1597, 2585, 4181, 6765]
    assert check_fibonacci(list_to_check) == False


def test_incorrect_start_sequence():
    """Check that incorrect fib sequences is fibonacci seq-ce"""
    list_to_check = [1596, 2584, 4181, 6765]
    assert check_fibonacci(list_to_check) == False


def test_incorrent_order_fib_values_seq():
    """Check that incorrect fib sequence is not a fibonacci seq-ce"""
    list_to_check = [0, 1, 1, 3, 2, 5]
    assert check_fibonacci(list_to_check) == False
