#!/usr/bin/env python3
"""
a python function insert_school that has two arguments
mongo_collection and **kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
       Python function that inserts a new document
       in a collection based on kwargs
    """
    res = mongo_collection.insert_one(kwargs)
    return res
