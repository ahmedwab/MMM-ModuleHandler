from tkinter import *
from tkinter import ttk
import addModule as am
import removeModule as rm

def addModule():
    inputValue = moduleName.get()
    if inputValue:
        am.addModule(inputValue)
        print (inputValue + " Added")
        print ("---------------------------")
        moduleName.delete(0,END)

def removeModule():
    inputValue = moduleName.get()
    if inputValue:
        rm.removeModule(inputValue)
        print (inputValue + " Removed")
        print ("---------------------------")
        moduleName.delete(0,END)

window = Tk()
window.title("Magic Mirror ModuleHandler")
window.geometry('400x300')
window.configure(background = "#161d25")
window.resizable(False, False)


frame = Frame(window,bg = "#161d25",width=400,height=400)
frame.grid(row=0,column=0,sticky="NW")
frame.grid_propagate(0)
frame.update()


label = Label(frame,text="Module Name:",bg="#161d25",font=("Courier", 30),fg="white")
label.place(x=200, y=30, anchor="center")
moduleName = Entry(frame)
moduleName.place(x=200, y=90, anchor="center")

addButton = Button(frame ,fg = "#161d25",bd="0", text="Add", command = addModule)
addButton.place(x=200, y=140, anchor="center")
removeButton = Button(frame , fg = "#161d25", text="Remove", command = removeModule)
removeButton.place(x=200, y=170, anchor="center")




window.mainloop()