def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.

    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    old = a
    a1 = a//10
    a2 = a % 10
    new = a2*10+a1
    if new <= old:
        return True
    else:
        return False


print(main(37))
print(main(53))
