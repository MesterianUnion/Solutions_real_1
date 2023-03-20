import tkinter as tk
from tkinter import PhotoImage


root = tk.Tk()
root.title("Cool Tkinter Buttons")
root.config(bg="#100e17")
root.geometry("800x400")


tk.Button(root, text=" Kanp 1 ", font="Bahnscrift 20", bg="red", fg="white",
activebackground="red", activeforeground="black", borderwidth=2, relief=tk.RAISED,
cursor="hand2").place(x=200, y=100)


root.mainloop()
