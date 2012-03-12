#!/usr/bin/env python

import subprocess

class Module(object):
    def __init__(self, name):
        self._name = name
        self._filename = None
        # p = subprocess.Popen([self._filename, "detail"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        # self._detail = p.communicate()[0]

    # modulre name
    @property
    def name(self):
        return self._name

    # Some kind of description of the module
    @property
    def detail(self):
        return self._detail

    # Filename of the module binary/script
    @property
    def filename(self):
        return self._filename

    # The scheduler will call this and will pass attributes from a Task instance
    def run_task(taskname, params):
        subprocess.Popen([self._filename, taskname, params], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        return p.communicate()[0]

# Manages a collection of modules, used by hub and remote
class ModuleManager(object):
    def __init__(self):
        pass

    def getbyname(name):
        pass

    def exists(name):
        pass

    def install():
        pass

    def uninstall()
        pass
