import tkinter as tk

padx = 15
pady = 30

root = tk.Tk()
root.title('Roblox Klement')
root.geometry("400x600")

knap1 = tk.Button(root, text="Knap 2")
knap1.grid(row=0, column=1, padx=padx, pady=pady)

entry = tk.Entry(root, justify="right")
entry.grid(row=2, column=2, padx=padx, pady=pady)
entry.insert(0, "Test")

label = tk.Label(root, text="Label")
label.grid(row=1, column=3, padx=90, pady=90)

if __name__ == '__main__':
    root.mainloop()