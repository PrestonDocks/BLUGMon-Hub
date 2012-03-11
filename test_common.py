#!/usr/bin/env python

from common.client import *
from common.storage import *

if __name__ == '__main__':
    clients = ClientMananger(Storage("Hub.Clients"))
    modules = ModuleManager(Storage("Hub.Modules"))

    #Create and register new client
    newClient = Client("Hub.Clients.1")
    clients.register(newClient)

    #Create a ping task     module                     task    params         sched
    #newClient.Tasks.Create(modules.getbyname("ping"), "ping" ["google.com"], [5])
    
