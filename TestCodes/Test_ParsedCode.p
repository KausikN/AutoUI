���      �PythonCodeTokenizer��Code���)��}�(�	code_path��TestCodes/Test.py��
code_lines�]�(�'''
��Script Description
��'''
��
��
# Imports
��import numpy as np
�h�# Main Functions
��def Sum(a, b):
��    if a == None:
��        return '1'
��    return a+b
��#FEND
��def Diff(a, b):
��    return a-b
��#FEND
��def Mult(a, b):
��    return a*b
��#FEND
��def AND(a, b):
��    return a and b
��#FEND
��def POWER(a, b):
��    return a**b
��#FEND
�h�# Driver Code
��	# Params
��IntVal = -10
��BoolVal = False
��StrVal = "Hi!"
��FloatVal = -12213.1313
��ADropDownVal = '' #TYPE: SELECTVAL NOTYPE Sum,Diff,Mult,AND,POWER
�� ImageVal = '' #TYPE: FILE Image
��TextVal = '' #TYPE: FILE Text
��FileVal = '' #TYPE: FILE
��(ListVal = [1, '2', 3.0, True] #SIZE 1,5
��	# Params
��print("Inputs:")
��print("IntVal:", IntVal)
��print("BoolVal:", BoolVal)
��print("StrVal:", StrVal)
��print("FloatVal:", FloatVal)
��#print("DropDownVal:", DropDownVal)
��print("ImageVal:", ImageVal)
��print("TextVal:", TextVal)
��print("FileVal:", FileVal)
��print("ListVal:", ListVal)
��StrSum = Sum(StrVal, StrVal)
��IntDiff = Diff(IntVal, 0)
��%FloatMult = Mult(FloatVal, FloatVal)
�� BoolAND = AND(BoolVal, BoolVal)
��&DropdownPOWER = POWER(IntVal, IntVal)
��print("Outputs:")
��print("SUM:", StrSum)
��print("DIFF:", IntDiff)
��print("MULT", FloatMult)
��print("AND", BoolAND)
��'print("DROPDOWN POWER:", DropdownPOWER)�e�script_desc��Script Description��imports�]��import numpy as np�a�classes�]��	functions�]�(h �Function���)��}�(�name�� Sum��desc�� ��
parameters�]�(�a��b�e�code�]�(�    if a == None:��        return '1'��    return a+b�eubhL)��}�(hO� Diff�hQhRhS]�(hUhVehW]��    return a-b�aubhL)��}�(hO� Mult�hQhRhS]�(hUhVehW]��    return a*b�aubhL)��}�(hO� AND�hQhRhS]�(hUhVehW]��    return a and b�aubhL)��}�(hO� POWER�hQhRhS]�(hUhVehW]��    return a**b�aube�script_parameters�]�(h �ScriptParameter���)��}�(hO�IntVal��value�J�����value_prefix�hR�value_suffix�hR�type��builtins��int����ui_mode�N�	otherData�}�ubhw)��}�(hO�BoolVal�h{�h|hRh}hRh~h�bool���h�Nh�}�ubhw)��}�(hO�StrVal�h{�Hi!�h|�"�h}h�h~h�str���h�Nh�}�ubhw)��}�(hO�FloatVal�h{G��ڐ�p:�h|hRh}hRh~h�float���h�Nh�}�ubhw)��}�(hO�DropDownVal�h{]�(�Sum��Diff��Mult��AND��POWER�eh|hRh}hRh~h�h��	SELECTVAL�h�}�ubhw)��}�(hO�ImageVal�h{hRh|�'�h}h�h~h�h��FILE�h�}��ext�]�(�.png��.jpg��.jpeg��.bmp��.JPG��.PNG�esubhw)��}�(hO�TextVal�h{hRh|h�h}h�h~h�h�h�h�}�h�]�(�.txt��.md��.py��.c��.cpp��.js��.html��.htm��.css�esubhw)��}�(hO�FileVal�h{hRh|h�h}h�h~h�h�h�h�}�ubhw)��}�(hO�ListVal�h{]�(hw)��}�(hO�0�h{Kh|hRh}hRh~h�h�Nh�}�ubhw)��}�(hO�1�h{�2�h|h�h}h�h~h�h�Nh�}�ubhw)��}�(hO�2�h{G@      h|hRh}hRh~h�h�Nh�}�ubhw)��}�(hO�3�h{�h|hRh}hRh~h�h�Nh�}�ubeh|�[�h}�]�h~�LIST�h�h�h�}��	sizeRange�]�(KKesube�driver_code�]�(�# Driver Code��print("Inputs:")��print("IntVal:", IntVal)��print("BoolVal:", BoolVal)��print("StrVal:", StrVal)��print("FloatVal:", FloatVal)��"print("DropDownVal:", DropDownVal)��print("ImageVal:", ImageVal)��print("TextVal:", TextVal)��print("FileVal:", FileVal)��print("ListVal:", ListVal)��StrSum = Sum(StrVal, StrVal)��IntDiff = Diff(IntVal, 0)��$FloatMult = Mult(FloatVal, FloatVal)��BoolAND = AND(BoolVal, BoolVal)��%DropdownPOWER = POWER(IntVal, IntVal)��print("Outputs:")��print("SUM:", StrSum)��print("DIFF:", IntDiff)��print("MULT", FloatMult)��print("AND", BoolAND)�hAeub.