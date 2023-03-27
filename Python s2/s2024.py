import tkinter as tk
from tkinter import ttk

padx = 8
pady = 4

root = tk.Tk()
root.title('Random GUI')
root.geometry("1000x500")

Ramme = tk.LabelFrame(root, text="Main Area")
Ramme.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)


def clean():
    print("🏴󠁭󠁵󠁰󠁷󠁿 Du rentgjorde teksten")
    entry.delete(0, tk.END)


entry = tk.Entry(Ramme, justify="center", width=40)
entry.grid(row=1, column=2, padx=padx, pady=pady)
entry.insert(0, "Tryk på knappen 'Kill' for at fjerne teksten")

label = tk.Label(Ramme, text="✖ Prøv at fjerne teksten")
label.grid(row=2, column=3, padx=padx, pady=pady)

knap = tk.Button(root, text=" 🥹 Kill 🥹 ", activebackground="red", command=clean)
knap.grid(row=0, column=1, padx=padx, pady=pady)

tree1scroll = tk.Scrollbar(root)
tree1scroll.grid(row=5, column=6, padx=padx, pady=pady, sticky='ns')
tree1 = ttk.Treeview(root, yscrollcommand=tree1scroll.set,
                     select="browse")
tree1.grid(row=5, column=5, padx=0, pady=pady)
tree1scroll.config(command=tree1.yview)

tree1['columns'] = ("col1", "col2", "col3")
tree1.column("#0", width=0, stretch=tk.NO)  # Suppress the annoying first empty column.
tree1.column("col1", anchor=tk.E, width=90)  # "E" stands for East, meaning Right. Possible anchors are N, NE, E, SE, S, SW, W, NW and CENTER
tree1.column("col2", anchor=tk.W, width=130)
tree1.column("col3", anchor=tk.E, width=180)

tree1.heading("#0", text="", anchor=tk.W)
tree1.heading("col1", text="1. Liste", anchor=tk.CENTER)
tree1.heading("col2", text="2. Liste", anchor=tk.CENTER)
tree1.heading("col3", text="3. Liste", anchor=tk.CENTER)


if __name__ == '__main__':
    root.mainloop()
