#!/usr/bin/env python3
"""[FIFO caching]
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """[Class that inherits from BaseCaching
    and becomes a caching system]

    Args:
        BaseCaching ([Class]): [Parent class]
    """

    def __init__(self):
        """[Constructor]
        """
        super().__init__()

    def put(self, key, item):
        """[Method that assign to the dictionary
        the item value for the key, discard the
        first item put in cache (FIFO algorithm)]

        Args:
                key: [Key]
                item: [Value for the key]
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = list(self.cache_data)[0]
            print('DISCARD:', list(self.cache_data)[0])
            self.cache_data.pop(first_key, 0)

    def get(self, key):
        """[Method that Get an item by key]

        Args:
                key: [Key]
                Returns: [Value in dictionay linked to key]
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
