from typing import List
import random


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    result = []
    if len(container) < 2:
        return container
    mid = int(len(container) / 2)
    container_left = sort(container[:mid])
    container_right = sort(container[mid:])
    while len(container_left) > 0 and len(container_right) > 0:
        if container_left[0] > container_right[0]:
            result.append(container_right[0])
            container_right.pop(0)
        else:
            result.append(container_left[0])
            container_left.pop(0)
    result += container_left
    result += container_right
    return result


if __name__ == '__main__':
    arr = [random.randint(-100, 100) for _ in range(30)]
    print(sort(arr))
