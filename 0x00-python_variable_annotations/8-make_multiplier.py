#!/usr/bin/env python3
"""Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Funtion that use a callable to return
    from a function

    Args:
        multiplier (float): Number to multiply

    Returns:
        Callable[[float], float]: Function multiples
    """
    def multiplies(number: float) -> float:
        """Multiples number with multiplier
        variable from the parent function

        Args:
            number (float): Number to multiply

        Returns:
            float: Result of the mult
        """
        return number * multiplier
    return multiplies
