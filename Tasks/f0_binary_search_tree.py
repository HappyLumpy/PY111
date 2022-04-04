"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""
from typing import Any, Optional, Tuple

# import networkx as nx

root = None


def create_node(key, value):
    return {'key': key, 'value': value, 'left': None, 'right': None}


def _find(key) -> Tuple[Optional[dict], Optional[dict]]:
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
    return prev_root, current_root


def insert(key: int, value: Any) -> None:
    """
    Insert (key, value) pair to binary search tree

    :param key: key from pair (key is used for positioning node in the tree)
    :param value: value associated with key
    :return: None
    """
    global root
    prev, current = _find(key)
    if current is not None:
        current['value'] = value
    elif prev is None:
        root = create_node(key, value)
    else:
        if key > prev['key']:
            prev['right'] = create_node(key, value)
        if key < prev['key']:
            prev['left'] = create_node(key, value)


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
    if root['key'] == current['key']:  # Удаление начала +
        if prev is None and current['right'] is None and current['left'] is None:
            clear()
            return current['key'], current['value']
        elif current['right'] is not None and current['left'] is None:
            root = current_node_right
        elif current['right'] is None and current['left'] is not None:
            root = current_node_left
        else:
            while current_node_right['left'] is not None:
                current_node_right = current_node_right['left']
            root = current_node_right
            root['right'] = current['right']
            root['left'] = current['left']
            return current['key'], current['value']
    elif current['left'] is None and current['right'] is None: # Удаление листа +
        if prev['key'] > current['key']:
            prev['left'] = None
            return current['key'], current['value']
        elif prev['key'] < current['key']:
            prev['right'] = None
            return current['key'], current['value']
    elif current['left'] is not None and current['right'] is None: # удаление односторонней левой ветки +
        prev['left'] = current['left']
        return current['key'], current['value']
    elif current['right'] is not None and current['left'] is None: # удаление односторонней правой ветки +
        prev['right'] = current['right']
        return current['key'], current['value']
    elif current['right'] is not None and current['left'] is not None: # Удаление узла с потомками с обоих сторон
        if root['key'] < current['key']:  # Удаление справа
            if current['left']['right'] is not None:
                while current_node_left['right'] is not None:
                    prev_node_left = current_node_left
                    current_node_left = current_node_left['right']
                if prev['key'] != root['key']:
                    prev['right'] = current_node_left
                    current_node_left['right'] = current['right']
                    current_node_left['left'] = current['left']
                    prev_node_left['right'] = None
                    return current['key'], current['value']
                else:
                    prev['right'] = current_node_left
                    current_node_left['right'] = current['right']
                    current_node_left['left'] = current['left']
                    prev_node_left['right'] = None
                    return current['key'], current['value']
            else:                                               # удаление среднего звена в ветке
                prev['left'] = current['right']
                current['right']['left'] = current['left']
                return current['key'], current['value']
        if root['key'] > current['key']:  # Удаление слева
            if current['right']['left'] is not None:
                while current_node_right['left'] is not None:
                    prev_node_right = current_node_right
                    current_node_right = current_node_right['left']
                if prev['key'] != root['key']:
                    prev['left'] = current_node_right
                    current_node_right['left'] = current['left']
                    current_node_right['right'] = current['right']
                    prev_node_right['left'] = None
                    return current['key'], current['value']
                else:
                    prev['left'] = current_node_right
                    current_node_right['left'] = current['left']
                    current_node_right['right'] = current['right']
                    prev_node_right['left'] = None
                    return current['key'], current['value']
            else:                                                   # удаление среднего звена в ветке
                prev['right'] = current['left']
                current['left']['right'] = current['right']
                return current['key'], current['value']


def find(key: int) -> Optional[Any]:
    """
    Find value by given key in the BST

    :param key: key for search in the BST
    :return: value associated with the corresponding key
    """
    _, current = _find(key)
    if current is None:
        raise KeyError
    return current['value']


def clear() -> None:
    """
    Clear the tree

    :return: None
    """
    global root
    root = None


def main():
    clear()
    """Просто дерево"""
    insert(15, 'это 15')
    insert(10, 'это 10')
    insert(12, 'это 12')
    insert(13, 'это 13')
    insert(14, 'это 14')
    insert(11, 'это 11')
    insert(5, 'это 5')
    insert(7, 'это 7')
    insert(3, 'это 3')
    insert(20, 'это 20')
    insert(25, 'это 25')
    insert(23, 'это 23')
    insert(24, 'это 24')
    insert(22, 'это 22')
    insert(30, 'это 30')
    insert(18, 'это 18')
    insert(19, 'это 19')
    insert(17, 'это 17')
    insert(16, 'это 16')
    insert(2, 'это 2')
    insert(1, 'это 1')
    insert(8, 'это 8')
    insert(6, 'это 6')
    print(root)
    print(remove(24))
    print(root)
    clear()
    """Дерево корень"""
    print(root)
    insert(15, 'это 15')
    print(remove(15))
    clear()
    """Дерево в одну сторону направо"""
    insert(1, 'это 1')
    insert(2, 'это 2')
    insert(3, 'это 3')
    insert(4, 'это 4')
    insert(5, 'это 5')
    insert(6, 'это 6')
    print(root)
    print(remove(1))
    print(root)
    clear()
    """Дерево в одну сторону налево"""
    insert(6, 'это 6')
    insert(5, 'это 5')
    insert(4, 'это 4')
    insert(3, 'это 3')
    insert(2, 'это 2')
    insert(1, 'это 1')
    print(root)
    print(remove(6))
    print(root)
    clear()


if __name__ == '__main__':
    main()
