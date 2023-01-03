def main(a, b, c):
    """
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    ans = 0
    if a > 0:
        ans += 1
    if b > 0:
        ans += 1
    if b > 0:
        ans += 1
    return ans


print(main(-2, 4, 3))
