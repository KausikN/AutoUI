"""
Util Functions
"""

# Imports
import sys
from io import StringIO

import tkinter as tk
from tkinter import ttk

# Main Functions
# Run String Code Functions


def RunPythonCode(code, ERRORTEXT=" --- ERROR IN SCRIPT EXEC ---"):
    '''
    Runs Python Code from a String
    '''
    ERRORCHECK = False
    RETURNDATA = False

    redirected_output = None

    if RETURNDATA:
        if ERRORCHECK:
            try:
                old_stdout = sys.stdout
                redirected_output = sys.stdout = StringIO()
                exec(code, globals())
                sys.stdout = old_stdout
            except:
                print(ERRORTEXT)
        else:
            old_stdout = sys.stdout
            redirected_output = sys.stdout = StringIO()
            exec(code, globals())
            sys.stdout = old_stdout
        return redirected_output.getvalue()

    else:
        exec(code, globals())
        return ""


    

# Other Generic Util Functions
def Threshold(val, threshold):
    '''
    Thresholds a Value between a Min and Max
    '''
    if val < threshold[0]:
        val = threshold[0]
    elif val > threshold[1]:
        val = threshold[1]
    return val

# Driver Code