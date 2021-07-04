"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple

# import networkx as nx

root = None


def create_node(key, value):
    return {'key': key, 'value': value, 'left': None, 'right': None}


def _find(key) -> Tuple[Optional[dict],Optional[dict]]:
    global root
    prev_root = None
    current_root = root
    while current_root is not None:
        if key > current_root['key']:
            prev_root = current_root
            current_root = current_root['right']
        elif key < current_root['key']:
            prev_root = current_root
            current_root = current_root['left']
        else:
            break
    return prev_root,current_root

def insert(key: int, value: Any) -> None:
    """
    Insert (key, value) pair to binary search tree

    :param key: key from pair (key is used for positioning node in the tree)
    :param value: value associated with key
    :return: None
    """
    global root
    if root is None:
        root = create_node(key, value)
    current_node = root
    while True:
        if key > current_node['key']:
            if current_node['right'] is None:
                current_node['right'] = create_node(key, value)
                return
            else:
                current_node = current_node['right']

        elif key < current_node['key']:
            if current_node['left'] is None:
                current_node['left'] = create_node(key, value)
                return
            else:
                current_node = current_node['left']
        else:
            current_node['value'] = value
            return


def remove(key: int) -> Optional[Tuple[int, Any]]:
    """
    Remove key and associated value from the BST if exists

    :param key: key to be removed
    :return: deleted (key, value) pair or None
    """
    global root
    prev, current = _find(key)
    if current is None:
        return
    current_node_right = current['right']
    current_node_left = current['left']
    prev_node_right = None
    prev_node_left = None
    if root['key'] == current['key']:
        while current_node_right ['left'] is not None:
                prev_node_right = current_node_right
                current_node_right = current_node_right['left']
        root = current_node_right
        prev_node_right['left'] = None
        root['right'] = current['right']
        root['left'] = current['left']
        return current['key'],current['value']
    if current['left'] is None and current['right'] is None:
        if prev['key'] > current['key']:
            prev['left'] = None
            return current['key'],current['value']
        elif prev['key'] < current['key']:
            prev['right'] = None
            return current['key']['value']
    if current['left'] is not None and current['right'] is None:
        prev['left'] = current['left']
        return current['key'],current['value']
    if current['right'] is not None and current['left'] is None:
        prev['left'] = current['right']
        return current['key'],current['value']
    if current['right'] is not None and current['left'] is not None:
        if root['key'] < current['key']:
            if current['left']['right'] is not None:
                while current_node_left['right'] is not None:
                    prev_node_left = current_node_left
                    current_node_left = current_node_left['right']
                    break
                prev['left'] = current_node_left
                current_node_left['right'] = current['right']
                current_node_left['left'] = current['left']
                prev_node_left['right'] = None
                return current['key'],current['value']
            else:
                prev['left'] = current['right']
                current['right']['left'] = current['left']
                return current['key'],current['value']
        if root['key'] > current['key']:
            if current['left']['right'] is not None:
                while current_node_right ['left'] is not None:
                    prev_node_right = current_node_right
                    current_node_right = current_node_right['left']
                    break
                prev['left'] = current_node_right
                current_node_right['left'] = current['left']
                current_node_right['right'] = current['right']
                prev_node_right['left'] = None
                return current['key'],current['value']
            else:
                prev['left'] = current['left']
                current['left']['right'] = current['right']
                return current['key'],current['value']


def find(key: int) -> Optional[Any]:
    """
    Find value by given key in the BST

    :param key: key for search in the BST
    :return: value associated with the corresponding key
    """
    if root is None:
        raise KeyError
    current_node = root
    while True:
        if key > current_node['key']:
            if current_node['right'] is None:
                raise KeyError
            else:
                current_node = current_node['right']
        elif key < current_node['key']:
            if current_node['left'] is None:
                raise KeyError
            else:
                current_node = current_node['left']
        elif key == current_node['key']:
            return current_node['value']


def clear() -> None:
    """
    Clear the tree

    :return: None
    """
    global root
    root = None


def main():
    clear()
    insert(15,'это 15')
    insert(10, 'это 10')
    insert(12, 'это 12')
    insert(14, 'это 14')
    insert(11, 'это 11')
    insert(5, 'это 5')
    insert(7, 'это 7')
    insert(3, 'это 3')
    insert(20, 'это 20')
    insert(25, 'это 25')
    insert(30, 'это 30')
    insert(18, 'это 18')
    insert(19, 'это 19')
    insert(16, 'это 16')
    print(remove(20))

if __name__ == '__main__':
    main()