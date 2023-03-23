import tkinter as tk

padx = 8
pady = 4

root = tk.Tk()
root.title('S2008 GUI')
root.geometry("500x500")

Ramme_grid = tk.LabelFrame(root, text="Main Area")
Ramme_grid.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

Ramme = tk.Frame(Ramme_grid)
Ramme.grid(row=0, column=0, padx=20)

label = tk.Label(Ramme, text="ID")
label.grid(row=0, column=1, pady=1, ipady=5)

label2 = tk.Label(Ramme, text="Vægt")
label2.grid(row=0, column=2)

label3 = tk.Label(Ramme, text="Destination")
label3.grid(row=0, column=3)

label4 = tk.Label(Ramme, text="Vejret")
label4.grid(row=0, column=4)


def clean():
    print("🏴󠁭󠁵󠁰󠁷󠁿 Du rentgjorde teksten")
    entry.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)


entry = tk.Entry(Ramme, width=4, justify="left")
entry.grid(row=1, column=1, padx=padx, pady=pady)

entry2 = tk.Entry(Ramme, width=8, justify="left")
entry2.grid(row=1, column=2, padx=padx, pady=pady)

entry3 = tk.Entry(Ramme, width=20, justify="left")
entry3.grid(row=1, column=3, padx=padx, pady=pady)

entry4 = tk.Entry(Ramme, width=14, justify="left")
entry4.grid(row=1, column=4, padx=padx, pady=pady)


frame_knap = tk.Frame(Ramme_grid)
frame_knap.grid(row=1, column=0,)
knap = tk.Button(frame_knap, text="  Lav  ")
knap.grid(row=2, column=1, pady=10, padx=10)


def update():
    print("🚩 Du opdateret programmet")
    knap2.quit()


knap2 = tk.Button(frame_knap, text="Opdater", command=update)
knap2.grid(row=2, column=2, pady=10, padx=10)

knap3 = tk.Button(frame_knap, text="   Slet   ")
knap3.grid(row=2, column=3, pady=10, padx=10)

knap4 = tk.Button(frame_knap, text="   Slet alt   ", command=clean)
knap4.grid(row=2, column=4, pady=10,  padx=10)



if __name__ == '__main__':
    root.mainloop()