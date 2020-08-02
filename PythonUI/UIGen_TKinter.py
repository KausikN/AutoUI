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
    ui_items_input = []
    ui_items_button = []
    ui_items_nonecheck = []
    ui_items_other = []

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
            ui_items_other.append((field.name, l, l_val, None))
        elif field.type == 'NoneCheck':
            n_val = BooleanVar(root)
            n_val.set(bool(field.value))
            n = Checkbutton(root, var=n_val)
            n.grid(row=field.location[0], column=field.location[1])
            ui_items_nonecheck.append((field.name, n, n_val, bool))
        elif field.type == 'Function':
            FunctionData = field
        elif field.type == 'Input_String':
            e_val = StringVar(root)
            e_val.set(str(field.value))
            e = Entry(root, textvariable=e_val)
            e.grid(row=field.location[0], column=field.location[1])
            ui_items_input.append((field.name, e, e_val, str))
        elif field.type == 'Input_Bool':
            c_val = BooleanVar(root)
            c_val.set(bool(field.value))
            c = Checkbutton(root, var=c_val)
            c.grid(row=field.location[0], column=field.location[1])
            ui_items_input.append((field.name, c, c_val, bool))
        elif field.type == 'Input_Int':
            e_val = StringVar(root)
            e_val.set(str(field.value))
            e = Entry(root, textvariable=e_val)
            e.grid(row=field.location[0], column=field.location[1])
            ui_items_input.append((field.name, e, e_val, int))
        elif field.type == 'Input_Float':
            e_val = StringVar(root)
            e_val.set(str(field.value))
            e = Entry(root, textvariable=e_val)
            e.grid(row=field.location[0], column=field.location[1])
            ui_items_input.append((field.name, e, e_val, float))
        elif field.type == 'Input_DropdownList':
            OptionList = list(field.value)
            d_val = StringVar(root)
            d_val.set(str(OptionList[0]))
            d = tk.OptionMenu(root, d_val, *OptionList)
            d.grid(row=field.location[0], column=field.location[1])
            ui_items_input.append((field.name, d, d_val, type(OptionList[0])))
        
    if FunctionData is not None:
        UI_ITEMS = {"INPUT": ui_items_input, "NONECHECK": ui_items_nonecheck}
        b = Button(root, text=FunctionData.name, command=partial(FunctionData.value, UI_ITEMS, CodeData))
        b.grid(row=FunctionData.location[0], column=FunctionData.location[1])
        ui_items_button.append((FunctionData.name, b, None, None))

    print("Window Created.\n\n")
    root.mainloop()

# Driver Code