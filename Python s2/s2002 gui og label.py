import tkinter as tk

root = tk.Tk()
root.title('Runde-hjørne er bedst')
root.geometry("1000x600")

knap1 = tk.Button(root, text="Jeg er en firkantet knap")
knap1.grid(row=0, column=1)
knap2 = tk.Button(root, text="Knap 2")
knap2.grid(row=1, column=1)
knap3 = tk.Button(root, text="Knap 3")
knap3.grid(row=2, column=1)
entry = tk.Entry(root, width=25, justify="right")
entry.grid(row=1, column=2)
entry.insert(0, "Skriv ikke her")
label = tk.Label(text="Det her er et label")
label.grid(row=2, column=3)
knap4 = tk.Button(root, text="Knap 4")
knap4.grid(row=3, column=3)
knap5 = tk.Button(root, text="Sidste knap")
knap5.grid(row=117, column=117)


if __name__ == '__main__':
    root.mainloop()