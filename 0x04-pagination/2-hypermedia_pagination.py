#!/usr/bin/env python3
"""[Hypermedia pagination]
"""

import csv
import math
from typing import List, Tuple, Dict


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """[Method that takes two integer arguments]

        Args:
        page (int): [number that represents the index
        of the beginning of the page]. Defaults to 1.
        page_size (int): [number representing the page size]. Defaults to 10.

        Returns:
        List[List]: [rows between the indicated indices]
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        if page > len(self.dataset()) and page_size > len(self.dataset()):
            return []
        tuple_result = index_range(page, page_size)
        return self.__dataset[tuple_result[0]: tuple_result[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """[method that takes the same arguments
        (and defaults) as get_page]

        Args:
        page (int): [number that represents the index
        of the beginning of the page]. Defaults to 1.
        page_size (int): [number representing the page size]. Defaults to 10.

        Returns:
            Dict: [dictionary containing specific key-value pairs]
        """
        page_num = self.get_page(page, page_size)
        total_page = math.ceil(len(self.dataset()) / page_size)
        if page <= 1:
            prev_page = None
        else:
            prev_page = page - 1
        if page >= total_page:
            next_page = None
        else:
            next_page = page + 1
        new_dict = {
            'page_size': len(page_num),
            'page': page,
            'data': page_num,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_page,
        }
        return new_dict
