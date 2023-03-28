import tkinter as tk
from tkinter import ttk


def clean():
    print("🏴󠁭󠁵󠁰󠁷󠁿 Du rentgjorde teksten")
    entry.delete(0, tk.END)
    print(entry.get())


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
    entry.insert(0, values[0])


padx = 8
pady = 4
rowhi = 24
tree_backgroundcolor = "#eeeeee"
tree_color = "black"
tree_select = "#773333"
oddrow = "#ddeedd"
evenrow = "#cce0cc"


data_list = []
data_list.append(("Japanese Empire", "N@zi Germany", "USA"))
data_list.append(("N@zi Germany", "Finland", "Soviet Union"))
data_list.append(("Fascist Italy", "N@zi Germany", "Greece"))
data_list.append(("Finland", "N@zi Germany", "Soviet Union"))
data_list.append(("British Empire", "USA", "N@zi Germany"))
data_list.append(("France", "British Empire", "N@zi Germany"))
data_list.append(("Vishy France", "N@zi Germany", "British Empire"))
data_list.append(("USA", "British Empire", "Japanese Empire"))
data_list.append(("Soviet Union", "USA", "N@zi Germany"))
data_list.append(("Republic of China", "British Empire", "Japanese Empire"))
data_list.append(("Polish Republic", "Japanese Empire", "N@zi Germany"))

root = tk.Tk()
root.title('Random GUI')
root.geometry("700x600")

Ramme = tk.LabelFrame(root, text="Main Area")
Ramme.grid(row=0, column=0, ipadx=90, padx=padx, pady=pady, sticky=tk.N)

Ramme2 = tk.LabelFrame(root, text="Countries WW2")
Ramme2.grid(row=1, column=0, pady=10, padx=20, sticky=tk.N)

entry = tk.Entry(Ramme, justify="center", width=40)
entry.grid(row=1, column=2, padx=padx, pady=pady)
entry.insert(0, "Tryk på knappen 'Kill' for at fjerne teksten")

label = tk.Label(Ramme, text="✖ Prøv at fjerne teksten")
label.grid(row=2, column=3, padx=padx, pady=pady)

knap = tk.Button(root, text=" 🥹 Kill 🥹 ", activebackground="red", command=clean)
knap.grid(row=0, column=1, padx=padx, pady=pady)

style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background=tree_backgroundcolor, foreground=tree_color, rowhi=rowhi, fieldbackground=tree_select)
style.map('Treeview', background=[('selected', tree_select)])

tree1scroll = tk.Scrollbar(Ramme2)
tree1scroll.grid(row=5, column=6, padx=padx, pady=pady, sticky='ns')
tree1 = ttk.Treeview(Ramme2, yscrollcommand=tree1scroll.set, selectmode="browse")
tree1.grid(row=5, column=5, padx=0, pady=pady)
tree1scroll.config(command=tree1.yview)

tree1['column'] = ("col1", "col2", "col3")
tree1.column("#0", width=0, stretch=tk.NO)
tree1.column("col1", anchor=tk.W, width=180)
tree1.column("col2", anchor=tk.W, width=180)
tree1.column("col3", anchor=tk.W, width=180)

tree1.heading("#0", text="", anchor=tk.W)
tree1.heading("col1", text="Countries", anchor=tk.CENTER)
tree1.heading("col2", text="Allies", anchor=tk.CENTER)
tree1.heading("col3", text="Enemies", anchor=tk.CENTER)

tree1.bind("<ButtonRelease-1>", lambda event: edit_record(event, tree1))

tree1.tag_configure('oddrow', background=oddrow)
tree1.tag_configure('evenrow', background=evenrow)

read_data(tree1)


if __name__ == '__main__':
    root.mainloop()