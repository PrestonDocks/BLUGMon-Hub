#!/usr/bin/env python

class Client(object):
    def __init__(self, identifier):
        self._storage = storage
        self._tasks = TaskManager(self._storage)
        self._modules = ModuleManager(self._storage)

    @property
    def name(self):
        return self._name

    # Readonly?
    @property
    def identifier(self):
        return self._identifier

    @property
    def last_update(self):
        return self._last_update
    
    @property
    def tasks(self):
        return self._tasks

    @property
    def modules(self):
        return self._modules

class ClientManager():
    def __init__():
        self._clients = []
        pass

    # Generate new indentifier and store client attributes. Return success or fail. 
    # Populate client identifier somehow, readonly identfier?
    def register(client):
        pass

    def unregister(indentifier):
        pass

    # Return a refernece to a client instance with the coresponding identifier.
    def getbyid(indentifier):
        pass

    pass




