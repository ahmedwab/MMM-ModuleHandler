# Magic Mirror Module Control

import addModule as am
import deleteModule as dm



while True:
    print("Select an option: \n")
    print(" Add")
    print(" Remove")
    print (" Quit \n")
    command = input()

    if command == 'Add':
        moduleName = input("Enter module name: ")
        print ("Adding Module " + moduleName)
        am.addModule(moduleName)
        print (moduleName + "Added")
        print ("---------------------------")

    elif command == 'Remove':
        moduleName = input("Enter module name: ")
        dm.deleteModule(moduleName)
        print ("Removed Module " + moduleName)
        print ("---------------------------")

    elif command == 'Quit':
        print ("Quitting \n---------------------------")
        exit(0)
    
    else:
        print ("Invalid option")
        print ("---------------------------")
    
    
    


