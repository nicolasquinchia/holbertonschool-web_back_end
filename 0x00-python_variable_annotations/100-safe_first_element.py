#!/usr/bin/env python3
"""First element of a sequence
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """[Function with the first element of a sequence and
    return values with the appropriate types]
    Args:
        lst (Sequence[Any]): [Any sequence type]
    Returns:
        Union[Any, None]: [Derived from sequence element type]
    """
    if lst:
        return lst[0]
    else:
        return None
