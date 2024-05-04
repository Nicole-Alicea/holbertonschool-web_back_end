#!/usr/bin/env python3
'''Simple pagination'''

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''This function takes two integer arguments and returns a tuple of size
    two containing a start index and an end index corresponding to the range
    of indexes to return in a list for those particular pagination
    parameters.'''

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index


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
        '''Will return the appropriate page of the dataset based on
        pagination parameters'''

        self.dataset()

        for x in [page, page_size]:
            assert isinstance(x, int) and page > 0
        assert page_size > 0

        range_x = index_range(page, page_size)

        return self.__dataset[range_x[0]:range_x[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        '''Gets hypermedia pagination and returns a dictionary containing
        the following key-value pairs.'''

        data: int = self.get_page(page, page_size)
        totalPages: int = math.ceil(len(self.__dataset) / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if (page + 1) <= totalPages else None,
            'prev_page': page - 1 if (page - 1) > 0 else None,
            'total_pages': totalPages
        }
