#!/usr/bin/env python3
"""
Create a class LIFOCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the last item put in cache (LIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """definition of class LIFOCache
    """
    def __init__(self):
        """Initialize an instance of cache_data
        """
        super().__init__()
        self.index = 0
        self.cache_index = {}

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value for the key key.
        """
        if (key is None or item is None):
            return
        else:
            if (self.index < self.MAX_ITEMS or key in self.cache_data.keys()):
                self.cache_data[key] = item
                self.cache_index[self.index] = key
                self.index += 1
            else:
                self.cache_data[key] = item
                last_item = self.cache_index[self.MAX_ITEMS - 1]
                self.cache_index[self.MAX_ITEMS - 1] = key
                print("DISCARD: {}".format(last_item))
                del self.cache_data[last_item]

    def get(self, key):
        """return the value in self.cache_data linked to key.
        """
        try:
            return self.cache_data[key]
        except KeyError:
            return None
