#!/usr/bin/env python3
"""[FIFO caching]
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
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
        last item put in cache (LIFO algorithm)]

        Args:
                key: [Key]
                item: [Value for the key]
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data)[-2]
            print('DISCARD:', last_key)
            self.cache_data.pop(last_key)

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
