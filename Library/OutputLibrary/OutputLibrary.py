"""
Output Library for AutoUI
"""

# Imports
import json

# Main Functions
def TransfromFunc_to_string(input):
    '''
    Transform Func - Transform input data to string
    '''
    return str(input)

def TransfromFunc_to_bool(input):
    '''
    Transform Func - Transform input data to bool
    '''
    return bool(input)

def TransfromFunc_to_int(input):
    '''
    Transform Func - Transform input data to int
    '''
    return int(input)

def TransfromFunc_to_float(input):
    '''
    Transform Func - Transform input data to float
    '''
    return float(input)

def TransfromFunc_to_list(input):
    '''
    Transform Func - Transform input data to list
    '''
    return list(input)

def TransfromFunc_to_dict(input):
    '''
    Transform Func - Transform input data to dict
    '''
    return dict(input)

def TransfromFunc_to_json(input):
    '''
    Transform Func - Transform input data (dict) to json
    '''
    return json.dumps(input, indent=4)

def TransformFunc_divide(input, divisor=2):
    '''
    Transform Func - Divide input by a number
    '''
    return input / divisor


# Main Vars
OUTPUT_TRANSFORMS = {
    "to_string": TransfromFunc_to_string,
    "to_bool": TransfromFunc_to_bool,
    "to_int": TransfromFunc_to_int,
    "to_float": TransfromFunc_to_float,
    "to_list": TransfromFunc_to_list,
    "to_dict": TransfromFunc_to_dict,
    "to_json": TransfromFunc_to_json,
    "divide_by": TransformFunc_divide
}
