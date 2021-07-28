#!/usr/bin/env python3
"""Complex types - mixed List
"""
from typing import List, Union
Num = Union[int, float]


def sum_mixed_list(mxd_lst: List[Num]) -> float:
    """Sum all items in a List

    Args:
        mxd_lst (List[Num]): List of integers and floats to sum

    Returns:
        float: Sum of all nums in the list
    """
    return sum(mxd_lst)
