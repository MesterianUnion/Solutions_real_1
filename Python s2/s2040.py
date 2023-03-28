import tkinter as tk
from tkinter import ttk

padx = 8
pady = 4
rowhi = 24
tree_backgroundcolor = "#FF0000"
tree_color = "#000000"
tree_select = "#EEEEEE"
oddrow = "#CCCCCC"
evenrow = "#DDDDDD"


def clean():
    print("🏴󠁭󠁵󠁰󠁷󠁿 Du rentgjorde teksten")
    entry.delete(0, tk.END)


def get():
    print(entry.get())
    print(entry2.get())
    print(entry3.get())
    print(entry4.get())


def read_data(tree):
    count = 0
    for record in data_list:
        if count % 2 == 0:
            tree.insert(parent='', index='end', text='', values=record, tags=('evenrow',))
        else:
            tree.insert(parent='', index='end', text='', values=record, tags=('oddrow',))
        count += 1


def edit_record(event, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, 'values')
    entry.delete(0, tk.END)
    entry.insert(1, values[0])
    entry2.delete(0, tk.END)
    entry2.insert(0, values[1])
    entry4.delete(0, tk.END)
    entry4.insert(0, values[2])


data_list = []
data_list.append(("1", "1000", "Oslo"))
data_list.append(("2", "2000", "Chicago"))
data_list.append(("3", "3000", "Milano"))
data_list.append(("4", "4000", "Amsterdam"))
data_list.append(('5', "25000", "Lorte Korsør"))

root = tk.Tk()
root.title('S2008 GUI')
root.geometry("600x500")

Ramme_grid = tk.LabelFrame(root, text="Container")
Ramme_grid.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

Ramme = tk.Frame(Ramme_grid)
Ramme.grid(row=0, column=0, padx=20)

Ramme_bund = tk.Frame(Ramme_grid)
Ramme_bund.grid(row=1, column=0)

lec = tk.Frame(Ramme_bund)
lec.grid(row=0, column=0, padx=padx, pady=pady)

label = tk.Label(lec, text="ID")
label.grid(row=0, column=1, pady=1, ipady=5)

label2 = tk.Label(lec, text="Vægt")
label2.grid(row=0, column=2)

label3 = tk.Label(lec, text="Destination")
label3.grid(row=0, column=3)

label4 = tk.Label(lec, text="Vejret")
label4.grid(row=0, column=4)

style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background=tree_backgroundcolor, foreground=tree_color, rowhi=rowhi, fieldbackground=tree_select)
style.map('Treeview', background=[('selected', tree_select)])

tree1scroll = tk.Scrollbar(Ramme)
tree1scroll.grid(row=5, column=6, padx=padx, pady=pady, sticky='ns')
tree1 = ttk.Treeview(Ramme, yscrollcommand=tree1scroll.set, selectmode="browse")
tree1.grid(row=5, column=5, padx=0, pady=pady)
tree1scroll.config(command=tree1.yview)

tree1['column'] = ("col1", "col2", "col3")
tree1.column("#0", width=0, stretch=tk.NO)
tree1.column("col1", anchor=tk.E, width=30)
tree1.column("col2", anchor=tk.E, width=80)
tree1.column("col3", anchor=tk.W, width=200)

tree1.heading("#0", text="", anchor=tk.W)
tree1.heading("col1", text="ID", anchor=tk.CENTER)
tree1.heading("col2", text="Vægt", anchor=tk.CENTER)
tree1.heading("col3", text="Destination", anchor=tk.CENTER)

tree1.bind("<ButtonRelease-1>", lambda event: edit_record(event, tree1))

tree1.tag_configure('oddrow', background=oddrow)
tree1.tag_configure('evenrow', background=evenrow)

read_data(tree1)


def clean():
    print("🏴󠁭󠁵󠁰󠁷󠁿 Du rentgjorde teksten")
    entry.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)


entry = tk.Entry(lec, width=4, justify="left")
entry.grid(row=1, column=1, padx=padx, pady=pady)

entry2 = tk.Entry(lec, width=8, justify="left")
entry2.grid(row=1, column=2, padx=padx, pady=pady)

entry3 = tk.Entry(lec, width=20, justify="left")
entry3.grid(row=1, column=3, padx=padx, pady=pady)

entry4 = tk.Entry(lec, width=14, justify="left")
entry4.grid(row=1, column=4, padx=padx, pady=pady)

krc = tk.Frame(Ramme_bund)
krc.grid(row=1, column=0, padx=padx, pady=pady)
knap = tk.Button(krc, text="  Lav  ", command=get)
knap.grid(row=2, column=1, pady=10, padx=10)


def update():
    print("🚩 Du opdateret programmet")
    knap2.quit()


knap2 = tk.Button(krc, text="Opdater", command=update)
knap2.grid(row=2, column=2, pady=10, padx=10)

knap3 = tk.Button(krc, text="   Slet   ")
knap3.grid(row=2, column=3, pady=10, padx=10)

knap4 = tk.Button(krc, text="   Slet alt   ", command=clean)
knap4.grid(row=2, column=4, pady=10,  padx=10)



if __name__ == '__main__':
    root.mainloop()