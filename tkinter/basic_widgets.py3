#!/usr/bin/env python

from tkinter import *
from tkinter import ttk

root = TK()
label = ttk.Label(root, text = 'Hello, Tkinter!').pack()

# Change label text in real time
label.config(text = 'Howdy, Tkinter!')

# Notice the pack geometry manager adjusts in size to adjust to the change in label text.
# To limit the horizontal size of a text widget:
label.config(wraplength = 150)

# To adjust text RIGHT/LEFT/CENTER justify
label.config(justify = CENTER)

# To change background/foreground colors
label.cofig(foreground = 'blue', background = 'yellow')
# Note, foreground and background also take Hex values for colors as well.

# To change the font
label.config(font = ('Courier', 18, 'bold'))

# Suppose we want to use a label to display an image instead. Tkinter labels accet GIF, PGM or PPM image files.
logo = PhotoImage(file = 'path/to/file.gif')
label.config(image = logo)

# Switch back and forth between the logo displaying text and an image, use the following:
label.config(compound = 'text')
label.config(compound = 'image')
label.config(compound = 'center')
label.config(compound = 'left')
label.config(compound = 'right')
label.config(compound = 'top')
label.config(compound = 'bottom')


if __name__ == '__main__':
root.mainloop()
