import tkinter as tk
from tkinter import ttk
import topbike_data as tpd
import topbike_func as tpf
import topbike_sql as tpsql
from dateutil import parser

padx = 8
pady = 4
rowheight = 24
treeview_background = "#ffffff"
treeview_foreground = "#000000"
treeview_selected = "#68caf7"
oddrow = "#dddddd"
evenrow = "#cccccc"

# Funktioner

# hold function start region


def read_hold_entries():  #  reads all hold entries
    return entry_hold_id.get(), entry_hold_erfaring.get(), entry_hold_storelse.get()


def clear_hold_entries():  #  clear all hold entries
    entry_hold_id.delete(0, tk.END)
    entry_hold_erfaring.delete(0, tk.END)
    entry_hold_storelse.delete(0, tk.END)


def write_hold_entries(values):
    entry_hold_id.insert(0, values[0])
    entry_hold_erfaring.insert(0, values[1])
    entry_hold_storelse.insert(0, values[2])


def edit_hold(event, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, "values")
    clear_hold_entries()
    write_hold_entries(values)


def create_hold(tree, record):
    hold = tpd.Hold.convert_from_tuple(record)
    tpsql.create_record_hold(hold)
    clear_hold_entries()
    refresh_treeview(tree, tpd.Hold)


def update_hold(tree, record):
    hold = tpd.Hold.convert_from_tuple(record)
    tpsql.update_hold(hold)
    clear_hold_entries()
    refresh_treeview(tree, tpd.Hold)


def delete_hold(tree, record):
    hold = tpd.Hold.convert_from_tuple(record)
    tpsql.soft_delete_hold(hold)
    clear_hold_entries()
    refresh_treeview(tree, tpd.Hold)

# hold function end region------------------------------

# bane function start region


def read_bane_entries():
    return entry_bane_id.get(), entry_bane_kapacitet.get(), entry_bane_sverhedsgrad.get()


def clear_bane_entries():
    entry_bane_id.delete(0, tk.END)
    entry_bane_kapacitet.delete(0, tk.END)
    entry_bane_sverhedsgrad.delete(0, tk.END)


def write_bane_entries(values):
    entry_bane_id.insert(0, values[0])
    entry_bane_kapacitet.insert(0, values[1])
    entry_bane_sverhedsgrad.insert(0, values[2])


def edit_bane(event, tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, "values")
    clear_bane_entries()
    write_bane_entries(values)


def create_bane(tree, record):
    bane = tpd.Bane.convert_from_tuple(record)
    tpsql.create_record_bane(bane)
    clear_bane_entries()
    refresh_treeview(tree, tpd.Bane)


def update_bane(tree, record):
    bane = tpd.Bane.convert_from_tuple(record)
    tpsql.update_bane(bane)
    clear_bane_entries()
    refresh_treeview(tree, tpd.Bane)


def delete_bane(tree, record):
    bane = tpd.Bane.convert_from_tuple(record)
    tpsql.soft_delete_bane(bane)
    clear_bane_entries()
    refresh_treeview()


#  end region bane functions
# start region bookings functions


def read_bookings_entries():
    return entry_bookings_id.get(), entry_bookings_dato.get(), entry_bookings_hold_id.get(), entry_bookings_bane_id.get()


def clear_bookings_entries():
    entry_bookings_id.delete(0, tk.END)
    entry_bookings_dato.delete(0, tk.END)
    entry_bookings_hold_id.delete(0, tk.END)
    entry_bookings_bane_id.delete(0, tk.END)


def write_bookings_entries(values):
    entry_bookings_id.insert(0, values[0])
    entry_bookings_dato.insert(0, values[1])
    entry_bookings_hold_id.insert(0, values[2])
    entry_bookings_bane_id.insert(0, values[3])


def edit_bookings(event,tree):
    index_selected = tree.focus()
    values = tree.item(index_selected, "values")
    clear_bookings_entries()
    write_bookings_entries(values)


def create_bookings(tree, record):
    bookings = tpd.Bookings.convert_from_tuple(record)
    print(bookings)
    already_booked = tpf.capacity_available(tpsql.get_record(tpd.Bane, bookings.bane_id), bookings.dato, tpsql.get_record(tpd.Hold, bookings.hold_id))
    print(already_booked)
    capacity_ok = True
    if not already_booked: # passes if true
        print("Allerede booked true")
        if capacity_ok:
            print("Kapacitet okay true")


def read_table(tree, class_):  # fill tree from database
    count = 0  # Used to keep track of odd and even rows, because these will be colored differently.
    result = tpsql.select_all(class_)  # Read all containers from database
    for record in result:
        if record.valid():  # this condition excludes soft deleted records from being shown in the data table
            if count % 2 == 0:  # even
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('evenrow',))  # Insert one row into the data table
            else:  # odd
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('oddrow',))  # Insert one row into the data table
            count += 1


def refresh_treeview(tree, class_):
    empty_treeview(tree)
    read_table(tree, class_)


def empty_treeview(tree):
    tree.delete(*tree.get_children())

# Slut Funktions Region

# Gui Design Region

root = tk.Tk()
root.title("Topbike Skandinavien")
root.geometry("1300x500")

style = ttk.Style()
style.theme_use("default")

style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map("Treeview", background=[("selected", treeview_selected)])

frame_hold = tk.LabelFrame(root, text="Hold")
frame_hold.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

tree_frame_hold = tk.Frame(frame_hold)
tree_frame_hold.grid(row=0, column=0, padx=padx, pady=pady)
# ---
tree_scroll_hold = tk.Scrollbar(tree_frame_hold)
tree_scroll_hold.grid(row=0, column=1, padx=padx, pady=pady)
tree_hold = ttk.Treeview(tree_frame_hold, yscrollcommand=tree_scroll_hold.set, selectmode="browse")
tree_hold.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_hold.config(command=tree_hold.yview)

tree_hold["columns"] = ("id", "erfaring", "storelse")
tree_hold.column("#0", width=0, stretch=tk.NO)
tree_hold.column("id", anchor=tk.E, width=40)
tree_hold.column("erfaring", anchor=tk.E, width=200)
tree_hold.column("storelse", anchor=tk.W, width=120)
tree_hold.heading("#0", text="", anchor=tk.W)
tree_hold.heading("id", text="id", anchor=tk.CENTER)
tree_hold.heading("erfaring", text="erfaring", anchor=tk.CENTER)
tree_hold.heading("storelse", text="storelse", anchor=tk.CENTER)
tree_hold.tag_configure('oddrow', background=oddrow)
tree_hold.tag_configure('evenrow', background=evenrow)

tree_hold.bind("<ButtonRelease-1>", lambda event: edit_hold(event, tree_hold))

# Frames for hold
controls_frame_hold = tk.Frame(frame_hold)
controls_frame_hold.grid(row=1, column=0, padx=padx, pady=pady)

# Frame for labels and entries
edit_frame_hold = tk.Frame(controls_frame_hold)
edit_frame_hold.grid(row=1, column=0, padx=padx, pady=pady)

# Frame for buttons
button_frame_hold = tk.Frame(controls_frame_hold)
button_frame_hold.grid(row=2, column=0, padx=padx, pady=pady)

# Labels and Entries
Label_hold_id = tk.Label(edit_frame_hold, text="Id")
Label_hold_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_hold_id = tk.Entry(edit_frame_hold, width=4, justify="right")
entry_hold_id.grid(row=1, column=0, padx=padx, pady=pady)

Label_hold_erfaring = tk.Label(edit_frame_hold, text="Erfaring")
Label_hold_erfaring.grid(row=0, column=1, padx=padx, pady=pady)
entry_hold_erfaring = tk.Entry(edit_frame_hold, width=15, justify="right")
entry_hold_erfaring.grid(row=1, column=1, padx=padx, pady=pady)

label_hold_storelse = tk.Label(edit_frame_hold, text="Størelse")
label_hold_storelse.grid(row=0, column=2, padx=padx, pady=pady)
entry_hold_storelse = tk.Entry(edit_frame_hold, width=10, justify="right")
entry_hold_storelse.grid(row=1, column=2, padx=padx, pady=pady)

# Buttons
button_create_hold = tk.Button(button_frame_hold, text="Create", command=lambda: create_hold(tree_hold, read_hold_entries()))
button_create_hold.grid(row=0, column=0, padx=padx, pady=pady)

button_update_hold = tk.Button(button_frame_hold, text="Update", command=lambda: update_hold(tree_hold, read_hold_entries()))
button_update_hold.grid(row=0, column=1, padx=padx, pady=pady)

button_delete_hold = tk.Button(button_frame_hold, text="Delete", command=lambda: delete_hold(tree_hold, read_hold_entries()))
button_delete_hold.grid(row=0, column=2, padx=padx, pady=pady)

button_clear_entries_hold = tk.Button(button_frame_hold, text="Clear entries", command=clear_hold_entries)
button_clear_entries_hold.grid(row=0, column=3, padx=padx, pady=padx)

# hold slut region

# Bane Start Region

frame_bane = tk.LabelFrame(root, text="Bane")
frame_bane.grid(row=0, column=2, padx=padx, pady=pady, sticky=tk.N)

tree_frame_bane = tk.Frame(frame_bane)
tree_frame_bane.grid(row=0, column=0, padx=padx, pady=pady)
# ---
tree_scroll_bane = tk.Scrollbar(tree_frame_bane)
tree_scroll_bane.grid(row=0, column=1, padx=padx, pady=pady)
tree_bane = ttk.Treeview(tree_frame_bane, yscrollcommand=tree_scroll_bane.set, selectmode="browse")
tree_bane.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_bane.config(command=tree_bane.yview)

tree_bane["columns"] = ("id", "kapacitet", "sverhedsgrad")
tree_bane.column("#0", width=0, stretch=tk.NO)
tree_bane.column("id", anchor=tk.E, width=40)
tree_bane.column("kapacitet", anchor=tk.E, width=200)
tree_bane.column("sverhedsgrad", anchor=tk.W, width=120)
tree_bane.heading("#0", text="", anchor=tk.W)
tree_bane.heading("id", text="id", anchor=tk.CENTER)
tree_bane.heading("kapacitet", text="kapacitet", anchor=tk.CENTER)
tree_bane.heading("sverhedsgrad", text="sverhedsgrad", anchor=tk.CENTER)

tree_bane.tag_configure("oddrow", background=oddrow)
tree_bane.tag_configure("evenrow", background=evenrow)

tree_bane.bind("<ButtonRelease-1>", lambda event: edit_bane(event, tree_bane))

# Frames for frames
controls_frame_bane = tk.Frame(frame_bane)
controls_frame_bane.grid(row=11, column=0, padx=padx, pady=pady)

# Frame for labels and entries
edit_frame_bane = tk.Frame(controls_frame_bane)
edit_frame_bane.grid(row=0, column=0, padx=padx, pady=pady)

label_bane_id = tk.Label(edit_frame_bane, text="Id")
label_bane_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_bane_id = tk.Entry(edit_frame_bane, width=4, justify="center")
entry_bane_id.grid(row=1, column=0, padx=padx, pady=pady)

label_bane_kapacitet = tk.Label(edit_frame_bane, text="Kapacitet")
label_bane_kapacitet.grid(row=0, column=1, padx=padx, pady=pady)
entry_bane_kapacitet = tk.Entry(edit_frame_bane, width=10, justify="center")
entry_bane_kapacitet.grid(row=1, column=1, padx=padx, pady=pady)

label_bane_sverhedsgrad = tk.Label(edit_frame_bane, text="Sværhedsgrad")
label_bane_sverhedsgrad.grid(row=0, column=2, padx=padx, pady=pady)
entry_bane_sverhedsgrad = tk.Entry(edit_frame_bane, width=10, justify="center")
entry_bane_sverhedsgrad.grid(row=1, column=2, padx=padx, pady=pady)

# Frame for buttons
button_frame_bane = tk.Frame(controls_frame_bane)
button_frame_bane.grid(row=1, column=0, padx=padx, pady=pady)

# Difine Buttons
button_create_bane = tk.Button(button_frame_bane, text="Create", command=lambda: create_bane(tree_bane, read_bane_entries()))
button_create_bane.grid(row=0, column=1, padx=padx, pady=pady)
button_update_bane = tk.Button(button_frame_bane, text="Update", command=lambda: update_bane(tree_bane, read_bane_entries()))
button_update_bane.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_bane = tk.Button(button_frame_bane, text="Delete", command=lambda: delete_bane(tree_bane, read_bane_entries()))
button_delete_bane.grid(row=0, column=3, padx=padx, pady=pady)
button_clear_bane_entries = tk.Button(button_frame_bane, text="Clear Entry Boxes", command=clear_bane_entries)
button_clear_bane_entries.grid(row=0, column=4, padx=padx, pady=pady)

# bane end region

# Bookings Start Region
frame_bookings = tk.LabelFrame(root, text="Bookings")
frame_bookings.grid(row=0, column=3, padx=padx, pady=pady, sticky=tk.N)


tree_frame_bookings = tk.Frame(frame_bookings)
tree_frame_bookings.grid(row=0, column=0, padx=padx, pady=pady)
tree_scroll_bookings = tk.Scrollbar(tree_frame_bookings)
tree_scroll_bookings.grid(row=0, column=1, padx=0, pady=pady, sticky='ns')
tree_bookings = ttk.Treeview(tree_frame_bookings, yscrollcommand=tree_scroll_bookings.set, selectmode="browse")
tree_bookings.grid(row=0, column=0, padx=0, pady=pady)
tree_scroll_bookings.config(command=tree_bookings.yview)

tree_bookings['columns'] = ("id", "dato", "hold_id", "bane_id")
tree_bookings.column("#0", width=0, stretch=tk.NO)
tree_bookings.column("id", anchor=tk.E, width=40)
tree_bookings.column("dato", anchor=tk.CENTER, width=100)
tree_bookings.column("hold_id", anchor=tk.CENTER, width=100)
tree_bookings.column("bane_id", anchor=tk.CENTER, width=100)

tree_bookings.heading("#0", text="", anchor=tk.W)
tree_bookings.heading("id", text="Id", anchor=tk.CENTER)
tree_bookings.heading("dato", text="Date", anchor=tk.CENTER)
tree_bookings.heading("hold_id", text="Hold id", anchor=tk.CENTER)
tree_bookings.heading("bane_id", text="Bane id", anchor=tk.CENTER)
tree_bookings.tag_configure('oddrow', background=oddrow)
tree_bookings.tag_configure('evenrow', background=evenrow)

tree_bookings.bind("<ButtonRelease-1>", lambda event: edit_bookings(event, tree_bookings))

controls_frame_bookings = tk.Frame(frame_bookings)
controls_frame_bookings.grid(row=3, column=0, padx=padx, pady=pady)

edit_frame_bookings = tk.Frame(controls_frame_bookings)  # Add tuple entry boxes
edit_frame_bookings.grid(row=0, column=0, padx=padx, pady=pady)

label_bookings_id = tk.Label(edit_frame_bookings, text="Id")
label_bookings_id.grid(row=0, column=0, padx=padx, pady=pady)
entry_bookings_id = tk.Entry(edit_frame_bookings, width=4, justify="center")
entry_bookings_id.grid(row=1, column=0, padx=padx, pady=pady)

label_bookings_dato = tk.Label(edit_frame_bookings, text="Dato")
label_bookings_dato.grid(row=0, column=1, padx=padx, pady=pady)
entry_bookings_dato = tk.Entry(edit_frame_bookings, width=10, justify="center")
entry_bookings_dato.grid(row=1, column=1, padx=padx, pady=pady)

label_bookings_hold_id = tk.Label(edit_frame_bookings, text="Hold id")
label_bookings_hold_id.grid(row=0, column=2, padx=padx, pady=pady)
entry_bookings_hold_id = tk.Entry(edit_frame_bookings, width=10, justify="center")
entry_bookings_hold_id.grid(row=1, column=2, padx=padx, pady=pady)

label_bookings_bane_id = tk.Label(edit_frame_bookings, text="Bane id")
label_bookings_bane_id.grid(row=0, column=3, padx=padx, pady=pady)
entry_bookings_bane_id = tk.Entry(edit_frame_bookings, width=10, justify="center")
entry_bookings_bane_id.grid(row=1, column=3, padx=padx, pady=pady)

# Define Frame containing buttons
button_frame_bookings = tk.Frame(controls_frame_bookings)
button_frame_bookings.grid(row=1, column=0, padx=padx, pady=pady)

# Define buttons
button_create_bookings = tk.Button(button_frame_bookings, text="Create", command=lambda: create_bookings(tree_bookings, read_bookings_entries()))
button_create_bookings.grid(row=0, column=1, padx=padx, pady=pady)
button_update_bookings = tk.Button(button_frame_bookings, text="Update", command=lambda: update_bookings(tree_bookings, read_bookings_entries()))
button_update_bookings.grid(row=0, column=2, padx=padx, pady=pady)
button_delete_bookings = tk.Button(button_frame_bookings, text="Delete", command=lambda: button_delete(tree_bookings, read_bookings_entries()))
button_delete_bookings.grid(row=0, column=3, padx=padx, pady=pady)
button_clear_bookings_entries = tk.Button(button_frame_bookings, text="Clear Entry Boxes", command=clear_bookings_entries)
button_clear_bookings_entries.grid(row=0, column=4, padx=padx, pady=pady)
# Gui Design Slut

if __name__ == "__main__":
    refresh_treeview(tree_hold, tpd.Hold)
    refresh_treeview(tree_bane, tpd.Bane)
    refresh_treeview(tree_bookings, tpd.Bookings)
    root.mainloop()