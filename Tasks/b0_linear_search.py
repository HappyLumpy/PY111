"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    arr_min = arr[0]
    index_min = 0
    for index, values in enumerate(arr):
        if values < arr_min:
            arr_min = values
            index_min = index
    return index_min
