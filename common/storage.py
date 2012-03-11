#!/usr/bin/env python

# Really need to think this thru. Need a storage model
# that can be backed via file, db, network even?
class Storage(object):
    def __init__(self, domain):
        self._domain = domain
        pass

    def get(self, key):
        pass

    def put(self, key, value):
        pass

    def keys():
        pass

class LocalStorage(Storage):
    passs

class DBStorage(Storage):
    passs
