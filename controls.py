from tkinter import *
from tkinter import ttk
import addModule as am
import threading
import removeModule as rm

def addModule():
    inputValue = moduleName.get()
    if inputValue:
        thread = threading.Thread(target= am.addModule(inputValue))
        thread.start()
        addButton.config(text="Add") 
        moduleName.delete(0,END)
        addButton.config(text="Add") 
def add():
    addButton.config(text="Adding...") 
    thread = threading.Thread(target= addModule)
    thread.start()
    

def removeModule():
    inputValue = moduleName.get()
    if inputValue:
        removeButton.config(text="Removing...") 
        thread = threading.Thread(target= rm.removeModule(inputValue))
        thread.start()
        removeButton.config(text="Remove") 
        moduleName.delete(0,END)
        removeButton.config(text="Remove")
def remove():
    removeButton.config(text="Removing...") 
    thread = threading.Thread(target= removeModule)
    thread.start()


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
moduleName = Entry()
moduleName.place(x=200, y=90, anchor="center")

addButton = Button(frame ,fg = "#161d25",width = 15, height=2, text="Add", command = add)
addButton.place(x=200, y=140, anchor="center")
removeButton = Button(frame , fg = "#161d25",width = 15, height = 2, text="Remove", command = remove)
removeButton.place(x=200, y=180, anchor="center")




window.mainloop()