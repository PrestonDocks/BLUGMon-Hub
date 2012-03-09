#!/usr/bin/env python
#Written by Simon Carr
#4 March 2012
from optparse import OptionParser
import sys, os, shutil, tarfile
import uuid,csv



class ManageModules(object):
    def __init__(self):
        pass
    
    def listModules(self, printList=True):
        moduleList = [x for x in os.listdir("./modules") if os.path.isdir(os.path.join("./modules",x))]
        if printList:
            for module in moduleList:
                print module
        else:
            return moduleList
            
            
    def unInstallModule(self,moduleName):
        if self.moduleExists(moduleName):
            shutil.rmtree(os.path.join("./modules",moduleName), False)
        else:
            raise ModuleDoesNotExist(moduleName)
    
    def installModule(self,archivePath):
        if not os.path.exists(archivePath):
            raise ModuleArchiveNonExistent(archivePath)
        else:
            tar = tarfile.open(archivePath,"r:gz")
            tar.extractall("./modules")
            moduleName = os.path.basename(archivePath)[:-7]
            if not self.moduleExists(moduleName):
                raise ModuleInstallFailed(archivePath)
    
    def moduleDetail(self,moduleName=None,printList=True):
        moduleConfig = []
        if not moduleName:
            for module in self.listModules(False):
                config = open(os.path.join("./modules/",module,module + ".config"))
                moduleConfig.append(config.read())
                config.close()
        else:
            if not self.moduleExists(moduleName):
                return False
            config = open(os.path.join("./modules/",moduleName,moduleName + ".config"))
            moduleConfig.append(config.read())
            config.close()
        if printList:
            for config in moduleConfig:
                print config
                print "*********************"
                
        else:
            return moduleConfig
        
    def moduleExists(self,moduleName):
        return os.path.isdir(os.path.join("./modules",moduleName))

    def importModule(self,moduleName):
        runModule = None
        exec("import " + "modules." + moduleName + "." + moduleName + " as runModule")
        return runModule

    

    def createTask(self,moduleName,command):
        runModule = self.importModule(moduleName)	
        self.importModule(moduleName)
        taskCreator = runModule.createTask()
        task = getattr(taskCreator,command)()
        buildTask = []
        uniqueID = uuid.uuid4()
        print "Task with id " + str(uniqueID) + " has been created: " + task[0] + " to be run every " + task[1] + " seconds"
        buildTask.append(str(uniqueID))
        buildTask.append(moduleName)
        buildTask.append(task[1])
        buildTask.append(task[0])
        
        
class ModuleBaseException(Exception):
    def __init__(self, modulename):
        self.modulename = modulename

class ModuleDoesNotExist(ModuleBaseException):
    def __str__(self):
        return "Module '%s' does not exists." % self.modulename

class ModuleInstallFailed(ModuleBaseException):
    def __str__(self):
        return "Module '%s' could not be installed." % self.modulename

class ModuleArchiveNonExistent(ModuleBaseException):
    def __str__(self):
        return "Module archive '%s' does not exist." % self.modulename
             

if __name__ == "__main__":
    mm = ManageModules()
    parser = OptionParser()
    parser.add_option("-l","--list",action="store_true",dest="listModules")
    parser.add_option("-u","--uninstall",dest="uninstall_moduleName",help="Uninstall a module")
    parser.add_option("-i","--install",dest="install_moduleName",help="Installs a new module. By default the script will check GitHub for latest version of the module and download. To specify a gz archive use -a or --archive and give path to archive.")
    parser.add_option("-a","--archive",dest="archivePath",help="Use in conjunction with -i to specify the location of an archive file to install")
    parser.add_option("-d","--detail",dest="details_moduleName",default=None,help="Print details of specified module. If 'ALL' specified detail is printed for all installed modules")
    parser.add_option("-t","--task",dest="task_moduleName",default=None,help="Runs the task creator for the given module and command. you must also provide -c <command>. To get a list of options run hubmodules.py -d <modulename>")
    parser.add_option("-c","--command",dest="task_Command",default=None,help="Runs the module task generator for the specific command you want to run the given module")
    (options, args) = parser.parse_args()
    
    if options.listModules == True: mm.listModules()
    if options.details_moduleName:     
        if options.details_moduleName == "ALL":
            mm.moduleDetail()
        else:
            mm.moduleDetail(options.details_moduleName,True)
    if options.uninstall_moduleName: mm.unInstallModule(options.uninstall_moduleName)
    if options.install_moduleName: mm.installModule(options.install_moduleName)
    if options.task_moduleName: mm.createTask(options.task_moduleName, options.task_Command)
