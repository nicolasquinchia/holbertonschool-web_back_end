#!/usr/bin/env python3
"""[Basic dictionary]
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):

    """[Class that inherits from BaseCaching
    and becomes a caching system]

    Args:
    BaseCaching ([Class]): [Parent class]
    """

    def put(self, key, item):
        """[Method that add an item in the cache]

        Args:
                key: [Key]
                item: [Value for the key]
        """

        if key is not None and item is not None:
            self.cache_data[key] = item

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
