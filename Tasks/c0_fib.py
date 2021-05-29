def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n >= 0:
        if n in (0, 1):
            return n
        return fib_recursive(n - 1) + fib_recursive(n - 2)
    else:
        raise ValueError


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n >= 0:
        f1 = 1
        f2 = 1
        i = 0
        f_sum = 0
        while i < n - 2:
            f_sum = f1 + f2
            f1 = f2
            f2 = f_sum
            i = i + 1
        return f_sum
    else:
        raise ValueError


if __name__ == '__main__':
    print(fib_iterative(-50))
    print(fib_recursive(-5))
