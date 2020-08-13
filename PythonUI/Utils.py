'''
Util Functions
'''

# Imports
import sys
from io import StringIO
import contextlib

import tkinter as tk
from tkinter import ttk

# Main Functions
# Run String Code Functions
@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

def RunPythonCode(code, ERRORTEXT=" --- ERROR IN SCRIPT EXEC ---"):
    ERRORCHECK = False

    if ERRORCHECK:
        with stdoutIO() as s:
            try:
                exec(code, globals())
            except:
                print(ERRORTEXT)
    else:
        with stdoutIO() as s:
            exec(code, globals())

    print("OVER")

    return s.getvalue()

# Other Generic Util Functions
def Threshold(val, threshold):
    if val < threshold[0]:
        val = threshold[0]
    elif val > threshold[1]:
        val = threshold[1]
    return val

# Driver Code