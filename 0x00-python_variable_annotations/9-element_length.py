#!/usr/bin/env python3
"""Iterable Object
"""
from typing import Sequence, Tuple, Iterable, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return an iterable object

    Args:
        lst (Iterable[Sequence]): Iterable obj to check

    Returns:
        List[Tuple[Sequence, int]]: List of elements iterable
    """
    return [(i, len(i)) for i in lst]
