#!/usr/bin/env python3
""" Complex types - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return a sum of elements
    in the list

    Args:
        input_list ([float]): Numbers to check

    Returns:
        float: Sum of all elements in the list
    """
    return sum(input_list)
