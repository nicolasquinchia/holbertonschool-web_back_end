#!/usr/bin/env python3
"""Complex types - string
and int/float to tuple
"""
from typing import Union, Tuple
Num = Union[int, float]


def to_kv(k: str, v: Num) -> Tuple[str, float]:
    """ Complex typing t process
    a square of a float variable

    Args:
        k (str): String to add to the tuple
        v (Num): Float or integer to square

    Returns:
        Tuple[str, float]: String and square of the arg
    """
    return (k, v ** 2)
