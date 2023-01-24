#!/usr/bin/env python3
"""
Python function list_all that has an argument
mongo_collection
"""


def list_all(mongo_collection):
    """Python function that lists all documents in a collection"""
    if mongo_collection.find() is not None:
        return (mongo_collection.find())
    else:
        return []
