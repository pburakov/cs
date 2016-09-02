def base(I, b):
    """
    Base converter.

    Converts decimal number into base representation of 2 through 16.

    :param int I: Decimal integer
    :param int b: Radix base
    :return str: Binary string
    """
    if not 1 < b <= 16:
        raise ValueError("Unable to convert to base {}".format(b))
    if I > 0:
        rem = I % b
        return base(I // b, b) + CHARS[rem]
    else:
        return ''


"""
Constants used in this module
"""
CHARS = "0123456789abcdef"
