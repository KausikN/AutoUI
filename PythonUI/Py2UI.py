'''
Script to generate UI for a Python Code File
'''

# Imports
import PythonCodeTokenizer as pct

# For Tkinter UI Generation
import UIGen_TKinter as uigen

# Main Functions
# Field Class
class Field:
    def __init__(self, name, Type, value, location):
        self.name = name
        self.type = Type
        self.value = value
        self.location = location

# Generate Window Data
def GenerateWindowData(ScriptParameters, RunScriptFunc):
    WindowData = []

    # Generate UI for Input Parameters
    curPos = [0, 0]

    fieldSetNoneLabel = Field('SetNone', 'Label', 'Set None', [curPos[0], curPos[1] + 2])
    WindowData.append(fieldSetNoneLabel)
    curPos = [curPos[0] + 1, curPos[1]]
    for sp in ScriptParameters:
        if sp.value is None:
            continue
        
        # Additional Fields
        fieldLabel = Field(sp.name, 'Label', sp.name, [curPos[0], curPos[1]])
        fieldNoneCheck = Field(sp.name, 'NoneCheck', False, [curPos[0], curPos[1] + 2])

        field = Field(sp.name, None, sp.value, [curPos[0], curPos[1] + 1])
        # print(sp.ui_mode)
        # print(sp.value)
        if sp.ui_mode == None:
            if sp.type == str:
                field.type = 'Input_String'
            elif sp.type == int:
                field.type = 'Input_Int'
            elif sp.type == float:
                field.type = 'Input_Float'
            elif sp.type == bool:
                field.type = 'Input_Bool'
        elif sp.ui_mode == 'DROPDOWN':
            field.type = 'Input_DropdownList'


        WindowData.append(fieldLabel)
        WindowData.append(fieldNoneCheck)
        WindowData.append(field)
        
        curPos = [curPos[0] + 1, curPos[1]]
    
    # Generate UI for Run Script Button
    funcField = Field('Run Script', 'Function', RunScriptFunc, [curPos[0], curPos[1] + 1])
    WindowData.append(funcField)
    
    return WindowData

def RunScript_Basic(ui_items, ParsedCode):
    inputs = {}

    # Check for None Input
    NoneInputNames = []
    for item in ui_items['NONECHECK']:
        for i in range(len(ParsedCode.script_parameters)):
            if ParsedCode.script_parameters[i].name == item[0]:
                if item[3] is not None:
                    print(item[2].get())
                    check = item[3](item[2].get())
                    if check:
                        NoneInputNames.append(item[0])
                    break

    # Gather Inputs from UI
    for item in ui_items['INPUT']:
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
# Params
mainPath = 'TestCodes/'
codefileName = 'Test.py'

UIFormatPath = 'PythonUI/TkinterFormat.py'

tempcode_Path = 'TestCodes/temp.py'

WindowTitle = 'Test'
RunScriptFunc = RunScript_Basic
# Params

# RunCode
# Tokenise to get Parse Code
ParsedCode = pct.Code(mainPath + codefileName)
ScriptParameters = ParsedCode.script_parameters

# Convert to Window Data
WindowData = GenerateWindowData(ScriptParameters, RunScriptFunc)

# Display Window
uigen.CreateWindow(ParsedCode, WindowData, WindowTitle)