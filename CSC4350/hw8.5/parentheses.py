def parentheses_to_remove(s: str) -> int:
    """
    Given a string with some parentheses, return the smallest number of parentheses that could be removed to yield a balanced string.
    Here, "(abc())" is balanced, as is "((a(a))b)", but "abc())" is not, nor is ")(".
    """
    right = 0
    left = 0
    for char in s:
        if char == "(":
            left += 1
        elif char == ")":
            if left == 0:
                right += 1
            else:
                left -= 1

    return left + right

