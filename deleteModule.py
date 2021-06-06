import subprocess
import os

def deleteModule(filename):
    path = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
    path = path +"/modules"
    shellCommand = "cd " + path + "  && rm -r -f " + filename
    subprocess.call(shellCommand, shell=True)
    
    


