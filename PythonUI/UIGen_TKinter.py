'''
Script to generate Tkinter UI programmatically
'''

# Imports
import os
import json
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from functools import partial

import Utils
import PythonCodeTokenizer as pct

# Load Config
config = json.load(open('PythonUI/WindowDataConfig.json', 'rb'))
root = None
canvas = None

# Main Functions
def CreateWindow(CodeData, WindowData, WindowTitle):
    global root
    global canvas

    # Init Window
    print('Creating Window...')
    TKWindow = Tk()
    TKWindow.title(WindowTitle)
    TKWindow.grid_rowconfigure(0, weight=1)
    TKWindow.columnconfigure(0, weight=1)

    master_frame = tk.Frame(TKWindow, bd=3, relief=tk.RIDGE)
    master_frame.grid(sticky=tk.NSEW)
    master_frame.columnconfigure(0, weight=1)

    temp_frame = tk.Frame(master_frame)
    temp_frame.grid(row=0, column=0, sticky=tk.NW)

    # Add a canvas in that frame.
    canvas = tk.Canvas(temp_frame)
    canvas.grid(row=0, column=0)

    # Create a vertical scrollbar linked to the canvas.
    vsbar = tk.Scrollbar(temp_frame, orient=tk.VERTICAL, command=canvas.yview)
    vsbar.grid(row=0, column=1, sticky=tk.NS)
    canvas.configure(yscrollcommand=vsbar.set)

    # Create a horizontal scrollbar linked to the canvas.
    hsbar = tk.Scrollbar(temp_frame, orient=tk.HORIZONTAL, command=canvas.xview)
    hsbar.grid(row=1, column=0, sticky=tk.EW)
    canvas.configure(xscrollcommand=hsbar.set)

    # Create a frame on the canvas to contain the buttons.
    root = tk.Frame(canvas, bd=2)

    # Init UI Items
    ui_items_input = {}
    ui_items_title = {}
    ui_items_additional = {}
    ui_items_button = {}
    ui_items_output = {}

    UI_ITEMS = {config['Input_UI']: ui_items_input, config['Output_UI']: ui_items_output, config['Additional_UI']: ui_items_additional}

    # Input UI
    for field in WindowData[config['Input_UI']]:
        val = None
        e = None
        valType = None
        if field.type == config['Input_String']:
            val = StringVar(root)
            val.set(str(field.value))
            val.trace('w', partial(field.command, UI_ITEMS, field.name))
            e = Entry(root, textvariable=val)
            e.grid(row=field.location[0], column=field.location[1])
            valType = str

        elif field.type == config['Input_Bool']:
            val = BooleanVar(root)
            val.set(bool(field.value))
            e = Checkbutton(root, var=val, command=partial(field.command, UI_ITEMS, field.name))
            e.grid(row=field.location[0], column=field.location[1])
            valType = bool

        elif field.type == config['Input_Int']:
            val = StringVar(root)
            val.set(str(field.value))
            val.trace('w', partial(field.command, UI_ITEMS, field.name))
            e = Entry(root, textvariable=val)
            e.grid(row=field.location[0], column=field.location[1])
            valType = int

        elif field.type == config['Input_Float']:
            val = StringVar(root)
            val.set(str(field.value))
            val.trace('w', partial(field.command, UI_ITEMS, field.name))
            e = Entry(root, textvariable=val)
            e.grid(row=field.location[0], column=field.location[1])
            valType = float

        elif field.type == config['Input_DropdownList']:
            OptionList = list(field.value)
            val = StringVar(root)
            val.set(str(OptionList[0]))
            e = tk.OptionMenu(root, val, *OptionList, command=partial(field.command, UI_ITEMS, field.name))
            e.grid(row=field.location[0], column=field.location[1])
            valType = type(OptionList[0])

        elif field.type == config['Input_FileSelect']:
            val = StringVar(root)
            val.set('No File Selected')
            val.trace('w', partial(field.command, UI_ITEMS, field.name))
            e = Button(root, text="Select File", command=partial(field.value, val, field.otherData))
            e.grid(row=field.location[0], column=field.location[1])
            valType = str

        elif field.type == config['Input_DirectorySelect']:
            val = StringVar(root)
            val.set('No Dir Selected')
            val.trace('w', partial(field.command, UI_ITEMS, field.name))
            e = Button(root, text="Select Dir", command=partial(field.value, val, field.otherData))
            e.grid(row=field.location[0], column=field.location[1])
            valType = str

        # Record Data
        if field.type in ui_items_input.keys():
            ui_items_input[field.type].append((field.name, e, val, valType))
        else:
            ui_items_input[field.type] = [(field.name, e, val, valType)]

    # Output UI
    for field in WindowData[config['Output_UI']]:
        o = None
        val = None
        if field.type == config['Output_Text']:
            val = StringVar(root)
            val.set(str(field.value))
            o = Label(root, textvariable=val)
            # o = Text(root, height=4, width=50)
            o.grid(row=field.location[0], column=field.location[1])
            # TextScroll = tk.Scrollbar(root, orient=tk.VERTICAL, command=o.yview)
            # TextScroll.grid(row=field.location[0], column=field.location[1], sticky=tk.NE)
            # o.configure(yscrollcommand=TextScroll.set)
            # o.insert(tk.END, str(field.value))
            # o.configure(state=tk.DISABLED)
        
        # Record Data
        if field.type in ui_items_output.keys():
            ui_items_output[field.type].append((field.name, o, val, str))
        else:
            ui_items_output[field.type] = [(field.name, o, val, str)]

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
            # UI_ITEMS = {config['Input_UI']: ui_items_input, config['Additional_UI']: ui_items_additional}
            a = Checkbutton(root, var=val, command=partial(field.command, UI_ITEMS, field.name))
            a.grid(row=field.location[0], column=field.location[1])
            valType = bool

        elif field.type == config['Additional_DataShow']:
            val = StringVar(root)
            if field.value is None:
                val.set('None')
            else:
                val.set(str(field.value))
            a = Label(root, textvariable=val)
            a.grid(row=field.location[0], column=field.location[1])
            valType = str

        elif field.type == config['Additional_FileShow']:
            val = StringVar(root)
            val.set(" ")
            a = Label(root, textvariable=val)
            a.grid(row=field.location[0], column=field.location[1])
            valType = str

        # Record Data
        if field.type in ui_items_additional.keys():
            ui_items_additional[field.type].append((field.name, a, val, valType))
        else:
            ui_items_additional[field.type] = [(field.name, a, val, valType)]

    # Buttons UI
    for field in WindowData[config['Button_UI']]:
        b = None
        if field.type == config['Button_Function']:
            # UI_ITEMS = {config['Input_UI']: ui_items_input, config['Additional_UI']: ui_items_additional}
            b = Button(root, text=field.name, command=partial(field.value, UI_ITEMS, CodeData))
            b.grid(row=field.location[0], column=field.location[1])

        # Record Data
        if field.type in ui_items_button.keys():
            ui_items_button[field.type].append((field.name, b, None, None))
        else:
            ui_items_button[field.type] = [(field.name, b, None, None)]  

    # Create canvas window to hold the buttons_frame.
    canvas.create_window((0, 0), window=root, anchor=tk.NW)

    UpdateScrollbarData(root, canvas)

    print("Window Created.\n\n")
    TKWindow.mainloop()

# UI Commands
# Scrolling Functions
def UpdateScrollbarData(root, canvas):
    root.update_idletasks()  # Needed to make bbox info available.
    bbox = canvas.bbox(tk.ALL)  # Get bounding box of canvas with Buttons.

    # Define the scrollable region as entire canvas with only the desired
    # number of rows and columns displayed.
    w = Utils.Threshold(bbox[2]-bbox[1], [0, config['Window_MaxSize'][0]])
    h = Utils.Threshold(bbox[3]-bbox[1], [0, config['Window_MaxSize'][1]])
    # dw, dh = int((w/COLS) * COLS_DISP), int((h/ROWS) * ROWS_DISP)
    canvas.configure(scrollregion=bbox, width=w, height=h)

# Data Display Functions
def DataShow_Basic(ui_items, name, *args):
    # Search and get the DataShow corresponding Field value
    data = None
    for itemTypeKey in ui_items[config['Input_UI']].keys():
        for item in ui_items[config['Input_UI']][itemTypeKey]:
            if name == item[0]:
                # Check datatype
                if pct.CheckType(item[2].get(), item[3]):
                    data = str(item[2].get())
                else:
                    data = 'INVALID DATA'
                break
    
    # Update the Data Show Label
    for item in ui_items[config['Additional_UI']][config['Additional_DataShow']]:
        if name == item[0]:
            item[2].set(data)
            break

def DataShow_WithFileDisplay(ui_items, name, *args):
    # Search and get the DataShow corresponding Field value
    data = None
    for itemTypeKey in ui_items[config['Input_UI']].keys():
        for item in ui_items[config['Input_UI']][itemTypeKey]:
            if name == item[0]:
                # Check datatype
                if pct.CheckType(item[2].get(), item[3]):
                    data = str(item[2].get())
                else:
                    data = 'INVALID DATA'
                break

    # Update File Show Label
    for item in ui_items[config['Additional_UI']][config['Additional_FileShow']]:
        if name == item[0]:
            # Check if valid file
            if os.path.isfile(data):
                ext = os.path.splitext(data)[-1]
                # Check if data is image
                if ext in pct.config['Image_Extensions']:
                    item[2].set("Image")
                    item[1].textvariable = ''
                    item[1].image = ImageTk.PhotoImage(Image.open(data))
                    item[1].configure(image=item[1].image, textvariable='')
                # Check if text file
                elif ext in pct.config['Text_Extensions']:
                    item[1].image = ''
                    item[2].set(str(open(data, 'r').read()))
                    item[1].configure(image='', textvariable=item[2])
                # If None dont display anything
                else:
                    item[1].image = ''
                    item[2].set("Unknown File Format")
                    item[1].configure(image='', textvariable=item[2])
            break
    
    # Update the Data Show Label
    for item in ui_items[config['Additional_UI']][config['Additional_DataShow']]:
        if name == item[0]:
            item[2].set((data))
            break
    
    # Update Scrollbar Sizes
    UpdateScrollbarData(root, canvas)

# Select File Functions
def SelectFile_BasicDialogBox(val, otherData):
    # Create File Dialog Box
    filename = filedialog.askopenfilename(initialdir='./', title="Select File")
    val.set(str(filename))

def SelectFile_ExtCheck(val, otherData):
    # Create File Dialog Box
    filename = filedialog.askopenfilename(initialdir='./', title="Select File")
    # Check for accepted extensions and perform extension check
    if 'ext' in otherData.keys():
        if os.path.splitext(filename)[-1] in otherData['ext']:
            val.set(str(filename))
        else:
            val.set('INVALID FILE EXTENSION')
    else:
        val.set(str(filename))

# Select Dir Functions
def SelectDir_BasicDialogBox(val, otherData):
    # Create File Dialog Box
    dirpath = filedialog.askdirectory(initialdir='./', title="Select Dir")
    val.set(str(dirpath))

# Set None Functions
def SetNoneCommand_EntryDisable(ui_items, name):
    # Disables corresponding entry field when Set None Field is Active
    # Search and get the NoneCheck Field Value and DataShow Label and FileShow Label
    disable = True
    for item in ui_items[config['Additional_UI']][config['Additional_NoneCheck']]:
        if name == item[0]:
            disable = item[3](item[2].get())
            break
    
    FileShow_Item = None
    for item in ui_items[config['Additional_UI']][config['Additional_FileShow']]:
        if name == item[0]:
            FileShow_Item = item[1]
            break
    DataShow_Val = None
    for item in ui_items[config['Additional_UI']][config['Additional_DataShow']]:
        if name == item[0]:
            DataShow_Val = item[2]
            break

    # Search and get the corresponding entry field
    field = None
    for itemTypeKey in ui_items[config['Input_UI']].keys():
        for item in ui_items[config['Input_UI']][itemTypeKey]:
            if name == item[0]:
                if disable:
                    DataShow_Val.set('None')
                    FileShow_Item.configure(state=tk.DISABLED)
                    item[1].configure(state=tk.DISABLED)
                else:
                    FileShow_Item.configure(state=tk.NORMAL)
                    item[1].configure(state=tk.NORMAL)
                    DataShow_Val.set(str(item[2].get()))
                break

    # Update Scrollbar Sizes
    UpdateScrollbarData(root, canvas)

# Run Script Functions
def RunScript_Basic(ui_items, ParsedCode):
    inputs = {}

    # Check for None Input
    NoneInputNames = []
    for item in ui_items[config['Additional_UI']][config['Additional_NoneCheck']]:
        for i in range(len(ParsedCode.script_parameters)):
            if ParsedCode.script_parameters[i].name == item[0]:
                if item[3] is not None:
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

    # print(code_RE)
    print('\n\n')

    # Run the reconstructed Code
    print("Script Output:\n\n")
    output = Utils.RunPythonCode(code_RE)
    print(output)

    # Set Output text to Output Text UI'
    if config['Output_Text'] in ui_items[config['Output_UI']].keys():
        for i in range(len(ui_items[config['Output_UI']][config['Output_Text']])):
            # ui_items[config['Output_UI']][config['Output_Text']][i][1].configure(state=tk.NORMAL)
            # ui_items[config['Output_UI']][config['Output_Text']][i][1].insert(tk.END, output)
            # ui_items[config['Output_UI']][config['Output_Text']][i][1].configure(state=tk.DISABLED)
            ui_items[config['Output_UI']][config['Output_Text']][i][2].set(str(output))
    


# Driver Code