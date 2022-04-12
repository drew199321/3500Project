############################################################################
# Course: CMPS 3500
# CLASS Project Group 9
# PYTHON IMPLEMENTATION: BASIC DATA ANALYSIS
# Date: 04/7/2022
# Student 1: Zachary Scholefield
# Student 2: Clemente Rodriguez Jr
# Student 4: Andrew Manz
# Student 4: Scott Kurtz
# Description: Implementation Basic Data Analysys Routines
############################################################################

import csv
import pandas as pd
from datetime import datetime

print("Loading and cleaning input data set:")
print("************************************")
# Dataset = pd.read_csv("./Datasets/InputDataSample.csv")
print('[', datetime.now(), '] Starting Script')
print('[', datetime.now(), '] Loading US_Accidents_data.csv')

# Read CSV file
# Dataset = pd.read_csv("./Datasets/testing.csv")
Dataset = pd.read_csv("./Datasets/US_Accidents_data.csv")
df = pd.DataFrame(Dataset)
# df.isnull()
# Dataset = pd.read_csv("./Datasets/Loading US_Accidents_data.csv")

############################################################################
# CLEAN DATA
############################################################################

# Drop rows with missing data from any of the specified columns
dropRowsSingle = df.dropna(subset=['ID', 'Severity', 'Zipcode', 'Start_Time',
'End_Time', 'Visibility(mi)', 'Weather_Condition', 'Country'], inplace=True) 

# Drop Rows missing 3 columns
dropRowsTriple = df.dropna(thresh=len(df.columns)-3, inplace=True)

# Drop Rows where Distance = 0
dropRowsDistance = df.drop(df.loc[df['Distance(mi)'] == 0].index)

# df['Start_Time'] = pd.to_datetime(df['Start_Time'])
# df['End_Time'] = pd.to_datetime(df['End_Time'])


print(dropRowsSingle, dropRowsTriple, dropRowsDistance)

# Only consider the first 5 digits of zipcode
zipCoder = df['Zipcode'].str[:5]
# Tested with index 21 with zipcode: 41033-9698; output: 41033
print(zipCoder[21])

                
print ("DONE!")
