���      �PythonCodeTokenizer��Code���)��}�(�	code_path��TestCodes/rtocsv.py��
code_lines�]�(�'''
��Test By Hrishikesh
��'''
��
��import pandas as pd
��import pyreadr as prr
�h�	# Params
��file1_path = 'gapminder.rdata'
��data_key = 'gapminder'
�� out_file_path = 'gapminder.csv'
��	# Params
�h�file1=prr.read_r(file1_path)
��# file2=pd.to_csv(file1)
��# print(file1.keys())
��df1 = file1[data_key]
��# print(df1)
��df=pd.DataFrame(df1)
��df.to_csv(r'gapminder.csv')
��!file2=pd.read_csv(out_file_path)
��print (file2)�e�script_desc��Test By Hrishikesh��imports�]�(�import pandas as pd��import pyreadr as prr�e�classes�]��	functions�]��script_parameters�]�(h �ScriptParameter���)��}�(�name��
file1_path��value��gapminder.rdata��value_prefix��'��value_suffix�h2�type��builtins��str����ui_mode�N�	otherData�}�ubh*)��}�(h-�data_key�h/�	gapminder�h1h2h3h2h4h7h8Nh9}�ubh*)��}�(h-�out_file_path�h/�gapminder.csv�h1h2h3h2h4h7h8Nh9}�ube�driver_code�]�(�file1=prr.read_r(file1_path)��# file2=pd.to_csv(file1)��# print(file1.keys())��df1 = file1[data_key]��# print(df1)��df=pd.DataFrame(df1)��df.to_csv(r'gapminder.csv')�� file2=pd.read_csv(out_file_path)�heub.