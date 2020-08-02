'''
Tokenizes any Python Code
'''

# Imports
import re

# Main Functions
# Basic Functions
def ReadPythonCode(path):
    return open(path, 'r').readlines()

def CheckType(value, TypeFunc):
    try: 
        TypeFunc(value)
        return True
    except ValueError:
        return False

# Code Class
class Code:
    def __init__(self, path):
        self.code_path = path
        self.tokenize()

    def tokenize(self):
        # Read the code lines
        self.code_lines = ReadPythonCode(self.code_path)
        # Tokenize and get all the required parts of the code
        self.script_desc, self.imports, self.functions, self.script_parameters, self.driver_code = PythonCode_Tokenize(self.code_lines)

# Function Class
class Function:
    def __init__(self, name, desc, parameters, code):
        self.name = name
        self.desc = desc
        self.parameters = parameters
        self.code = code

# Script Parameters
class ScriptParameter:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.value_prefix = ''
        self.value_suffix = ''
        self.type = None
        self.ui_mode = None
        self.findType(value)
    def getCodeText(self):
        if self.value is None:
            return self.name + " = " + "None"
        else:
            return self.name + " = " + self.value_prefix + str(self.value) + self.value_suffix
    def findType(self, value):
        # Specified Type
        SpecifiedType = True
        if '#TYPE:' in value:
            SpecTypeData = re.findall('#TYPE:(.*)', value)[-1].strip().split(' ')
            if SpecTypeData[0] == 'DROPDOWN':
                self.ui_mode = 'DROPDOWN'
                choices = SpecTypeData[1].split(',')
                sp_temp = ScriptParameter('temp', choices[0])
                self.type = sp_temp.type
                self.value = list(map(self.type, choices))
            else: # Empty Specification - IGNORE
                SpecifiedType = False
        else:
            SpecifiedType = False

        if not SpecifiedType:
            # None Type
            if value == 'None':
                self.value = None
                self.type = type(None)
            # Bool Type
            elif value in ['True', 'False']:
                self.value = value == 'True'
                self.type = type(self.value)
            # String Type
            elif value.startswith('"') and value.endswith('"') or value.startswith("'") and value.endswith("'"):
                self.value = value[1:-1]
                self.type = type(self.value)
                self.value_prefix = value[0]
                self.value_suffix = value[-1]
            # Other Types
            else:
                Types = [float, int]

                TypeFound = False
                for ty in Types:
                    if CheckType(value, ty):
                        self.value = ty(value)
                        self.type = type(self.value)
                        TypeFound = True
                        break
                
            



# Following Rules should be followed in Code
# 1. Script Description MUST be given at start in ''' or """
# 2. Code must be separated in 3 parts:
#       -   Imports after line # Imports
#       -   Functions after line # Main Functions
#       -   Driver Code after line # Driver Code
def PythonCode_Tokenize(code_lines, verbose=False):
    # Preprocess
    # Remove all empty lines
    code_lines_preprocessed = []
    for l in code_lines:
        if not l.strip() == '':
            code_lines_preprocessed.append(l)
    code_lines = code_lines_preprocessed

    if verbose:
        print("Initial Code:\n", code_lines)

    curIndex = 0
    # Get the Script Description
    ScriptDesc, remaining_code_lines = GetScriptDesc(code_lines)
    code_lines = remaining_code_lines
    if verbose:
        print("Script Desc:\n", ScriptDesc)
        # print("Code after Script Desc:\n", code_lines)

    # Get the Imports
    Imports, remaining_code_lines = GetImports(code_lines)
    code_lines = remaining_code_lines
    if verbose:
        print("Imports:\n", Imports)
        # print("Code after Imports:\n", code_lines)

    # Get Functions
    Functions, remaining_code_lines = GetFunctions(code_lines)
    code_lines = remaining_code_lines
    if verbose:
        print("Functions:\n")
        for f in Functions:
            print(f.name, "\n", f.parameters, "\n", f.code)
        # print("Code after Functions Code:\n", code_lines)

    # Get ScriptParameters
    ScriptParameters, remaining_code_lines = GetScriptParameters(code_lines)
    code_lines = remaining_code_lines
    if verbose:
        print("ScriptParameters:\n")
        for sp in ScriptParameters:
            print(sp.name, "\n", sp.value, "\n", sp.type)
        # print("Code after ScriptParameters:\n", code_lines)
    
    # Get Driver Code
    DriverCode = code_lines
    if verbose:
        print("Driver Code:\n")
        for c in DriverCode:
            print(c)

    return ScriptDesc, Imports, Functions, ScriptParameters, DriverCode
            
def GetScriptDesc(code_lines):
    remaining_code_lines = []

    ScriptDesc = ''
    DescSeparators = ['"""', "'''"]
    
    DescFound = False
    SepFound = False
    UsedSep = None
    for i in range(len(code_lines)):
        if DescFound:
            remaining_code_lines.append(code_lines[i])
            continue
        l = code_lines[i].strip()
        if not SepFound:
            for sep in DescSeparators:
                if l.startswith(sep):
                    UsedSep = sep
                    SepFound = True
                    if len(l) > len(UsedSep):
                        ScriptDesc = l[len(UsedSep):]
                        # print("Added1:", l[len(UsedSep):])
                        if l.endswith(UsedSep):
                            if len(ScriptDesc) > len(UsedSep):
                                ScriptDesc = ScriptDesc[:-len(UsedSep)]
                                # print("Replaced Same Line:", ScriptDesc[:-len(UsedSep)])
                            SepFound = False
                            DescFound = True
                        else:
                            ScriptDesc = ScriptDesc + "\n"
                            # print("Added:", "\\n")
                    break
            if SepFound:
                continue
        if SepFound:
            if l.endswith(UsedSep):
                if len(l) > len(UsedSep):
                    ScriptDesc = ScriptDesc + l[:-len(UsedSep)]
                    # print("Added2:", l[:-len(UsedSep)])
                SepFound = False
                DescFound = True
            else:
                ScriptDesc = ScriptDesc + l + "\n"
                # print("Added3:", l)

    if not DescFound:
        ScriptDesc = ''
        remaining_code_lines = code_lines

    ScriptDesc = ScriptDesc.strip('\n')

    return ScriptDesc, remaining_code_lines

def GetImports(code_lines):
    remaining_code_lines = []

    Imports = []

    lastImport_Index = -1
    for i in range(len(code_lines)):
        if re.search('^import', code_lines[i]) is not None or re.search('^from .* import', code_lines[i]) is not None:
            Imports.append(code_lines[i].strip('\n'))
            lastImport_Index = i

    if lastImport_Index == -1:
        remaining_code_lines = code_lines
    elif lastImport_Index < len(code_lines)-1:
        remaining_code_lines = code_lines[lastImport_Index+1:]

    return Imports, remaining_code_lines

def GetFunctions(code_lines):
    remaining_code_lines = []

    Functions = []
    FunctionStart = 'def'
    FunctionEnd = '#FEND'

    FunctionStarted = False
    curFunction = None
    for i in range(len(code_lines)):
        if FunctionStarted:
            if code_lines[i].strip().startswith(FunctionEnd):
                FunctionStarted = False
                Functions.append(curFunction)
                curFunction = None
                if i < len(code_lines)-1:
                    remaining_code_lines = code_lines[i+1:]
                continue
            else:
                curFunction.code.append(code_lines[i].strip('\n'))
        elif re.search('^' + FunctionStart, code_lines[i]) is not None:
            FunctionStarted = True
            name = re.findall('^' + FunctionStart + '(.*)\(', code_lines[i])[0].strip('\n')
            parameters = re.findall('^' + FunctionStart + '.*\((.*)\)', code_lines[i])[0].replace(' ', '').strip('\n').split(',')
            curFunction = Function(name, '', parameters, [])
            continue

    if len(Functions) == 0:
        remaining_code_lines = code_lines

    return Functions, remaining_code_lines

def GetScriptParameters(code_lines):
    remaining_code_lines = []

    ScriptParameters = []
    ParamsStart = '# Params'
    ParamsEnd = '# Params'

    ParamsStarted = False
    curParams = []
    for i in range(len(code_lines)):
        if ParamsStarted:
            if code_lines[i].strip().startswith(ParamsEnd):
                ParamsStarted = False
                ScriptParameters.extend(curParams)
                curParams = []
                continue
            else:
                name = re.findall('^(.*)=', code_lines[i])[0].strip().strip('\n')
                value = re.findall('^.*=(.*)', code_lines[i])[0].strip().strip('\n')
                param = ScriptParameter(name, value)
                curParams.append(param)
        elif re.search('^' + ParamsStart, code_lines[i]) is not None:
            ParamsStarted = True
            continue
        else:
            remaining_code_lines.append(code_lines[i].strip().strip('\n'))

    return ScriptParameters, remaining_code_lines

# Reconstruction Functions
def ReconstructCodeText(code_data):
    code_text = []

    # Reconstruct Script Desc
    code_text.append("'''")
    code_text.append(code_data.script_desc)
    code_text.append("'''")

    code_text.append("")

    # Reconstruct Imports
    code_text.append("# Imports")
    for imp in code_data.imports:
        code_text.append(imp)
    
    code_text.append("")

    # Reconstruct Main Functions
    code_text.append("# Main Functions")
    for f in code_data.functions:
        code_text.append("def " + f.name + "(" + ', '.join(f.parameters) + "):")
        code_text.extend(f.code)

    code_text.append("")

    # Reconstruct Script Parameters
    code_text.append("# Driver Code")
    code_text.append("# Params")
    for sp in code_data.script_parameters:
        code_text.append(sp.getCodeText())

    code_text.append("")

    # Reconstruct Driver Code
    code_text.extend(code_data.driver_code)

    return '\n'.join(code_text)

"""
# Driver Code
# Params
mainPath = 'TestCodes/'
fileName = 'Test.py'

ReconstructedCode_savePath = 'Test_RE.py'

# Parse Original Code
PyCode = Code(mainPath + fileName)

# Change Data
changeParamName = 'IntVal'
replaceVal = 2
for i in range(len(PyCode.script_parameters)):
    if PyCode.script_parameters[i].name == changeParamName:
        PyCode.script_parameters[i].value = replaceVal

# Reconstruct Code
code_RE = ReconstructCodeText(PyCode)
open(mainPath + ReconstructedCode_savePath, 'w').write(code_RE)
"""