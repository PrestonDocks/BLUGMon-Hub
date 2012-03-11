#Created by Simon Carr
#09/03/2012

#This file will provide management of remote servrer configuration.
#Remotes are file based objects that are stored in the remotes folder.
#They represent a physical server on the network that has BLUGMon-Remote installed.

from optparse import OptionParser
import uuid,os,datetime

class HubRemote(object):
    def __init__(self):
        self.remotesFolder = "./remotes/"
        pass
    
    def rmtcreate(self,remoteName, hostName, remoteID):
        """
        Creates a new remote configuration
        
        TODO: Check that remote name does not contain illegal characters before 
        creating. Should be Alpha Numeric only and no spaces or minuses 
        """
        self.thisRemotesPath = os.path.join(self.remotesFolder, remoteName)
        
        if self.remoteExists(remoteName):
            ErrorTitle = 'Remote %s already exists'%remoteName
            ErrorMsg = 'The Remote %s that you tried to create already exists. Use a different name.'%remoteName
            self.remoteLog((remoteName,1,ErrorTitle,ErrorMsg))
            return (1,ErrorMsg)
        else:
            try:
                #Create the folder for the remote
                os.mkdir(self.thisRemotesPath)
                #Create the config file
                f = open(os.path.join(self.thisRemotesPath, 'remote.config'),'w')
                f.write('id:' + remoteID + '\nhost:' + hostName + '\nname:' + remoteName)
                f.close()
                print "I am here"
                print os.path.join(self.thisRemotesPath,'remote.tasks')
                #Create the tasks file. This will hold a list of commands that the remote has to execute
                f = open(os.path.join(self.thisRemotesPath,'remote.tasks'),'w')
                f.close()
                print "I am here 2"
                print os.path.join(self.thisRemotesPath,'remote.tasks')
                #Create a module file. This will hold a list of modules that should be installed on the remote
                f = open(os.path.join(self.thisRemotesPath,'remote.modules'),'w').close()
                #Creates a log file for this remote.
                f = open(os.path.join(self.thisRemotesPath,'remote.log'),'w').close()
                self.remoteLog((remoteName,0,"Created Remote " + remoteName,"The remote was created successfully"))
                return None
            except:
                ErrorTitle = 'Unable to create remote'
                ErrorMsg = 'There was a problem trying to create remote config. Check you have permissions to write to the remotes folder'
                self.remoteLog((remoteName,2,ErrorTitle, ErrorMsg))
                return (1,ErrorTitle)
            
            
    def remoteExists(self,remoteName):
        """
        Check if remote exists.
        Returns True or False
        """
        if os.path.isdir(self.thisRemotesPath): 
            return True
        else:
            return False
    
    def remoteList(self):
        """
        List all the configured remotes in the remote folder.
        Allow the list to be formated in different ways. I.e. show only enabled remotes,
        show all remotes, show enabled and disabled remotes in different colours.
        
        The data should be put into a tupel object with each element being a dictionary
        The dictionary will hold the following information
        
        Remote Name
        Host Name/IP Address
        Active (True or False)
        
        As an example the Tupel will look something like this
        ( {'name':'WebServer','host':'19.168.0.200','active':True} ,  {'name':'FileServer','host':'19.168.0.201','active':True} ) 
        
        """
        pass
    
    def rmtDelete(self):
        """
        Delete a remote configuration completely. This will mean removing the high level
        folder from the remotes folder. i.e './remotes/WebServer' would have to be deleted 
        """
        pass
    
    def addModule(self):
        """
        Add a reference to a module to the remote.module file. You first need to check
        that the module exists.
        """
        pass
    
    def rmModule(self):
        """
        remove a reference to a module from the module file.
        You will also have to identify and remove any commands for this module that
        are configured in task file.
        """
        pass
    
    def lsModule(self):
        """
        List modules in the module file. These will only be references to the modules
        that the remote uses.
        """
        pass
    
    def lsTask(self):
        """
        list commands in the command file
        Provide different ways to display them. i.e. by module or by schedule
        """
        pass
    
    def addTask(self):
        """
        Add a command to the command file
        """
        pass
    
    def rmTask(self):
        """
        remove a command from the command file
        """
        pass
    
    def log(self):
        """
        Provide different for returning the log file
        e.g. Show only warnings or show all, show last 10 or show last critical
        """

    def remoteLog(self,logMessage):
        """
        Log message should be sent as a tupal with the following information
        (<remoteName str>,<verbosity int>,<logTitle str>, <logDetail str>)
        
        Verbosity should be one of:-
        0=Notice
        1=Warning
        2=Critical
        
        
        log messages are written an a Tab seperated file in the following format
        
        date \t verbosity \t title \t detail
        """
        
        #If it exists write to the specific remotes log file first
        if os.path.exists(os.path.join(self.remotesFolder,logMessage[0],'remote.log')):
            f = open(os.path.join(self.remotesFolder,logMessage[0],'remote.log'),'a')
            f.write(str(datetime.datetime.now()) + "\t" + str(logMessage[1]) + "\t" + logMessage[2] + "\t" + logMessage[3] + "\n")
            f.close()
        #Now write to the all up remotes log file
        try:
            f = open('./remotes/remotes.log','a')
            f.write(str(datetime.datetime.now()) + "\t" + str(logMessage[1]) + "\t" + logMessage[2] + "\t" + logMessage[3] + "\n")
            f.close()
            
        except IOError as (errno, strerror):
            print "I/O error({0}): {1}".format(errno, strerror)
            return "I/O error({0}): {1}".format(errno, strerror)
            
            
if __name__ == '__main__':
    hubremote = HubRemote()
    parser = OptionParser()
    parser.add_option('-a','--add',dest='addRemote',action='store_true',help='Add new remote server')
    parser.add_option('-i','--ip',dest='hostName',help='Hostname or IP Address of remote')
    parser.add_option('-n','--name',dest='remoteName',help='Friendly name of remote')
    parser.add_option('-e','--enabled',dest='remoteEnabled',default=True,help='Enable Remote on create (True or False) default = True')
    (options, args) = parser.parse_args()
    if options.addRemote:
        if not options.hostName and not options.remoteName:
            print "To add a remote you must specify a name and a host/IP address"
        else:
            remoteID = str(uuid.uuid4())
            hubremote.rmtcreate(options.remoteName, options.hostName, remoteID)
            
        

    
    
        