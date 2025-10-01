"""
Stream lit GUI for hosting AutoUI
"""

# Imports
import os
import json
import streamlit as st

import AutoUI

# Main Vars
config = json.load(open("./StreamLitGUI/UIConfig.json", "r"))

# Main Functions
def main():
    # Create Sidebar
    selected_box = st.sidebar.selectbox(
    "Choose one of the following",
        tuple(
            [config["PROJECT_NAME"]] + 
            config["PROJECT_MODES"]
        )
    )
    
    if selected_box == config["PROJECT_NAME"]:
        HomePage()
    else:
        correspondingFuncName = selected_box.replace(" ", "_").lower()
        if correspondingFuncName in globals().keys():
            globals()[correspondingFuncName]()
 

def HomePage():
    st.title(config["PROJECT_NAME"])
    st.markdown("Github Repo: " + "[" + config["PROJECT_LINK"] + "](" + config["PROJECT_LINK"] + ")")
    st.markdown(config["PROJECT_DESC"])
    # st.write(open(config["PROJECT_README"], "r").read())

#############################################################################################################################
# Repo Based Vars
PATHS = {
    "cache": "StreamLitGUI/CacheData/Cache.json",
    "defaults": {
        "ui_config": "StreamLitGUI/DefaultData/ui_config_default.json"
    }
}

# Util Vars
CACHE = {}

# Util Functions
def LoadCache():
    '''
    Load Cache
    '''
    global CACHE
    CACHE = json.load(open(PATHS["cache"], "r"))

def SaveCache():
    '''
    Save Cache
    '''
    global CACHE
    json.dump(CACHE, open(PATHS["cache"], "w"), indent=4)

# Main Functions


# UI Functions


# Repo Based Functions
def auto_json_output_ui():
    # Title
    st.title("Auto JSON Output UI")

    # Prereq Loaders

    # Load Inputs
    st.header("Upload UI Config JSON")
    USERINPUT_UIConfig = st.file_uploader("Upload UI Config JSON", type=["json"])
    if USERINPUT_UIConfig is None: USERINPUT_UIConfig = open(PATHS["defaults"]["ui_config"], "r")
    UIConfig = json.load(USERINPUT_UIConfig)
    USERINPUT_UIConfigStr = st.text_area("UI Config JSON", value=json.dumps(UIConfig, indent=8), height=300)
    UIConfig = json.loads(USERINPUT_UIConfigStr)

    # Process Inputs
    st.header("Generated UI")
    USER_INPUTS = AutoUI.AutoUI_InputUI(UIConfig)
    DERIVED_INPUTS = AutoUI.AutoUI_GenerateDerivedFields(UIConfig, USER_INPUTS)
    OUTPUT_JSON = AutoUI.AutoUI_OutputJSON(UIConfig, USER_INPUTS, DERIVED_INPUTS)

    # Display Outputs
    st.header("Outputs")
    st.subheader("User Inputs")
    st.json(USER_INPUTS, expanded=True)

    st.subheader("Derived Inputs")
    st.json(DERIVED_INPUTS, expanded=True)

    st.subheader("Output JSON")
    st.json(OUTPUT_JSON, expanded=True)
    st.download_button(
        label="Download Output JSON",
        data=json.dumps(OUTPUT_JSON, indent=4),
        file_name="output.json",
        mime="application/json"
    )
#############################################################################################################################
# Run Code
if __name__ == "__main__":
    main()