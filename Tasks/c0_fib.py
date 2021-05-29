def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    if n in (0, 1):
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """

    if n < 0:
        raise ValueError
    f1 = 1
    f2 = 1
    i = 0
    for i in range(n-2):
        f1, f2 = f2, f2 + f1
    return f2


if __name__ == '__main__':
    print(fib_iterative(10))
    print(fib_recursive(10))
