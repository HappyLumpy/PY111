"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any

dict_priority = {i: [] for i in range(11)}


def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue
    :param elem: element to be added
    :return: Nothing
    """

    return dict_priority[priority].append(elem)


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    for priority in dict_priority:
        if dict_priority[priority]:
            return dict_priority[priority].pop(0)


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    if ind < len(dict_priority[priority]):
        return dict_priority[priority][ind]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    for priority in dict_priority:
        dict_priority[priority].clear()
