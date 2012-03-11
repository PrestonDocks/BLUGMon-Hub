#!/usr/bin/env python

import subprocess

class Module(object):
    def __init__(self, name):
        self._name = name
        self._filename = None
        #p = subprocess.Popen([self._filename, "detail"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        #self._detail = p.communicate()[0]

    @property
    def name(self):
        return self._name

    @property
    def detail(self):
        return self._detail

    @property
    def filename(self):
        return self._filename

    def run_task(taskname, params):
        subprocess.Popen([self._filename, taskname, params], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        return p.communicate()[0]

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
