'''
Script to generate Tkinter UI programmatically
'''

# Imports
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from functools import partial

# Main Functions
def CreateWindow(CodeData, WindowData, WindowTitle):
    ui_items = []

    # Init
    print('Creating Window...')
    root = Tk()
    root.title(WindowTitle)

    FunctionData = None
    for field in WindowData:
        if field.type == 'Label':
            l_val = StringVar(root)
            l_val.set(str(field.value))
            l = Label(root, textvariable=l_val)
            l.grid(row=field.location[0], column=field.location[1])
            ui_items.append((field.name, l, l_val, None))
        elif field.type == 'Function':
            FunctionData = field
        elif field.type == 'Input_String':
            e_val = StringVar(root)
            e_val.set(str(field.value))
            e = Entry(root, textvariable=e_val)
            e.grid(row=field.location[0], column=field.location[1])
            ui_items.append((field.name, e, e_val, str))
        elif field.type == 'Input_Bool':
            c_val = BooleanVar(root)
            c_val.set(bool(field.value))
            c = Checkbutton(root, var=c_val)
            c.grid(row=field.location[0], column=field.location[1])
            ui_items.append((field.name, c, c_val, bool))
        elif field.type == 'Input_Int':
            e_val = StringVar(root)
            e_val.set(str(field.value))
            e = Entry(root, textvariable=e_val)
            e.grid(row=field.location[0], column=field.location[1])
            ui_items.append((field.name, e, e_val, int))
        elif field.type == 'Input_Float':
            e_val = StringVar(root)
            e_val.set(str(field.value))
            e = Entry(root, textvariable=e_val)
            e.grid(row=field.location[0], column=field.location[1])
            ui_items.append((field.name, e, e_val, float))
        elif field.type == 'Input_DropdownList':
            OptionList = list(field.value)
            d_val = StringVar(root)
            d_val.set(OptionList[0])
            d = tk.OptionMenu(root, d_val, *OptionList)
            ui_items.append((field.name, d, d_val, type(OptionList[0])))
        
    if FunctionData is not None:
        b = Button(root, text=FunctionData.name, command=partial(FunctionData.value, ui_items, CodeData))
        b.grid(row=FunctionData.location[0], column=FunctionData.location[1])
        ui_items.append((FunctionData.name, b, None, None))

    root.mainloop()

# Driver Code