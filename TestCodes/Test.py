'''
Script Description
'''

# Imports
import numpy as np

# Main Functions
def Sum(a, b):
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

# Driver Code
# LOLBOI
# Params
IntVal = -10
BoolVal = False
StrVal = 'LOLHI'
FloatVal = -12213.1313
# Params
StrSum = Sum(StrVal, StrVal)
IntDiff = Diff(IntVal, 0)
FloatMult = Mult(FloatVal, FloatVal)
BoolAND = AND(BoolVal, BoolVal)
print(StrSum)
print(IntDiff)
print(FloatMult)
print(BoolAND)