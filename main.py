# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 17:46:33 2021
take a sheet with event logs from the event viewer and compare different PCs
@author: stjse
"""

import pandas as pd
import os
os.chdir("D:\\OneDrive\\OneDrive\\Python\\shutdowns\\")
# df = pd.read_excel("source\\shutdown_table.xlsx")
excelfile = pd.ExcelFile("source\\shutdown_table.xlsx")
# =============================================================================
# df = pd.read_excel('Shutdowns.xlsx', sheet_name = None, header=None)
# =============================================================================
df = pd.DataFrame()
for sheet in excelfile.sheet_names:
    print(sheet)
    temp_df =  excelfile.parse(sheet_name = sheet, header=None)
    temp_df["PC"] = sheet
    df = pd.concat([df, temp_df])
df.columns = ['Level', 'DateAndTime', 'Source', 'EventID', 'TaskCategory', 'PC']
df.reset_index(drop=True, inplace=True)

