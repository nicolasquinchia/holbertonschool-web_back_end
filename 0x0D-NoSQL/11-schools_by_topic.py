#!/usr/bin/env python3
""" Module that holds where can I learn python
"""

import pymongo


def schools_by_topic(mongo_collection, topic):
    """ Method that returns the list of
        school having a specific topic
    """
    specific_topic = mongo_collection.find({"topics": topic})
    return specific_topic
