import tkinter as tk

padx = 8
pady = 4

root = tk.Tk()
root.title('COMMAND GUI')
root.geometry("500x100")

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

knap = tk.Button(root, text=" 🥹 Kill 🥹 ", command=clean)
knap.grid(row=0, column=1, padx=padx, pady=pady)


if __name__ == '__main__':
    root.mainloop()