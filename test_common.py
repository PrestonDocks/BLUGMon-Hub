#!/usr/bin/env python

from common.client import *
from common.storage import *

if __name__ == '__main__':
    hubStorage = LocalStorage("Hub")

    clients = ClientMananger(hubStorage.domain("Clients"))
    modules = ModuleManager(hubStorage.domain("Modules"))

    #Create and register new client
    newClient = Client("New Client 1")
    clients.register(newClient)

    #Create a ping task     module                     task    params         sched
    #newClient.Tasks.Create(modules.getbyname("ping"), "ping" ["google.com"], [5])
    
