import tkinter as tk
from tkinter import ttk

def append_to_display(value):
    current_input.set(current_input.get() + value)

def clear_display():
    current_input.set('')

def calculate():
    try:
        result = eval(current_input.get())
        current_input.set(result)
    except Exception as e:
        current_input.set('Fejl!')

# Create a tkinter window
window = tk.Tk()
window.title("Lommeregner")

# Create a StringVar to hold the current input
current_input = tk.StringVar()
current_input.set('')

# Create an Entry widget to display the input and result
display = tk.Entry(window, textvariable=current_input, font=('Arial', 24), justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

# Create rounded buttons using ttk and custom button images
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row = 1
col = 0

# Create rounded button images with rounded corners
button_images = []
for i in range(16):
    img = tk.PhotoImage(width=1, height=1)
    img.put('#CCCCCC', to=(0, 0, 50, 50))
    img.put('black', to=(1, 1, 49, 49))
    button_images.append(img)

for button in buttons:
    if button == '=':
        ttk.Button(window, text=button, image=button_images[14], compound='center', style='Rounded.TButton', command=calculate).grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10)
    elif button == 'C':
        ttk.Button(window, text=button, image=button_images[13], compound='center', style='Rounded.TButton', command=clear_display).grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10)
    else:
        ttk.Button(window, text=button, image=button_images[buttons.index(button)], compound='center', style='Rounded.TButton', command=lambda b=button: append_to_display(b)).grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Create a style for rounded buttons
style = ttk.Style()
style.configure('Rounded.TButton', padding=0)

# Start the tkinter main.py loop
window.mainloop()
