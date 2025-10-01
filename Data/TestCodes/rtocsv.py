'''
Test By Hrishikesh
'''

import pandas as pd
import pyreadr as prr

# Params
file1_path = 'gapminder.rdata'
data_key = 'gapminder'
out_file_path = 'gapminder.csv'
# Params

file1=prr.read_r(file1_path)
# file2=pd.to_csv(file1)
# print(file1.keys())
df1 = file1[data_key]
# print(df1)
df=pd.DataFrame(df1)
df.to_csv(r'gapminder.csv')
file2=pd.read_csv(out_file_path)
print (file2)