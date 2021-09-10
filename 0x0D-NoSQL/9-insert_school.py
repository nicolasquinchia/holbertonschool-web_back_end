#!/usr/bin/env python3
""" Module that holds insert a document
"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """ Method that inserts a new document in a
        collection based on kwargs
    """
    new_document = mongo_collection.insert(kwargs)
    return new_document
