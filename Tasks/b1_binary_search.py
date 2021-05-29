from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    fist = 0
    last = len(arr) - 1
    mid = (fist + last) // 2
    while fist <= last and arr[mid] != elem:
        if elem > arr[mid]:
            fist = mid + 1
        else:
            last = mid - 1
        mid = (fist + last) // 2
    if fist > last:
        return None
    else:
        while mid > 0 and arr[mid - 1] == elem:
            mid = mid - 1
        return mid


if __name__ == '__main__':
    list_ = list(range(0, 11))
    print(binary_search(3, list_))
