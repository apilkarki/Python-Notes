#!/usr/bin/env python
'''The Very basics for a TK window'''

from tkinter import * 
from tkinter import ttk # tkinter themes

root = TK()
button = ttk.Button(root, text = 'Click Me') # is a themed button (OS specific?)
button.pack() # Causes the button to be displayed, and where to be displayed.

# To find the value of a particular widget's attribute
print(button['text']) # prints 'Click Me'

# We can also change the value of a particular widget's attribute
button['text'] = 'Click You!'

# another way to modify a widget's attribute is to use <widget.config(key = value)>
button.config(text = 'Push Me')

# For a list of all attributes for a widget simply enter <widget.config()>
print(button.config())

# every widget has string representation, you can view this by using 
# str(<widget_name>)
# str(root) == '.'

label = ttk.Label(root, text = 'Hello, Tkinter!').pack()
root.mainloop()
