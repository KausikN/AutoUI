"""
AutoUI - Automated UI Generation for forming JSON data
"""

# Imports
import streamlit as st

from Library.InputLibrary.InputLibrary import *
from Library.OutputLibrary.OutputLibrary import *

# Main Functions
def AutoUI_InputUI(UIConfig):
    '''
    Generate UI - Basic UI Generation from UI Config
    '''
    # Input Vars
    INPUT_FIELDS = UIConfig["input_fields"]
    USER_INPUTS = {}
    
    # Generate Inputs
    for k in INPUT_FIELDS:
        temp_inp = INPUT_TYPES[INPUT_FIELDS[k]["input"]["type"]](**INPUT_FIELDS[k]["input"]["params"])
        for transform in INPUT_FIELDS[k]["output"]["transforms"]:
            temp_inp = OUTPUT_TRANSFORMS[transform["name"]](temp_inp, **transform.get("params", {}))
        USER_INPUTS[k] = temp_inp
    
    return USER_INPUTS

def AutoUI_GenerateDerivedFields(UIConfig, USER_INPUTS):
    '''
    Generate Derived Fields - Generate derived fields based on user inputs and UI Config
    '''
    # Input Vars
    DERIVED_FIELDS = UIConfig.get("derived_fields", {})
    DERIVED_INPUTS = {}
    TEMP_DERIVED_DATA = {}
    
    # Generate Derived Inputs
    for k in DERIVED_FIELDS:
        temp_inp = None
        for transform in DERIVED_FIELDS[k]["transforms"]:
            func_inps = {}
            for inp_key in transform["input_fields_params_map"]:
                if inp_key in USER_INPUTS:
                    func_inps[transform["input_fields_params_map"][inp_key]] = USER_INPUTS[inp_key]
                elif inp_key in TEMP_DERIVED_DATA:
                    func_inps[transform["input_fields_params_map"][inp_key]] = TEMP_DERIVED_DATA[inp_key]
            TEMP_DERIVED_DATA[transform["output_key"]] = OUTPUT_TRANSFORMS[transform["name"]](**func_inps, **transform.get("params", {}))
            temp_inp = TEMP_DERIVED_DATA[transform["output_key"]]
        DERIVED_INPUTS[k] = temp_inp

    return DERIVED_INPUTS

def AutoUI_OutputJSON(UIConfig, USER_INPUTS, DERIVED_INPUTS):
    '''
    Generate Output JSON - Generate output JSON based on user inputs, derived inputs and UI Config
    '''
    # Input Vars
    OUTPUT_FIELDS = UIConfig["output_schema"]
    OUTPUT_JSON = {}

    def recursive_dict_traversal(d, out_dict):
        for k, v in d.items():
            if isinstance(v, dict):
                out_dict[k] = {}
                recursive_dict_traversal(v, out_dict[k])
            else:
                if k in USER_INPUTS:
                    out_dict[k] = USER_INPUTS[k]
                elif k in DERIVED_INPUTS:
                    out_dict[k] = DERIVED_INPUTS[k]
    
    # Generate Output JSON
    recursive_dict_traversal(OUTPUT_FIELDS, OUTPUT_JSON)

    return OUTPUT_JSON

# Run Code