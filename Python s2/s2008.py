import tkinter as tk

padx = 8
pady = 4

root = tk.Tk()
root.title('S2008 GUI')
root.geometry("500x500")

Ramme = tk.LabelFrame(root, text="Main Area")
Ramme.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

entry = tk.Entry(Ramme, justify="center")
entry.grid(row=1, column=2, padx=padx, pady=pady)
entry.insert(0, "Skriv her")

label = tk.Label(Ramme, text="Det her er et label")
label.grid(row=2, column=3, padx=padx, pady=pady)

knap = tk.Button(root, text="Den seje knap")
knap.grid(row=0, column=1, padx=padx, pady=pady)


if __name__ == '__main__':
    root.mainloop()