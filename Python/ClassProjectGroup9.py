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
print("Hello")
df = pd.DataFrame(Dataset)
# df.isnull()
# Dataset = pd.read_csv("./Datasets/Loading US_Accidents_data.csv")

df = df.dropna(subset=['ID', 'Severity', 'Zipcode', 'Start_Time',
'End_Time', 'Visibility(mi)', 'Weather_Condition', 'Country'])

print(df)
# print(df.dropna(subset=['Weather_Condition']))

# print(datetime.now())
                
print ("DONE!")