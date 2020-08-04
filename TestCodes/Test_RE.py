"""
Script Description
"""

# Imports
import numpy as np

# Main Functions
def  Sum(a, b):
    if a == None:
        return '1'
    return a+b
def  Diff(a, b):
    return a-b
def  Mult(a, b):
    return a*b
def  AND(a, b):
    return a and b
def  POWER(a, b):
    return a**b

# Driver Code
# Params
IntVal = 2
BoolVal = False
StrVal = "LOLHI"
FloatVal = -12213.1313
DropDownVal = [23.0, 46.0, 97.0]

# Driver Code
print("Inputs:")
print("IntVal:", IntVal)
print("BoolVal:", BoolVal)
print("StrVal:", StrVal)
print("FloatVal:", FloatVal)
print("DropDownVal:", DropDownVal)
StrSum = Sum(StrVal, StrVal)
IntDiff = Diff(IntVal, 0)
FloatMult = Mult(FloatVal, FloatVal)
BoolAND = AND(BoolVal, BoolVal)
DropdownPOWER = POWER(DropDownVal, DropDownVal)
print("Outputs:")
print("SUM:", StrSum)
print("DIFF:", IntDiff)
print("MULT", FloatMult)
print("AND", BoolAND)
print("DROPDOWN POWER:", DropdownPOWER)