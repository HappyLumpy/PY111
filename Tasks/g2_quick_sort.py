from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    less = []
    middle = []
    greater = []

    if len(container) > 1:
        current = container[0]
        for x in container:
            if x < current:
                less.append(x)
            elif x == current:
                middle.append(x)
            elif x > current:
                greater.append(x)
        return sort(less) + middle + sort(greater)
    else:
        return container
