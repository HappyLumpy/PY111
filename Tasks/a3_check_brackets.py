def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    count_brackets = 0

    for brackets in brackets_row:
        if brackets == '(' and count_brackets != -1:
            count_brackets += 1
        if brackets == ')':
            count_brackets -= 1
        if count_brackets == -1:
            break
    if count_brackets == 0:
        return True
    else:
        return False
