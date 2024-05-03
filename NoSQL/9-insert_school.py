#!/usr/bin/env python3
'''This function inserts a new document'''

import pymongo


def insert_school(mongo_collection, **kwargs):
    '''Will insert a new document in a collection based on kwargs'''

    inserted_document = mongo_collection.insert_one(kwargs)

    return (inserted_document.inserted_id)
