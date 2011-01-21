# -*- coding: utf-8 -*-
# base - convert numbers between arbitrary bases.
# Copyright © 2011 Andreas Blixt
# MIT license

"""A module for converting between bases.

"""

BASE2 = BINARY = '01'
BASE8 = OCTAL = '01234567'
BASE10 = DECIMAL = '0123456789'
BASE16 = HEX = '0123456789ABCDEF'
BASE62 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
BASE64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def rebase(number, from_base, to_base):
    """Changes the base of a number. Takes the base to convert from and the
    base to convert to. A base is defined as a string of digits that make up
    the base.

    Examples:
    >>> rebase('80', HEX, DECIMAL)
    '128'
    >>> rebase(-255, DECIMAL, HEX)
    '-FF'
    >>> rebase('1111', BINARY, DECIMAL)
    '15'

    """
    # Assumes that numbers can be negative, and that they are so when they
    # start with the dash character.
    number = str(number)
    if number[0] == '-':
        number = number[1:]
        negative = True
    else:
        negative = False

    # Get the radii (number of possible digits) of the bases.
    from_radix = len(from_base)
    to_radix = len(to_base)

    # Convert the input number to a normal integer so that arithmetics can be
    # performed.
    x = 0
    for digit in number:
        x = x * from_radix + from_base.index(digit)

    # Build the final string that will be the number in the target base.
    result = ''
    while x:
        result = to_base[x % to_radix] + result
        x //= to_radix

    # Return the result. If the input was negative, also return the result as
    # negative.
    return '-' + result if negative else result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
