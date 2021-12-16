# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 17:46:33 2021
take a sheet with event logs from the event viewer and compare different PCs
@author: stjse
"""

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

os.chdir("D:\\OneDrive\\OneDrive\\Python\\shutdowns\\")
# df = pd.read_excel("source\\shutdown_table.xlsx")
excelfile = pd.ExcelFile("source\\shutdown_table.xlsx")
# =============================================================================
# df = pd.read_excel('Shutdowns.xlsx', sheet_name = None, header=None)
# =============================================================================
df = pd.DataFrame()
for i, sheet in enumerate(excelfile.sheet_names):
    print(sheet)
    temp_df =  excelfile.parse(sheet_name = sheet, header=None)
    temp_df["PC"] = sheet
    temp_df["PCnum"] = i
    df = pd.concat([df, temp_df])

df.columns = ['Level', 'DateAndTime', 'Source', 'EventID', 'TaskCategory', 'PC', 'PCnum']

days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]

df['Weekday'] = df['DateAndTime'].dt.dayofweek
df['WeekdayName'] = df['Weekday'].apply(lambda x : days[x]) 

df.reset_index(drop=True, inplace=True)

# simple scatter plot of the PCs by name over time
plt.scatter(x=df['DateAndTime'], y=df['PC'])

# simple cdf of all PCs over time
PC_names = df['PC'].unique()
dfs = {}
for name in PC_names:
    dfs[name] = df[df['PC'] == name]
f, ax = plt.subplots(figsize=(8, 8))
for name, entries_df in dfs.items():
    ax = sns.kdeplot(entries_df['DateAndTime'], cumulative=True)
    
# hist plot over weekdays
for name, entries_df in dfs.items():
    ax = sns.kdeplot(entries_df['DateAndTime'], cumulative=True)
    
    
# Create histogram over weekdays
fig, ax = plt.subplots(figsize=(10,4))
sns.histplot(data=df, x='Weekday', hue='PCnum', multiple='dodge', discrete=True,
             edgecolor='white', palette=plt.cm.Accent, alpha=1)
# Additional formatting
sns.despine()
ax.get_legend().set_frame_on(False)
    
    
