#Created by Simon Carr
#09/03/2012

#This file will provide management of remote servrer configuration.
#Remotes are file based objects that are stored in the remotes folder.
#They represent a physical server on the network that has BLUGMon-Remote installed.

from optparse import OptionParser
import uuid,os

class HubRemote(object):
    def __init__(self):
        pass
    
    def rmtcreate(self,remoteName, hostName, remoteID):
        """
        Creates a new remote configuration
        
        TODO: Check that remote name does not contain illegal characters before 
        creating. Should be Alpha Numeric only and no spaces or minuses 
        """
        
        if os.path.isdir('./remotes/' + remoteName):
            ErrorMsg = 'Remote %s already exists'%remoteName
            return (1,ErrorMsg)
        else:
            os.mkdir('./remotes/' + remoteName)
            f = open('./remotes/' + remoteName + '/remote.config','w')
            f.write('id:' + remoteID + '\nhost:' + hostName + '\nname:' + remoteName)
            f.close
            return None
    
    def rmtlist(self):
        pass
    
    def rmtdelete(self):
        pass
    
    def addModule(self):
        pass
    
    def rmModule(self):
        pass
    
    def lsmodule(self):
        pass
    
    def lscmd(self):
        pass
    
    def addcmd(self):
        pass
    
    def rmcmd(self):
        pass




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
            
        

    
    
        