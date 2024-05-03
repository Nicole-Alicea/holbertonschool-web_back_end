#!/usr/bin/env python3
'''This function will list all documents in a collection'''


def list_all(mongo_collection):
    '''Will return a list of all documents in a collection.
    If there are no documents, it will return an empty list'''

    all_documents = []
    empty_list = []

    for document in mongo_collection:
        all_documents.append(document)

        return all_documents
    
    else:
        return empty_list
