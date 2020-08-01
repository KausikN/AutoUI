'''
Script Description
'''

# Imports
import numpy as np

# Main Functions
def  Sum(a, b):
    return a+b
def  Diff(a, b):
    return a-b
def  Mult(a, b):
    return a*b
def  AND(a, b):
    return a and b

# Driver Code
# Params
IntVal = 2
BoolVal = False
StrVal = 'LOLHI'
FloatVal = -12213.1313

# Driver Code
# LOLBOI
StrSum = Sum(StrVal, StrVal)
IntDiff = Diff(IntVal, 0)
FloatMult = Mult(FloatVal, FloatVal)
BoolAND = AND(BoolVal, BoolVal)
print(StrSum)
print(IntDiff)
print(FloatMult)
print(BoolAND)