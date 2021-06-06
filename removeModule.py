import subprocess
import os

def removeModule(filename):
    try:
        path = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
        path = path +"/modules"
        shellCommand = "cd " + path + "  && rm -r -f " + filename
        subprocess.call(shellCommand, shell=True)
        shellCommand = "node changeConfig.js remove "+filename
        subprocess.call(shellCommand, shell=True)
        print (filename + " Removed")
        print ("---------------------------")
    except:
        print ("Error removing module")
    
    


