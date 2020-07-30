'''
Tokenizes any Python Code
'''

# Imports
import re

# Main Functions
# Basic Functions
def ReadPythonCode(path):
    return open(path, 'r').readlines()

# Code Class
class Code:
    def __init__(self, path):
        self.code_path = path
        self.tokenize()

    def tokenize(self):
        # Read the code lines
        self.code_lines = ReadPythonCode(self.code_path)
        # Tokenize and get all the required parts of the code
        self.script_desc, self.imports, self.funcs, self.parameters, self.driver_code = PythonCode_Tokenize(self.code_lines)

# Function Class
class Function:
    def __init__(self, name, desc, parameters, code, returnVal):
        self.name = name
        self.desc = desc
        self.parameters = parameters
        self.code = code
        self.returnVal = returnVal

# Following Rules should be followed in Code
# 1. Script Description MUST be given at start in ''' or """
# 2. Code must be separated in 3 parts:
#       -   Imports after line # Imports
#       -   Functions after line # Main Functions
#       -   Driver Code after line # Driver Code
def PythonCode_Tokenize(code_lines):
    # Preprocess
    # Remove all empty lines
    code_lines_preprocessed = []
    for l in code_lines:
        if not l.strip() == '':
            code_lines_preprocessed.append(l)
    code_lines = code_lines_preprocessed

    curIndex = 0
    # Get the Script Description
    ScriptDesc, remaining_code_lines = GetScriptDesc(code_lines)
    code_lines = remaining_code_lines
    print(code_lines)
        
    Imports = None
    Functions = None
    Params = None
    DriverCode = None
    return ScriptDesc, Imports, Functions, Params, DriverCode
            
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

    ScriptDesc = ScriptDesc.strip('\n')

    return ScriptDesc, remaining_code_lines


# Driver Code
# Params
mainPath = 'TestCodes/'
fileName = 'Test.py'

PyCode = Code(mainPath + fileName)
print(PyCode.script_desc)