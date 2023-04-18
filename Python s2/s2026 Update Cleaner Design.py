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


def edit_record(tree):
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

data_list = [("Japanese Empire", "N@zi Germany", "USA"), ("N@zi Germany", "Finland", "Soviet Union"), ("Fascist Italy", "N@zi Germany", "Greece"), ("Finland", "N@zi Germany", "Soviet Union"), ("British Empire", "USA", "N@zi Germany"), ("France", "British Empire", "N@zi Germany"), ("Vishy France", "N@zi Germany", "British Empire"), ("USA", "British Empire", "Japanese Empire"), ("Soviet Union", "USA", "N@zi Germany"), ("Republic of China", "British Empire", "Japanese Empire"), ("Polish Republic", "Japanese Empire", "N@zi Germany")]

root = tk.Tk()
root.title('🚥 S2026 GUI - 🖥 ▁ ▂ ▄ ▅ ▆ ▇ █彡２.１彡█ ▇ ▆ ▅ ▄ ▂ ▁̲')
root.geometry("700x600")

Ramme = tk.LabelFrame(root, text="Main Område ", background="#F5F5F5")
Ramme.grid(row=0, column=0, ipadx=90, padx=padx, pady=pady, sticky=tk.N)

Ramme2 = tk.LabelFrame(root, text="Lande WW2", background="#F5F5F5")
Ramme2.grid(row=1, column=0, pady=10, padx=20, sticky=tk.N)

entry = tk.Entry(Ramme, justify="center", width=40, highlightthickness=1, highlightbackground="#C5C5C5", border=0, background="#F6F6F6")
entry.grid(row=1, column=2, padx=padx, pady=pady)
entry.insert(0, "Tryk på knappen 'Kill' for at fjerne teksten")

label = tk.Label(Ramme, text="✖ Prøv at fjerne teksten")
label.grid(row=2, column=3, padx=padx, pady=pady)

knap = tk.Button(root, text=" 🥹 Kill 🥹 ", activebackground="red", command=clean, highlightthickness=5, border=0, background="#E0EBF9", highlightbackground="#C5C5C5")
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

tree1.bind("<ButtonRelease-1>", lambda event: edit_record(tree1))

tree1.tag_configure('oddrow', background=oddrow)
tree1.tag_configure('evenrow', background=evenrow)

read_data(tree1)

if __name__ == '__main__':
    root.mainloop()
