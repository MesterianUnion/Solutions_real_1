import tkinter as tk

padx = 8
pady = 4

root = tk.Tk()
root.title('GUI')
root.geometry("500x500")

frame = tk.Frame(root)
frame.grid(row=0, column=0, padx=padx, pady=pady, sticky=tk.N)

knap = tk.Button(root, bg="Red", text="Hej")
knap.grid(row=0, column=1, padx=padx, pady=pady)

label = tk.Label(frame, bg="Darkgray", text="Hej med dig")
label.grid(row=2, column=3, padx=padx, pady=pady)

entry = tk.Entry(frame, justify="right")
entry.grid(row=1, column=2, padx=padx, pady=pady)
entry.insert(0, "Skriv her")


if __name__ == '__main__':
    root.mainloop()