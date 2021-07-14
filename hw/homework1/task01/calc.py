# Check that provided value is power of two
#
# Parameters:
# a : value to check
#
# Returns: True or False
def check_value_is_power_of_2(a: int) -> bool:
    return bool((a != 0) and (a & (a - 1) == 0))
