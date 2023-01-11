from tkinter import *
from tkinter import ttk

def clear_entry_boxes():
    for entry in entry_list:
        entry.delete(0, END)

root = Tk()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

labelframe = ttk.LabelFrame(mainframe, text="Labelframe")
labelframe.grid(column=0, row=0, sticky=(N, W, E, S))

frame1 = ttk.Frame(labelframe, padding="3 3 12 12")
frame1.grid(column=0, row=0, sticky=(N, W, E, S))

tree = ttk.Treeview(frame1)
tree.grid(column=0, row=0, sticky=(N, W, E, S))

scrollbar = ttk.Scrollbar(frame1, orient=VERTICAL, command=tree.yview)
scrollbar.grid(column=1, row=0, sticky=(N, W, E, S))

frame2 = ttk.Frame(labelframe, padding="3 3 12 12")
frame2.grid(column=0, row=1, sticky=(N, W, E, S))

label1 = ttk.Label(frame2, text="Label 1")
label1.grid(column=0, row=0, sticky=(N, W, E, S))

entry1 = ttk.Entry(frame2)
entry1.grid(column=1, row=0, sticky=(N, W, E, S))

label2 = ttk.Label(frame2, text="Label 2")
label2.grid(column=0, row=1, sticky=(N, W, E, S))

entry2 = ttk.Entry(frame2)
entry2.grid(column=1, row=1, sticky=(N, W, E, S))

label3 = ttk.Label(frame2, text="Label 3")
label3.grid(column=0, row=2, sticky=(N, W, E, S))

entry3 = ttk.Entry(frame2)
entry3.grid(column=1, row=2, sticky=(N, W, E, S))

frame3 = ttk.Frame(labelframe, padding="3 3 12 12")
frame3.grid(column=0, row=2, sticky=(N, W, E, S))

button1 = ttk.Button(frame3, text="Button 1")
button1.grid(column=0, row=0, sticky=(N, W, E, S))

button2 = ttk.Button(frame3, text="Button 2")
button2.grid(column=1, row=0, sticky=(N, W, E, S))

button3 = ttk.Button(frame3, text="Button 3")
button3.grid(column=2, row=0, sticky=(N, W, E, S))

button4 = ttk.Button(frame3, text="Button 4")
button4.grid(column=3, row=0, sticky=(N, W, E, S))

button5 = ttk.Button(frame3, text="Button 5")
button5.grid(column=4, row=0, sticky=(N, W, E, S))

button6 = ttk.Button(frame3, text="Button 6")
button6.grid(column=5, row=0, sticky=(N, W, E, S))

button7 = ttk.Button(frame3, text="Button 7")
button7.grid(column=6, row=0, sticky=(N, W, E, S))

button8 = ttk.Button(frame3, text="Button 8")
button8.grid(column=7, row=0, sticky=(N, W, E, S))

button9 = ttk.Button(frame3, text="Button 9")