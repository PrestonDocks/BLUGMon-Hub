#!/usr/bin/env python

class Task(object):
    def __init__(self):
        pass

    @property
    def identifier(self):
        return self._identifier

    # An instance of module 
    @property
    def module(self):
        return self._module

    # Taskname to be passed on the cli to the module binary/script
    @property
    def taskname(self):
        return self._tasknname

    # Array of params to be passed on the cli to the module binary/script
    @property
    def params(self):
        return self._params

    # Used by the scheduler to determine how often to run the task
    @property
    def schedule(self):
        return self._schedule

    pass

# Manages a collection of tasks, used by hub and remote
class TaskManager(object):
    def __init__(self):
        self._tasks = []

    def create(module, taskname, taskparams, tasksched):
        pass
   
    def destroy(task):
        pass

    def getby():
        pass
