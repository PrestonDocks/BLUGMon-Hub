#!/usr/bin/env python

# Really need to think this thru. Need a storage model
# that can be backed via file, db, network even?
class Storage(object):
    def __init__(self, domain):
        # case insensitive
        self._domain = [domain]
        pass

    # Returns a new storage class whose domain is composed of the parent
    # storage domain and the name passed in here
    def domain(name):
        return Storage(self._domain.add(name))

    def get(self, key):
        return self._read(domain, key)

    def put(self, key, value):
        return self._write(domain, key, value)
    
    # Returns all the keys in the current domain
    def keys():
        self._readkeys(domain)

    # Returns a list of all the domains that contain domain 
    def domains(domain=None)
        pass

class FileStorage(Storage):
    # Maps storage domains to conf files
    # i.e. domain [hub, client-007, tasks] would map to client-007/tasks.conf
    # also domain is commutative as in [a, b] is the same as [b, a]

    # hashtable ?
    map = [ { "client-%s/tasks.conf" : ["hub", "client-(\d+)", "task-(\d+)"] },
            { "client-%s/modules.conf" : ["hub", "client-(\d+)", "module-(\d+)"] } ]

    # Write tp file determined by processing mappings
    def _write(self, domain, key, value):
        pass

    # Read from file determined by processing mappings
    def _read(self, domain, key):
        pass 

class DBStorage(Storage):
    # Maps storage domains to tables, columns
    # i.e. for sql, [hub, client-007, tasks] would map to 'client_tasks' table 'where client_id = 007'
    
    map = []

    def _write(self, domain, key, value):
        pass

    def _read(self, domain, key):
        pass
