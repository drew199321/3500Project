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

from asyncio.windows_events import NULL
import csv
from numpy import average
import pandas as pd
from datetime import datetime

print("Loading and cleaning input data set:")
print("************************************")
# Dataset = pd.read_csv("./Datasets/InputDataSample.csv")
print('[', datetime.now(), '] Starting Script')
# print('[', datetime.now(), '] Loading US_Accidents_data.csv')

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
dropRowsTriple = df.dropna(thresh=len(df.columns)-2, inplace=True)

# Drop Rows where Distance = 0
df = df.drop(df.loc[df['Distance(mi)'] == 0].index)

# Drop rows where start and endtime are the same(equal zero)
df['Start_Time'] = pd.to_datetime(df['Start_Time'])
df['End_Time'] = pd.to_datetime(df['End_Time'])
df = df[df['Start_Time'] != df['End_Time']]




# # Only consider the first 5 digits of zipcode

# zipCoder = df['Zipcode'].str[:5]
# # Tested with index 21 with zipcode: 41033-9698; output: 41033
# print(zipCoder[21])

                
print ("CLEANING IS COMPLETE")

############################################################################
# OUTPUT PROMPTS
############################################################################

# 1. In what month were there more accidents reported?
print("Prompt 1")
months = df['month'] = pd.DatetimeIndex(df['Start_Time']).month
print(months.value_counts().head(1))

# 2. What is the state that had the most accidents in 2020?
print("Prompt 2")
years = df['years'] = pd.DatetimeIndex(df['Start_Time']).year
acc2020 = df[years == 2020]

state2020 = acc2020['State'].value_counts().head(1)
print(state2020)

# 3. What is the state that had the most accidents of severity 2 in 2021?
print("Prompt 3")
acc2021 = df[years == 2021]
severity2 = acc2021['Severity'] == 2
print(type(severity2))
print(type(acc2021))

state1 = acc2021[severity2]
state2 = state1['State']
# state2 = severity2[acc2021]
# print(acc2021)
# print(severity2)
# print(state1)
print(state2)
# print(df)


# 4. What severity is the most common in Virginia?
print("Prompt 4")
stateVirginia = df['State'] == "VA"
virginiaColumns = df[stateVirginia]
virginiaSeverity = virginiaColumns['Severity'].value_counts().head()
# print(virginiaColumns)
print(virginiaSeverity)
# print(df)

# 5. What are the 5 cities that had the most accidents in 2019 in California?
print("Prompt 5")
stateCalifornia = df['State'] == "CA"
acc2019 = df[years == 2019]
# print(acc2019)
caliAccidents2019 = acc2019[stateCalifornia]
topCaliforniaCities = caliAccidents2019['City'].value_counts().head() 
print(topCaliforniaCities)

# 6. What was the average humidity and average temperature of all accidents of 
# severity 4 that occurred in 2021?
print("Prompt 6")

# Severity of 4
severityFour = df['Severity'] == 4
# Severity of 4 in 2021
yearAndSeverity = acc2021[severityFour]
# Humidity of severity 4 accidents in 2021
humiditySevFour = yearAndSeverity['Humidity(%)'].mean()
# Temperature of severity 4 accidents in 2021
tempSevFour = yearAndSeverity['Temperature(F)'].mean()

# average temperature and humidity for accidents w/ a severity of 4 in 2021
print('average humidity: ', humiditySevFour)
print('average temp: ', tempSevFour)

# 7. What are the 3 most common weather conditions (weather_conditions) when accidents occurred?
print("Prompt 7")
weatherConditions = df['Weather_Condition'].value_counts().head(3) 
print(weatherConditions)

# 8. What was the maximum visibility of all accidents of severity 2 that occurred in the state of New Hampshire?
print("Prompt 8")
stateNewHampshire = df['State'] == "NH"
tempDF = df[stateNewHampshire]
severity = df['Severity'] == 2
stateSeverity = tempDF[severity]
visibility = stateSeverity['Visibility(mi)'].max()
# print(df)
print(visibility)

# 9. How many accidents of each severity were recorded in Bakersfield?
print("Prompt 9")
bakersfield = df['City'] == "Bakersfield"
severityBak1 = df['Severity'] == 1
severityBak2 = df['Severity'] == 2
severityBak3 = df['Severity'] == 3
severityBak4 = df['Severity'] == 4

tmpDF = df[bakersfield]

print(df)
print(severityBak1)
print(type(severityBak1))
print(type(tmpDF))

bakersfieldSev1 = len(tmpDF[severityBak1])
bakersfieldSev2 = len(tmpDF[severityBak2])
bakersfieldSev3 = len(tmpDF[severityBak3])
bakersfieldSev4 = len(tmpDF[severityBak4])

print(type(bakersfieldSev1))
print(bakersfieldSev1)
print(bakersfieldSev2)
print(bakersfieldSev3)
print(bakersfieldSev4)

# 10 What was the longest accident (in hours) recorded in Florida in the Spring (March, April, and May) of 2022?
print("Prompt 10")



