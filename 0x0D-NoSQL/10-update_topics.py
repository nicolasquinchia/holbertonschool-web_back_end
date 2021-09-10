#!/usr/bin/env python3
""" Module that holds change school topics
"""

import pymongo


def update_topics(mongo_collection, name, topics):
    """ Method that changes all topics of a
        school document based on the name
    """
    new_topics = mongo_collection.update_many(
        {"name": name},
        {"$set":
         {"topics": topics}})
    return new_topics
