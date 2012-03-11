#!/usr/bin/env python

class Task(object):
    def __init__(self):
        pass

    @property
    def identifier(self):
        return self._identifier

    @property
    def module(self):
        return self._module

    @property
    def taskname(self):
        return self._tasknname

    @property
    def params(self):
        return self._params

    @property
    def schedule(self):
        return self._schedule

    pass

class TaskManager(object):
    def __init__(self):
        self._tasks = []

    def create(module, taskname, taskparams, tasksched):
        pass
   
    def destroy(task):
        pass

        def destroy(task):
        pass

    def getby():
        pass
