from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence, fist=0, last=1) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param last:
    :param fist:
    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if last < fist:
        return None
    else:
        midval = fist + ((last - fist) // 2)
        if arr[midval] > elem:
            return binary_search(elem, arr, fist, midval - 1)
        elif arr[midval] < elem:
            return binary_search(elem, arr, midval + 1, last+1)
        else:
            return midval


if __name__ == '__main__':
    list_ = list(range(0, 200))
    print(binary_search(199, list_))
