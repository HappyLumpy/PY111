from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence, fist=45, last=15) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param last:
    :param fist:
    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if fist > last:
        return None
    else:
        mid = (fist + last) // 2
        if arr[mid] < elem:
            binary_search(elem, arr, 0, mid-1)
        elif arr[mid] > elem:
            binary_search(elem, arr, mid+1, 0)
        else:
            return mid


if __name__ == '__main__':
    list_ = list(range(0, 11))
    binary_search(7, list_)


