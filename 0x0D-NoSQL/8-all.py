#!/usr/bin/env python3
""" Module that holds list all documents
"""

import pymongo


def list_all(mongo_collection):
    """ Method that lists all documents in a collection
    """
    all_documents = mongo_collection.find()
    if mongo_collection is None:
        return []
    else:
        return all_documents
