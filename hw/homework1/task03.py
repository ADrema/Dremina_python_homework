"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from typing import Tuple


# Get max and min values from file
#
# Parameters:
# file_name : file name to get values
#
# Returns: tuple[int, int] with min and max file value
def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    params = list()

    with open(file_name) as file:
        for line in file:
            params += (int(x) for x in line.split(", "))

    return min(params), max(params)
