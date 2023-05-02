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



# Slut Funktions Region

# Gui Design Region

root = tk.Tk()
root.title("Topbike Skandinavien")
root.geometry("800x1600")

style = ttk.Style()
style.theme_use("default")

style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map("Treeview", background=[("selected", treeview_selected)])

frame_hold = tk.LabelFrame(root, text="Hold")
frame_hold.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

tree_frame_hold = tk.Frame(frame_hold)
tree_frame_hold.grid(row=0, column=1, padx=padx, pady=pady)
# ---
tree_scroll_hold = tk.Scrollbar(tree_frame_hold)
tree_scroll_hold.grid(row=0, column=1, padx=padx, pady=pady)
tree_hold = ttk.Treeview(tree_frame_hold, yscrollcommand=tree_scroll_hold.set,)

# Gui Design Slut