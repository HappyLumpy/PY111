from typing import List
import random


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) < 2:
        return container
    result = []
    mid = int(len(container) / 2)
    container_left = sort(container[:mid])
    container_right = sort(container[mid:])
    i = 0
    j = 0
    while i < len(container_left) and j < len(container_right):
        if container_left[i] > container_right[j]:
            result.append(container_right[j])
            j += 1
        else:
            result.append(container_left[i])
            i += 1
    result += container_left[i:]
    result += container_right[j:]
    return result


if __name__ == '__main__':
    arr = [random.randint(-100, 100) for _ in range(30)]
    print(sort(arr))
