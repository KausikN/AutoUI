"""
Input Library for AutoUI
"""

# Imports
import streamlit as st

# Main Functions


# Main Vars
INPUT_TYPES = {
    "text_input": st.text_input,
    "text_area": st.text_area,
    "number_input": st.number_input,
    "date_input": st.date_input,
    "time_input": st.time_input,
    "checkbox": st.checkbox,
    "radio": st.radio,
    "selectbox": st.selectbox,
    "multiselect": st.multiselect,
    "slider": st.slider,
    "file_uploader": st.file_uploader,
    "color_picker": st.color_picker
}