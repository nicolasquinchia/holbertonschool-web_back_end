#!/usr/bin/env python3
"""Type Checking
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Function with others type Annotations and
    return values with the appropriate types
    """
    zoomed_in: List = [
        item for item in list(lst)
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
