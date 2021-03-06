'''
Script Description
'''

# Imports
import numpy as np

# Main Functions
def Sum(a, b):
    if a == None:
        return '1'
    return a+b
#FEND
def Diff(a, b):
    return a-b
#FEND
def Mult(a, b):
    return a*b
#FEND
def AND(a, b):
    return a and b
#FEND
def POWER(a, b):
    return a**b
#FEND

# Driver Code
# Params
IntVal = -10
BoolVal = False
StrVal = "Hi!"
FloatVal = -12213.1313
DropDownVal = '' #TYPE: SELECTVAL NOTYPE Sum,Diff,Mult,AND,POWER
ImageVal = '' #TYPE: FILE Image
TextVal = '' #TYPE: FILE Text
FileVal = '' #TYPE: FILE
ListVal = [1, '2', 3.0, True] #SIZE 1,5
# Params
print("Inputs:")
print("IntVal:", IntVal)
print("BoolVal:", BoolVal)
print("StrVal:", StrVal)
print("FloatVal:", FloatVal)
print("DropDownVal:", DropDownVal)
print("ImageVal:", ImageVal)
print("TextVal:", TextVal)
print("FileVal:", FileVal)
print("ListVal:", ListVal)
StrSum = Sum(StrVal, StrVal)
IntDiff = Diff(IntVal, 0)
FloatMult = Mult(FloatVal, FloatVal)
BoolAND = AND(BoolVal, BoolVal)
DropdownPOWER = POWER(IntVal, IntVal)
print("Outputs:")
print("SUM:", StrSum)
print("DIFF:", IntDiff)
print("MULT", FloatMult)
print("AND", BoolAND)
print("DROPDOWN POWER:", DropdownPOWER)