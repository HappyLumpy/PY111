from typing import List
import random

def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    n = len(container)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if container[j] > container[j + 1]:
                container[j], container[j + 1] = container[j + 1], container[j]
    return container


if __name__ == '__main__':
    arr = [10, 9, 8, 7, 6, 6, 4, 3, 2, 1]
    print(sort(arr))