import tkinter as tk

root = tk.Tk()
root.title('Første Gui')
root.geometry("500x700")

knap_1 = tk.Button(root, bd="10", activebackground="red", "Klik her")
myLabel1 = tk.Label(root, text=" ")
myLabel2 = tk.Label(root, text="      ")


knap_1.grid(row=1, column=1)
myLabel1.grid(row=1, column=0)
myLabel2.grid(row=0, column=0)

if __name__ == '__main__':
    root.mainloop()
