'''
Script to generate UI for a Python Code File
'''

# Imports
import os
import json
import pickle

import PythonCodeTokenizer as pct

# For Tkinter UI Generation
import UIGen_TKinter as uigen

# Load Config
config = json.load(open('PythonUI/WindowDataConfig.json', 'rb'))

# Main Functions
# Field Class
class Field:
    def __init__(self, name, Type, value, location, cmd=None, otherData={}):
        self.name = name
        self.type = Type
        self.value = value
        self.location = location
        self.command = cmd
        self.otherData = otherData

# Generate Window Data
def GenerateWindowData(ScriptParameters, RunScriptFunc, OtherFuncs):
    WindowData = {}
    WindowData[config['Input_UI']] = []
    WindowData[config['Output_UI']] = []
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
        field = Field(sp.name, None, sp.value, [curPos[0], curPos[1] + 2], OtherFuncs[config['Additional_DataShow']], {})
        fieldDataShow = Field(sp.name, config['Additional_DataShow'], sp.value, [curPos[0], curPos[1] + 3])
        fieldFileShow = Field(sp.name, config['Additional_FileShow'], sp.value, [curPos[0], curPos[1] + 4])

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
        elif sp.ui_mode == pct.config['SpecificTypes']['FileSelect']:
            field.type = config['Input_FileSelect']
            field.value = OtherFuncs[config['Additional_FileSelect']]
            if 'ext' in sp.otherData.keys():
                field.otherData['ext'] = sp.otherData['ext'].copy()
        elif sp.ui_mode == pct.config['SpecificTypes']['DirectorySelect']:
            field.type = config['Input_DirectorySelect']
            field.value = OtherFuncs[config['Additional_DirectorySelect']]

        WindowData[config['Title_UI']].append(fieldLabel)
        WindowData[config['Additional_UI']].append(fieldNoneCheck)
        WindowData[config['Additional_UI']].append(fieldDataShow)
        WindowData[config['Additional_UI']].append(fieldFileShow)
        WindowData[config['Input_UI']].append(field)
        
        curPos = [curPos[0] + 1, curPos[1]]
    
    # Generate UI for Run Script Button
    funcField = Field('Run Script', config['Button_Function'], RunScriptFunc, [curPos[0], curPos[1] + 1])
    WindowData[config['Button_UI']].append(funcField)
    curPos = [curPos[0] + 1, curPos[1]]

    # Generate UI for Output Text
    fieldOutputTextLabel = Field('LabelsTitle', config['Title_Label'], 'Output Text', [curPos[0], curPos[1]])
    fieldOutputText = Field('OutputText', config['Output_Text'], 'NO OUTPUT', [curPos[0], curPos[1] + 1])
    WindowData[config['Title_UI']].append(fieldOutputTextLabel)
    WindowData[config['Output_UI']].append(fieldOutputText)
    curPos = [curPos[0] + 1, curPos[1]]
    
    return WindowData

# Driver Code
# Params
mainPath = 'TestCodes/'
codefileName = 'ImageOps.py'

WindowTitle = 'Generated UI'
RunScriptFunc = uigen.RunScript_Basic
OtherFuncs = {
                config['Additional_NoneCheck']: uigen.SetNoneCommand_EntryDisable, 
                config['Additional_FileSelect']: uigen.SelectFile_ExtCheck, 
                config['Additional_DirectorySelect']: uigen.SelectDir_BasicDialogBox, 
                config['Additional_DataShow']: uigen.DataShow_WithFileDisplay
            }

JSONSuffix_ParsedCode = '_ParsedCode'
JSONSuffix_ParsedCode = '_ParsedCode'
# Params

# RunCode
# Tokenise to get Parse Code
ParsedCode = pct.Code(mainPath + codefileName)
ScriptParameters = ParsedCode.script_parameters

# Convert to Window Data
WindowData = GenerateWindowData(ScriptParameters, RunScriptFunc, OtherFuncs)

# Save Data as Pickle
pickle.dump(ParsedCode, open(mainPath + os.path.splitext(os.path.basename(codefileName))[0] + pct.config['SaveJSON_Suffix'] + ".p", 'wb'))
pickle.dump(WindowData, open(mainPath + os.path.splitext(os.path.basename(codefileName))[0] + config['SaveJSON_Suffix'] + ".p", 'wb'))

# Display Window
uigen.CreateWindow(ParsedCode, WindowData, WindowTitle)