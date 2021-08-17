#!/usr/bin/env python3
"""[MRU Caching]
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """[Class that inherits from BaseCaching
    and becomes a caching system]

    Args:
        BaseCaching ([Class]): [Parent class]
    """

    def __init__(self):
        """[Constructor]
        """
        super().__init__()
        self.key_list = []

    def put(self, key, item):
        """[Method that assign to the dictionary
        the item value for the key, discard the
        most recently used item (MRU algorithm)]

        Args:
                key: [Key]
                item: [Value for the key]
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.key_list.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            recent_used_key = self.key_list.pop(-2)
            print('DISCARD:', recent_used_key)
            del self.cache_data[recent_used_key]

    def get(self, key):
        """[Method that Get an item by key]

        Args:
                key: [Key]
                Returns: [Value in dictionay linked to key]
        """
        if key is not None and key in self.cache_data:
            self.key_list.append(key)
            return self.cache_data[key]
        else:
            return None
