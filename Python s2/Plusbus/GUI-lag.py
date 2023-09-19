import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import data_lag as dcd
import sql_data as dcsql

padx = 8
pady = 4
rowhi = 24
tree_backgroundcolor = "#FF0000"
tree_color = "#000000"
tree_select = "#BEE4D1"
oddrow = "#CCCCCC"
evenrow = "#DDDDDD"


def read_container_entries():  # Read content of entry boxes
    return entry.get(), entry2.get(), entry3.get()


def edit_container(event, tree):  # Copy selected tuple into entry boxes. Parameter event is mandatory but we don't use it.
    index_selected = tree.focus()  # Index of selected tuple
    values = tree.item(index_selected, 'values')  # Values of selected tuple
    clear_container_entries()  # Clear entry boxes
    if values:
        write_container_entries(values)


def write_container_entries(values):  # Fill entry boxes
    entry.insert(0, values[0])
    entry2.insert(0, values[1])
    entry3.insert(0, values[2])


def create_container(tree, record):  # add new tuple to database
    kunder = dcd.Kunder.convert_from_tuple(record)  # Convert tuple to Container
    dcsql.create_record(kunder)  # Update database
    clear_container_entries()  # Clear entry boxes
    refresh_treeview(tree, dcd.Kunder)  # Refresh treeview table


def clear_container_entries():  # Clear entry boxes
    entry.delete(0, tk.END)  # Delete text in entry box, beginning with the first character (0) and ending with the last character (tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)


def update_container(tree, record):  # update tuple in database
    kunder = dcd.Kunder.convert_from_tuple(record)  # Convert tuple to Container
    dcsql.update_container(kunder)  # Update database
    clear_container_entries()  # Clear entry boxes
    refresh_treeview(tree, dcd.Kunder)  # Refresh treeview table


def delete_container(tree, record):  # delete tuple in database
    kunder = dcd.Kunder.convert_from_tuple(record)  # Convert tuple to Container
    dcsql.delete_soft_container(kunder)  # Update database
    clear_container_entries()  # Clear entry boxes
    refresh_treeview(tree, dcd.Kunder)


def read_table(tree, class_):  # fill tree from database
    count = 0  # Used to keep track of odd and even rows, because these will be colored differently.
    result = dcsql.select_all(class_)  # Read all containers from database
    for record in result:
        if record.valid():  # this condition excludes soft deleted records from being shown in the data table
            if count % 2 == 0:  # even
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('evenrow',))  # Insert one row into the data table
            else:  # odd
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('oddrow',))  # Insert one row into the data table
            count += 1


def refresh_treeview(tree, class_):  # Refresh treeview table
    empty_treeview(tree)  # Clear treeview table
    read_table(tree, class_)


def empty_treeview(tree):  # Clear treeview table
    tree.delete(*tree.get_children())


# Rejser


def rejser_read_container_entries():  # Read content of entry boxes
    return entry.get(), entry2.get(), entry3.get(), entry4.get()


def rejser_edit_container(event, tree):  # Copy selected tuple into entry boxes. Parameter event is mandatory but we don't use it.
    index_selected = tree.focus()  # Index of selected tuple
    values = tree.item(index_selected, 'values')  # Values of selected tuple
    rejser_clear_container_entries()  # Clear entry boxes
    if values:
        rejser_write_container_entries(values)


def rejser_write_container_entries(values):  # Fill entry boxes
    entry.insert(0, values[0])
    entry2.insert(0, values[1])
    entry3.insert(0, values[2])
    entry4.insert(0, values[3])


def rejser_create_container(tree, record):  # add new tuple to database
    rejser = dcd.Rejser.rejser_convert_from_tuple(record)  # Convert tuple to Container
    dcsql.rejser_create_record(rejser)  # Update database
    rejser_clear_container_entries()  # Clear entry boxes
    rejser_refresh_treeview(tree, dcd.Rejser)  # Refresh treeview table


def rejser_clear_container_entries():  # Clear entry boxes
    entry.delete(0, tk.END)  # Delete text in entry box, beginning with the first character (0) and ending with the last character (tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)


def rejser_update_container(tree, record):  # update tuple in database
    rejser = dcd.Rejser.rejser_convert_from_tuple(record)  # Convert tuple to Container
    dcsql.rejser_update_container(rejser)  # Update database
    rejser_clear_container_entries()  # Clear entry boxes
    rejser_refresh_treeview(tree, dcd.Rejser)  # Refresh treeview table


def rejser_delete_container(tree, record):  # delete tuple in database
    rejser = dcd.Rejser.rejser_convert_from_tuple(record)  # Convert tuple to Container
    dcsql.rejser_delete_soft_container(rejser)  # Update database
    rejser_clear_container_entries()  # Clear entry boxes
    rejser_refresh_treeview(tree, dcd.Rejser)


def rejser_read_table(tree, class_):  # fill tree from database
    count = 0  # Used to keep track of odd and even rows, because these will be colored differently.
    result = dcsql.rejser_select_all(class_)  # Read all containers from database
    for record in result:
        if record.valid():  # this condition excludes soft deleted records from being shown in the data table
            if count % 2 == 0:  # even
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.rejser_convert_to_tuple(), tags=('evenrow',))  # Insert one row into the data table
            else:  # odd
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.rejser_convert_to_tuple(), tags=('oddrow',))  # Insert one row into the data table
            count += 1


def rejser_refresh_treeview(tree, class_):  # Refresh treeview table
    rejser_empty_treeview(tree)  # Clear treeview table
    rejser_read_table(tree, class_)


def rejser_empty_treeview(tree):  # Clear treeview table
    tree.delete(*tree.get_children())


root = tk.Tk()
root.title('Plusbus')
root.geometry("1200x700")

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

label2 = tk.Label(lec, text="EMAIl")
label2.grid(row=0, column=2)

label4 = tk.Label(lec, text="PHONE-NUMBER")
label4.grid(row=0, column=4)

style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background="#ffffff", foreground="black", rowhi=rowhi, fieldbackground="#90998A",)
style.configure("Treeview.Heading", background="#1F323F", foreground="white", relief="flat", fieldbackground="#2B3F49")
style.map('Treeview', background=[('selected', tree_select)])

tree1scroll = tk.Scrollbar(Ramme)
tree1scroll.grid(row=5, column=6, padx=padx, pady=pady, sticky='ns')
tree1 = ttk.Treeview(Ramme, yscrollcommand=tree1scroll.set, selectmode="browse")
tree1.grid(row=5, column=5, padx=0, pady=pady)
tree1scroll.config(command=tree1.yview)

tree1['columns'] = ("Id", "Email", "Telefon")
tree1.column("#0", width=0, stretch=tk.NO)
tree1.column("Id", anchor=tk.E, width=30)
tree1.column("Email", anchor=tk.N, width=200)
tree1.column("Telefon", anchor=tk.W, width=80)

tree1.heading("#0", text="", anchor=tk.W)
tree1.heading("Id", text="Id", anchor=tk.CENTER)
tree1.heading("Email", text="Email", anchor=tk.CENTER)
tree1.heading("Telefon", text="Telefon", anchor=tk.CENTER)


tree1.bind("<ButtonRelease-1>", lambda event: edit_container(event, tree1))


tree1.tag_configure('oddrow', background=oddrow)
tree1.tag_configure('evenrow', background=evenrow)

read_table(tree1, dcd.Kunder)

entry = tk.Entry(lec, width=4, justify="left")
entry.grid(row=1, column=1, padx=padx, pady=pady)

entry2 = tk.Entry(lec, width=28, justify="left")
entry2.grid(row=1, column=2, padx=padx, pady=pady)

entry3 = tk.Entry(lec, width=12, justify="left")
entry3.grid(row=1, column=4, padx=padx, pady=pady)

krc = tk.Frame(Ramme_bund)
krc.grid(row=1, column=0, padx=padx, pady=pady)
knap = tk.Button(krc, text="Create", command=lambda: create_container(tree1, read_container_entries()))
knap.grid(row=2, column=1, pady=10, padx=10)


knap2 = tk.Button(krc, text="Update", command=lambda: update_container(tree1, read_container_entries()))
knap2.grid(row=2, column=2, pady=10, padx=10)
knap3 = tk.Button(krc, text="Clear", command=clear_container_entries)
knap3.grid(row=2, column=3, pady=10, padx=10)
knap4 = tk.Button(krc, text="Delete", command=lambda: delete_container(tree1, read_container_entries()))
knap4.grid(row=2, column=4, pady=10,  padx=10)


"""


•────────────────────────────•

╭──────────.★..─╮
    Rejser
╰─..★.──────────╯

•────────────────────────────•


"""

Rejser_area = tk.LabelFrame(root, text="Rejser")
Rejser_area.grid(row=0, column=1, pady=pady, padx=padx, sticky=tk.N)

Rejser_ramme = tk.Frame(Rejser_area)
Rejser_ramme.grid(row=0, column=0, padx=20)

Rejser_ramme_bund = tk.Frame(Rejser_area)
Rejser_ramme_bund.grid(row=1, column=0)

Rejser_lec = tk.Frame(Rejser_ramme_bund)
Rejser_lec.grid(row=0, column=0, padx=padx, pady=pady)

# labels
label = tk.Label(Rejser_lec, text="ID")
label.grid(row=0, column=1, pady=1, ipady=5)

label2 = tk.Label(Rejser_lec, text="Route")
label2.grid(row=0, column=2)

label3 = tk.Label(Rejser_lec, text="Date")
label3.grid(row=0, column=3)

label4 = tk.Label(Rejser_lec, text="Seats")
label4.grid(row=0, column=4)

# Entry
entry = tk.Entry(Rejser_lec, width=4, justify="left")
entry.grid(row=1, column=1, padx=padx, pady=pady)

entry2 = tk.Entry(Rejser_lec, width=28, justify="left")
entry2.grid(row=1, column=2, padx=padx, pady=pady)

entry3 = tk.Entry(Rejser_lec, width=12, justify="left")
entry3.grid(row=1, column=3, padx=padx, pady=pady)

entry4 = tk.Entry(Rejser_lec, width=12, justify="left")
entry4.grid(row=1, column=4, padx=padx, pady=pady)

# Knap
Rejser_krc = tk.Frame(Rejser_ramme_bund)
Rejser_krc.grid(row=1, column=0, padx=padx, pady=pady)
knap = tk.Button(Rejser_krc, text="Create", command=lambda: rejser_create_container(tree1, rejser_read_container_entries()))
knap.grid(row=2, column=1, pady=10, padx=10)
knap2 = tk.Button(Rejser_krc, text="Update", command=lambda: rejser_update_container(tree1, rejser_read_container_entries()))
knap2.grid(row=2, column=2, pady=10, padx=10)
knap3 = tk.Button(Rejser_krc, text="Clear", command=rejser_clear_container_entries)
knap3.grid(row=2, column=3, pady=10, padx=10)
knap4 = tk.Button(Rejser_krc, text="Delete", command=lambda: rejser_delete_container(tree1, rejser_read_container_entries()))
knap4.grid(row=2, column=4, pady=10,  padx=10)

# Treeview
tree1scroll = tk.Scrollbar(Rejser_ramme)
tree1scroll.grid(row=5, column=6, padx=padx, pady=pady, sticky='ns')
tree1 = ttk.Treeview(Rejser_ramme, yscrollcommand=tree1scroll.set, selectmode="browse")
tree1.grid(row=5, column=5, padx=0, pady=pady)
tree1scroll.config(command=tree1.yview)

tree1['columns'] = ("Id", "Route", "Date", "Seats")
tree1.column("#0", width=0, stretch=tk.NO)
tree1.column("Id", anchor=tk.E, width=30)
tree1.column("Route", anchor=tk.N, width=180)
tree1.column("Date", anchor=tk.W, width=50)
tree1.column("Seats", anchor=tk.W, width=80)

tree1.heading("#0", text="", anchor=tk.W)
tree1.heading("Id", text="Id", anchor=tk.CENTER)
tree1.heading("Route", text="Route", anchor=tk.CENTER)
tree1.heading("Date", text="Date", anchor=tk.CENTER)
tree1.heading("Seats", text="Seats", anchor=tk.CENTER)


tree1.bind("<ButtonRelease-1>", lambda event: rejser_edit_container(event, tree1))

rejser_read_table(tree1, dcd.Rejser)


tree1.tag_configure('oddrow', background=oddrow)
tree1.tag_configure('evenrow', background=evenrow)




if __name__ == '__main__':
    refresh_treeview(tree1, dcd.Kunder)
    rejser_refresh_treeview(tree1, dcd.Rejser)
    root.mainloop()