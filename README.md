# Python base module

## Information

The `base.rebase` function provided by this package can be used to convert
numbers between arbitrary bases.

## Examples

    >>> import base
    >>> base.rebase('80', base.HEX, base.DECIMAL)
    '128'
    >>> base.rebase(-255, base.DECIMAL, base.HEX)
    '-FF'
    >>> base.rebase('1111', base.BINARY, base.DECIMAL)
    '15'

## MIT license

This project is licensed under an [MIT license][].

Copyright © 2011 Andreas Blixt (<andreas@blixt.org>)

[MIT license]: http://www.opensource.org/licenses/mit-license.php
