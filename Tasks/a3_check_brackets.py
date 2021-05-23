import re


def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    count_open_brackets = 0
    count_close_brackets = 0
    for brackets in brackets_row:
        if brackets == '(':
            count_open_brackets += 1
            if brackets == ')':
                count_close_brackets += 1
    if count_open_brackets == count_close_brackets:
        if re.fullmatch(r'\(.*\)', brackets_row) or brackets_row == "":
            return True
    else:
        return False
