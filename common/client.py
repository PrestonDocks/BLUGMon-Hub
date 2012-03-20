#!/usr/bin/env python
from task import *
from module import *

class Client(object):
    def __init__(self, storage):
        self._storage = storage
        self._name = self._storage.get('name')
        self._identifier = self._storage.get('identifier')
        self._tasks = TaskManager(self._storage.domain("task-(\d+)"))
        self._modules = ModuleManager(self._storage.domain("modules-(\d+)"))

    @property
    def name(self):
        return self._name

    # Readonly?
    @property
    def identifier(self):
        return self._identifier

    # When did remote last speak to hub
    @property
    def last_update(self):
        return self._last_update
    
    # Instance of TaskManager for this client
    @property
    def tasks(self):
        return self._tasks

    # Instance of ModuleManager for this client
    @property
    def modules(self):
        return self._modules

class ClientManager():
    def __init__():
        self._clients = []
        pass

    # Generate new indentifier and store any client attributes. Return success or fail. 
    # Populate client identifier somehow, readonly identfier?
    def register(client):
        # identifier = generate_blah()
        Client(self._storage.domain("client-%s" % identifier))
        pass

    def unregister(indentifier):
        # check existence first
        pass

    # Return a refernece to a client instance with the coresponding identifier.
    def getbyid(identifier):
        # check existence first
        return Client(self._storage.domain("client-%s" % identifier))

    pass




