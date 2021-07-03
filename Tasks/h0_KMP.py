from typing import Optional, List


def substr(some_str):
    sub_str = []
    for i in range(2, len(some_str) + 1):
        sub_str.append(some_str[:i])
    return sub_str


def list_pref(sub_str):
    _pref = []
    for i in range(1, len(sub_str)):
        _pref.append(sub_str[:i])
    return _pref


def list_suf(sub_str):
    _suf = []
    for i in range(1, len(sub_str)):
        _suf.append(sub_str[-i:])
    return _suf


def _prefix_fun(prefix_str: str) -> List[int]:
    """
    Prefix function for KMP

    :param prefix_str: dubstring for prefix function
    :return: prefix values table
    """

    sub_str = substr(prefix_str)
    prefix_list = [0]
    for i in sub_str:
        max_lenght = 0
        pref = list_pref(i)
        suf = list_suf(i)
        for prefix, suffix in zip(pref, suf):
            if prefix == suffix:
                max_lenght = len(prefix)
        prefix_list.append(max_lenght)
    return prefix_list


def kmp_algo(inp_string: str, substr: str) -> Optional[int]:
    """
    Implementation of Knuth-Morrison-Pratt algorithm

    :param inp_string: String where substr is to be found (haystack)
    :param substr: substr to be found in inp_string (needle)
    :return: index where first occurrence of substr in inp_string started or None if not found
    """
    i = 0
    j = 0
    pref = _prefix_fun(substr)

    while i < len(inp_string):
        if inp_string[i] == substr[j]:
            i += 1
            j += 1
            if j == len(substr):
                return i - len(substr)
        elif j == 0:
            i += 1
        else:
            j = pref[j - 1]


def main():
    some_str = 'abcabcsabcd'
    subst = 'abcabcd'
    print(kmp_algo(some_str, subst))


if __name__ == '__main__':
    main()
