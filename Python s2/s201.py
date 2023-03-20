from tkinter import *

root = Tk()
root.geometry("300x100")

myLabel1 = Label(root, text="Hej")
myLabel2 = Label(root, text="Hej 2")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

root.mainloop()
