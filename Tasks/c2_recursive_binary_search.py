from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    fist = 0
    last = len(arr) - 1
    mid = (fist + last) // 2
    print(arr)
    if arr[mid] == elem:
        return mid
    else:
        if elem < arr[mid] != elem:
            last = mid - 1
            arr = arr[:last]
            return binary_search(elem, arr)
        else:
            fist = mid + 1
            arr = arr[fist:]
            return binary_search(elem, arr)


if __name__ == '__main__':
    list_ = list(range(0, 11))
    binary_search(8, list_)
