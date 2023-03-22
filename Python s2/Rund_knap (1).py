import tkinter as tk


class RoundedButton(tk.Canvas):

    def __init__(self, parent, width, height, cornerradius, padding, color, command=None):
        tk.Canvas.__init__(self, parent, borderwidth=0, relief="flat", highlightthickness=0)
        self.command = command
        rad = 2*cornerradius
        self.create_polygon((padding, height-cornerradius-padding, padding, cornerradius+padding, padding+cornerradius, padding, width-padding-cornerradius, padding, width-padding, cornerradius+padding, width-padding, height-cornerradius-padding, width-padding-cornerradius, height-padding, padding+cornerradius, height-padding), fill=color, outline=color)
        self.create_arc((padding, padding+rad, padding+rad, padding), start=90, extent=90, fill=color, outline=color)
        self.create_arc((width-padding-rad, padding, width-padding, padding+rad), start=0, extent=90, fill=color, outline=color)
        self.create_arc((width-padding, height-rad-padding, width-padding-rad, height-padding), start=270, extent=90, fill=color, outline=color)
        self.create_arc((padding, height-padding-rad, padding+rad, height-padding), start=180, extent=90, fill=color, outline=color)
        (x0, y0, x1, y1) = self.bbox("all")
        width = (x1-x0)
        height = (y1-y0)
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()


def test12():
    print("Hello")


root = tk.Tk()
canvas = tk.Canvas(root, height=300, width=500)
canvas.pack()
button = RoundedButton(root, 200, 100, 50, 2, 'red', command=test12)
button.place(relx=.1, rely=.1)
root.mainloop()
