#!/usr/bin/env python3
"""[Simple helper function]
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """[Function that takes two integer arguments]

    Args:
        page (int): [number that represents the index
        of the beginning of the page]
        page_size (int): [number representing the page size]

    Returns:
        Tuple: [tuple of size two containing a start
        index and an end index corresponding to the
        range of indexes to return in a list for
        those particular pagination parameters]
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
