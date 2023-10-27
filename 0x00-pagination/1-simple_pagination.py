import csv
import math
from typing import List, Tuple


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

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        '''
        return a tuple of size two containing a start index
        and an end index
        '''
        offset = page_size * (page - 1)
        end = offset + page_size
        return offset, end

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        Use index_range to find the correct indexes to paginate 
        the dataset correctly and return the appropriate page of the dataset
        '''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        dataset = self.dataset()
        data_len = len(dataset)
        try:
            index = self.index_range(page, page_size)
            return dataset[index[0]:index[1]]
        except IndexError:
            return []
