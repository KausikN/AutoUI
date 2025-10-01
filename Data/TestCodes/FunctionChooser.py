'''
Function Chooser Program
'''

# Imports
import numpy as np

# Main Functions
def SUM(a, b):
    if a == None or b == None:
        return 0.0
    return a + b
#FEND
def DIFF(a, b):
    if a == None or b == None:
        return 0.0
    return float(a) - float(b)
#FEND
def MULT(a, b):
    if a == None or b == None:
        return 0.0
    if type(a) == int or type(b) == int:
        return a * b
    return float(a) * float(b)
#FEND
def DIV(a, b):
    if a == None or b == None:
        return 0.0
    return float(a) / float(b)
#FEND
def AND(a, b):
    if a == None or b == None:
        return 0.0
    return a and b
#FEND
def POWER(a, b):
    if a == None or b == None:
        return 0.0
    return float(a) ** float(b)
#FEND

# Run Code
# Params
A = 2.1
B = 2.1
Type = None #TYPE: SELECTVAL NOTYPE float,int
Operation = None #TYPE: SELECTVAL NOTYPE SUM,DIFF,MULT,DIV,AND,POWER
# Params

# Convert to Required Type
if A is not None:
    A = Type(A)
if B is not None:
    B = Type(B)

# Display Inputs
print("Inputs:")
print("A:", A)
print("B:", B)

# Perform Chosen Operation
Val = Operation(A, B)

# Display Results
print("Outputs:")
print("Val:", Val)