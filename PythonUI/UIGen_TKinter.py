'''
Script to generate Tkinter UI programmatically
'''

# Imports
import json
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from functools import partial

import PythonCodeTokenizer as pct

# Load Config
config = json.load(open('PythonUI/WindowDataConfig.json', 'rb'))

# Main Functions
def CreateWindow(CodeData, WindowData, WindowTitle):
    ui_items_input = {}
    ui_items_title = {}
    ui_items_additional = {}
    ui_items_button = {}

    # Init
    print('Creating Window...')
    root = Tk()
    root.title(WindowTitle)

    # Input UI
    for field in WindowData[config['Input_UI']]:
        val = None
        e = None
        valType = None
        if field.type == config['Input_String']:
            val = StringVar(root)
            val.set(str(field.value))
            e = Entry(root, textvariable=val)
            e.grid(row=field.location[0], column=field.location[1])
            valType = str

        elif field.type == config['Input_Bool']:
            val = BooleanVar(root)
            val.set(bool(field.value))
            e = Checkbutton(root, var=val)
            e.grid(row=field.location[0], column=field.location[1])
            valType = bool

        elif field.type == config['Input_Int']:
            val = StringVar(root)
            val.set(str(field.value))
            e = Entry(root, textvariable=val)
            e.grid(row=field.location[0], column=field.location[1])
            valType = int

        elif field.type == config['Input_Float']:
            val = StringVar(root)
            val.set(str(field.value))
            e = Entry(root, textvariable=val)
            e.grid(row=field.location[0], column=field.location[1])
            valType = float

        elif field.type == config['Input_DropdownList']:
            OptionList = list(field.value)
            val = StringVar(root)
            val.set(str(OptionList[0]))
            e = tk.OptionMenu(root, val, *OptionList)
            e.grid(row=field.location[0], column=field.location[1])
            valType = type(OptionList[0])

        # Record Data
        if field.type in ui_items_input.keys():
            ui_items_input[field.type].append((field.name, e, val, valType))
        else:
            ui_items_input[field.type] = [(field.name, e, val, valType)]

    # Title UI
    for field in WindowData[config['Title_UI']]:
        val = None
        t = None
        if field.type == config['Title_Label']:
            val = StringVar(root)
            val.set(str(field.value))
            t = Label(root, textvariable=val)
            t.grid(row=field.location[0], column=field.location[1])
        
        # Record Data
        if field.type in ui_items_title.keys():
            ui_items_title[field.type].append((field.name, t, val, None))
        else:
            ui_items_title[field.type] = [(field.name, t, val, None)]
    
    # Other UI
    for field in WindowData[config['Additional_UI']]:
        val = None
        a = None
        valType = None
        if field.type == config['Additional_NoneCheck']:
            val = BooleanVar(root)
            val.set(bool(field.value))
            UI_ITEMS = {config['Input_UI']: ui_items_input, config['Additional_UI']: ui_items_additional}
            a = Checkbutton(root, var=val, command=partial(field.command, UI_ITEMS, field.name))
            a.grid(row=field.location[0], column=field.location[1])
            valType = bool

        # Record Data
        if field.type in ui_items_additional.keys():
            ui_items_additional[field.type].append((field.name, a, val, valType))
        else:
            ui_items_additional[field.type] = [(field.name, a, val, valType)]

    # Buttons UI
    for field in WindowData[config['Button_UI']]:
        b = None
        if field.type == config['Button_Function']:
            UI_ITEMS = {config['Input_UI']: ui_items_input, config['Additional_UI']: ui_items_additional}
            b = Button(root, text=field.name, command=partial(field.value, UI_ITEMS, CodeData))
            b.grid(row=field.location[0], column=field.location[1])

        # Record Data
        if field.type in ui_items_button.keys():
            ui_items_button[field.type].append((field.name, b, None, None))
        else:
            ui_items_button[field.type] = [(field.name, b, None, None)]
            

    print("Window Created.\n\n")
    root.mainloop()

# UI Commands
def SetNoneCommand_EntryDisable(ui_items, name):
    # Disables corresponding entry field when Set None Field is Active
    # Search and get the NoneCheck Field Value
    disable = True
    for item in ui_items[config['Additional_UI']][config['Additional_NoneCheck']]:
        if name == item[0]:
            disable = item[3](item[2].get())
            break
    # Search and get the corresponding entry field
    field = None
    for itemTypeKey in ui_items[config['Input_UI']].keys():
        for item in ui_items[config['Input_UI']][itemTypeKey]:
            if name == item[0]:
                if disable:
                    item[1].configure(state=tk.DISABLED)
                else:
                    item[1].configure(state=tk.NORMAL)
                break

def RunScript_Basic(ui_items, ParsedCode):
    inputs = {}

    print(ui_items.keys())

    # Check for None Input
    NoneInputNames = []
    for item in ui_items[config['Additional_UI']][config['Additional_NoneCheck']]:
        for i in range(len(ParsedCode.script_parameters)):
            if ParsedCode.script_parameters[i].name == item[0]:
                if item[3] is not None:
                    print(item[2].get())
                    check = item[3](item[2].get())
                    if check:
                        NoneInputNames.append(item[0])
                    break

    # Gather Inputs from UI
    for itemTypeKey in ui_items[config['Input_UI']].keys():
        for item in ui_items[config['Input_UI']][itemTypeKey]:
            for i in range(len(ParsedCode.script_parameters)):
                if ParsedCode.script_parameters[i].name == item[0]:
                    if item[3] is not None:
                        # Check for None Input and assign
                        if item[0] in NoneInputNames:
                            ParsedCode.script_parameters[i].value = None
                            ParsedCode.script_parameters[i].type = type(None)
                        else:
                            ParsedCode.script_parameters[i].value = item[3](item[2].get())
                        break

    # Reconstruct new code using Inputs from UI
    code_RE = pct.ReconstructCodeText(ParsedCode)

    # Run the reconstructed Code
    print("Script Output:\n\n")
    try:
        exec(code_RE)
    except:
        print(" --- ERROR IN SCRIPT EXEC ---")


# Driver Code