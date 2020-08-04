'''
Script to generate UI for a Python Code File
'''

# Imports
import json

import PythonCodeTokenizer as pct

# For Tkinter UI Generation
import UIGen_TKinter as uigen

# Load Config
config = json.load(open('PythonUI/WindowDataConfig.json', 'rb'))

# Main Functions
# Field Class
class Field:
    def __init__(self, name, Type, value, location, cmd=None):
        self.name = name
        self.type = Type
        self.value = value
        self.location = location
        self.command = cmd

# Generate Window Data
def GenerateWindowData(ScriptParameters, RunScriptFunc, OtherFuncs):
    WindowData = {}
    WindowData[config['Input_UI']] = []
    WindowData[config['Title_UI']] = []
    WindowData[config['Additional_UI']] = []
    WindowData[config['Button_UI']] = []

    # Generate UI for Input Parameters
    curPos = [0, 0]

    # Title Label Fields
    fieldSetNoneLabel = Field('SetNone', config['Title_Label'], 'Set None', [curPos[0], curPos[1]])
    fieldTitleLabel = Field('LabelsTitle', config['Title_Label'], 'Params', [curPos[0], curPos[1] + 1])
    fieldDataLabel = Field('EntryTitle', config['Title_Label'], 'Data', [curPos[0], curPos[1] + 2])
    WindowData[config['Title_UI']].append(fieldSetNoneLabel)
    WindowData[config['Title_UI']].append(fieldTitleLabel)
    WindowData[config['Title_UI']].append(fieldDataLabel)

    # Actual Parameter Fields
    curPos = [curPos[0] + 1, curPos[1]]
    for sp in ScriptParameters:
        if sp.value is None:
            continue
        
        # Additional Fields
        fieldNoneCheck = Field(sp.name, config['Additional_NoneCheck'], False, [curPos[0], curPos[1]], OtherFuncs[config['Additional_NoneCheck']])
        fieldLabel = Field(sp.name, config['Title_Label'], sp.name, [curPos[0], curPos[1] + 1])

        field = Field(sp.name, None, sp.value, [curPos[0], curPos[1] + 2])
        # print(sp.ui_mode)
        # print(sp.value)
        if sp.ui_mode == None:
            if sp.type == str:
                field.type = config['Input_String']
            elif sp.type == int:
                field.type = config['Input_Int']
            elif sp.type == float:
                field.type = config['Input_Float']
            elif sp.type == bool:
                field.type = config['Input_Bool']
        elif sp.ui_mode == pct.config['SpecificTypes']['Dropdown']:
            field.type = config['Input_DropdownList']


        WindowData[config['Title_UI']].append(fieldLabel)
        WindowData[config['Additional_UI']].append(fieldNoneCheck)
        WindowData[config['Input_UI']].append(field)
        
        curPos = [curPos[0] + 1, curPos[1]]
    
    # Generate UI for Run Script Button
    funcField = Field('Run Script', config['Button_Function'], RunScriptFunc, [curPos[0], curPos[1] + 1])
    WindowData[config['Button_UI']].append(funcField)
    
    return WindowData

# Driver Code
# Params
mainPath = 'TestCodes/'
codefileName = 'Test.py'

WindowTitle = 'Generated UI'
RunScriptFunc = uigen.RunScript_Basic
OtherFuncs = {config['Additional_NoneCheck']: uigen.SetNoneCommand_EntryDisable}
# Params

# RunCode
# Tokenise to get Parse Code
ParsedCode = pct.Code(mainPath + codefileName)
ScriptParameters = ParsedCode.script_parameters

# Convert to Window Data
WindowData = GenerateWindowData(ScriptParameters, RunScriptFunc, OtherFuncs)

# Display Window
uigen.CreateWindow(ParsedCode, WindowData, WindowTitle)