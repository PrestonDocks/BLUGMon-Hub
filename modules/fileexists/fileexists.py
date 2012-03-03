'''
Created on 19 Feb 2012

@author: simon
'''
import sys
import os
import threading

class moduleMain( threading.Thread ):
    
    def run( self, parameter=None ):
        """
        fileexists module

	pass in a file name and path as the first paramater
	The module returns true if the file exists and false if it does not
        """
        self.argument = sys.argv[1]
        if os.path.exists(parameter):
            return {'status': True, 'message': "The file exists"}
        else:
            return {'status': False, 'message': "The file does not exist"}

    