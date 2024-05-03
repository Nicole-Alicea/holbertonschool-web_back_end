#!/usr/bin/env python3
'''This function changes all topics of a school document'''

import pymongo


def update_topics(mongo_collection, name, topics):
    '''Will update all topics of a school document based on the name'''

    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
