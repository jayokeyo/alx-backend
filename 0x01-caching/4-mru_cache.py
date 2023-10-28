#!/usr/bin/env python3
"""
Create a class MRUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the most recently used item (MRU algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""
BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """definition of class MRUCache
    """
    def __init__(self):
        """Initialize an instance of cache_data
        """
        super().__init__()
        self.index = 0
        self.rank = 0
        self.cache_rank = {}

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value for the key key.
        """
        if (key is None or item is None):
            return
        else:
            if (self.index < self.MAX_ITEMS or key in self.cache_data.keys()):
                self.cache_data[key] = item
                try:
                    rank = self.cache_rank[key]
                    self.cache_rank[key] = self.rank
                    self.rank += 1
                except KeyError:
                    self.cache_rank[key] = 0
                    self.rank += 1
                self.index += 1
            else:
                self.cache_data[key] = item
                self.cache_rank[key] = self.rank
                self.rank += 1
                for key, value in self.cache_rank.items():
                    if (value == self.rank - 2):
                        print("DISCARD: {}".format(key))
                        del self.cache_rank[key]
                        del self.cache_data[key]
                        break

    def get(self, key):
        """return the value in self.cache_data linked to key.
        """
        try:
            data = self.cache_data[key]
            self.cache_rank[key] = self.rank
            self.rank += 1
            return data
        except KeyError:
            return None
