import subprocess
import os
import getModule as gm





def obtainModule(moduleName):
    return gm.findModule(moduleName)



def git(filename):
    subprocess.call(["git", "clone",filename])

def addModule(filename):
    cloneLink = obtainModule(filename)
    git(cloneLink)
    subprocess.call(["mv", filename,"../modules"])
    path = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
    path = path +"/modules/"+filename
    shellCommand = "cd "+ path + " &&" + " npm install"
    subprocess.call(shellCommand, shell=True)
    shellCommand = "node changeConfig.js add "+filename
    subprocess.call(shellCommand, shell=True)

    

    
   





