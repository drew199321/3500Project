############################################################################
# Course: CMPS 3500
# CLASS Project Group 9
# PYTHON IMPLEMENTATION: BASIC DATA ANALYSIS
# Date: 04/7/2022
# Student 1: Zachary Scholefield
# Student 2: Clemente Rodriguez Jr
# Student 3: Andrew Manz
# Student 4: Scott Kurtz
# Description: Implementation Basic Data Analysys Routines
############################################################################

# from asyncio.windows_events import NULL
import sys
import warnings
import csv
from numpy import average
import pandas as pd
from datetime import datetime

import warnings
warnings.filterwarnings("ignore")

print("\nWelcome to a data processing application to find records of \n"
    "accidents that occurred in the U.S. from 2016 to 2021.\n\n"
    "> You will need to (1) load the information first and then\n"
    "> (2) Process the data before you can search.\n"
    "*****************************************************************")
# Define global set here
df = 0

def loadData():
    print("Loading and cleaning input data set:")
    print("************************************")
    # Dataset = pd.read_csv("./Datasets/InputDataSample.csv")
    print('[', datetime.now(), '] Starting Script')
    global df
    df = pd.read_csv("US_Accidents_data.csv")

    # df = pd.DataFrame(Dataset)
 
    print(len(df))

# CLEAN DATA
def processData():
    # Drop rows with missing data from any of the specified columns
    global df
    df.dropna(subset=['ID', 'Severity', 'Zipcode', 'Start_Time',
    'End_Time', 'Visibility(mi)', 'Weather_Condition', 'Country'], inplace=True) 

    # Drop Rows missing 3 columns
    df.dropna(thresh=len(df.columns)-2, inplace=True)

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
    print(len(df))
    return df


    #**************************************
    # starting functions that answer the questions
    # 1. In what month were there more accidents reported?
def prompt1():
    print("Prompt 1:")
    months = df['month'] = pd.DatetimeIndex(df['Start_Time']).month
    month = months.value_counts()[:1].index.to_list()
    print(f"The month with the most accidents is: {month[0]}\n")

# 2. What is the state that had the most accidents in 2020?
def prompt2():
    print("Prompt 2:")
    years = df['years'] = pd.DatetimeIndex(df['Start_Time']).year
    acc2020 = df[years == 2020]
    state2020 = acc2020['State'].value_counts()[:1].index.to_list()
    print(f"The state with the most accidents in the year 2020 is: {state2020}\n")

# 3. What is the state that had the most accidents of severity 2 in 2021?
def prompt3():
    print("Prompt 3:")
    years = df['years'] = pd.DatetimeIndex(df['Start_Time']).year
    acc2021 = df[years == 2021]
    severity2 = acc2021['Severity'] == 2
    # print(type(severity2))
    # print(type(acc2021))

    state1 = acc2021[severity2]
    state2 = state1['State'].value_counts()[:1].index.to_list()
   
    print(f"The state with the most accidents of severity 2 in 2021 is: {state2}\n")


# 4. What severity is the most common in Virginia?
def prompt4():
    print("Prompt 4")
    stateVirginia = df['State'] == "VA"
    virginiaColumns = df[stateVirginia]
    virginiaSeverity = virginiaColumns['Severity'].value_counts()[:1].index.to_list()
    print(f"The most common severity in Virginia is: {virginiaSeverity}\n")

# 5. What are the 5 cities that had the most accidents in 2019 in California?
def prompt5():
    print("Prompt 5")
    years = df['years'] = pd.DatetimeIndex(df['Start_Time']).year
    stateCalifornia = df['State'] == "CA"
    acc2019 = df[years == 2019]
    # print(acc2019)
    caliAccidents2019 = acc2019[stateCalifornia]
    topCaliforniaCities = caliAccidents2019['City'].value_counts().head() 
    print(f"The 5 cities in California that had the most accidents in 2019 are:\n{topCaliforniaCities}\n")

# 6. What was the average humidity and average temperature of all accidents of 
# severity 4 that occurred in 2021?
def prompt6():
    print("Prompt 6:")
    years = df['years'] = pd.DatetimeIndex(df['Start_Time']).year
    acc2021 = df[years == 2021]
    # Severity of 4
    severityFour = df['Severity'] == 4
    # Severity of 4 in 2021
    yearAndSeverity = acc2021[severityFour]
    # Humidity of severity 4 accidents in 2021
    humiditySevFour = yearAndSeverity['Humidity(%)'].mean()
    # Temperature of severity 4 accidents in 2021
    tempSevFour = yearAndSeverity['Temperature(F)'].mean()

    # average temperature and humidity for accidents w/ a severity of 4 in 2021
    print("For accidents with severity 4 that occured in 2021: ")
    print('average humidity: ', humiditySevFour)
    print('average temp: ', tempSevFour, "\n")

# 7. What are the 3 most common weather conditions (weather_conditions) when accidents occurred?
def prompt7():
    print("Prompt 7:")
    print("The 3 most common weather conditions are: ")
    weatherConditions = df['Weather_Condition'].value_counts().head(3) 
    print(weatherConditions, "\n")

# 8. What was the maximum visibility of all accidents of severity 2 that occurred in the state of New Hampshire?
def prompt8():
    print("Prompt 8:")
    stateNewHampshire = df['State'] == "NH"
    tempDF = df[stateNewHampshire]
    severity = df['Severity'] == 2
    stateSeverity = tempDF[severity]
    visibility = stateSeverity['Visibility(mi)'].max()
    # print(df)
    print(f"The maximum visibility of all accidents of severity 2 that occurred in the state of New Hampshire: {visibility}\n")
    # print(visibility)

# 9. How many accidents of each severity were recorded in Bakersfield?
def prompt9():
    print("Prompt 9:")
    bakersfield = df['City'] == "Bakersfield"
    severityBak1 = df['Severity'] == 1
    severityBak2 = df['Severity'] == 2
    severityBak3 = df['Severity'] == 3
    severityBak4 = df['Severity'] == 4

    tmpDF = df[bakersfield]

    # print(df)
    # print(severityBak1)
    # print(type(severityBak1))
    # print(type(tmpDF))

    bakersfieldSev1 = len(tmpDF[severityBak1])
    bakersfieldSev2 = len(tmpDF[severityBak2])
    bakersfieldSev3 = len(tmpDF[severityBak3])
    bakersfieldSev4 = len(tmpDF[severityBak4])

    # print(type(bakersfieldSev1))
    print("Accidents in Bakersfield with Severity 1: ", bakersfieldSev1)
    print("Accidents in Bakersfield with Severity 2: ", bakersfieldSev2)
    print("Accidents in Bakersfield with Severity 3: ", bakersfieldSev3)
    print("Accidents in Bakersfield with Severity 4: ", bakersfieldSev4)

# 10 What was the longest accident (in hours) recorded in Florida in the Spring (March, April, and May) of 2020?
def prompt10():
    print("10. What was the longest accident (in hours) recorded in Florida in"
        " the Spring (March, April, and May) of 2020?")
    # gather the start, end, and state from the dataset
    longest_acc_fl = df.loc[:, ('Start_Time', 'End_Time', 'State')]
    # get state: Florida
    longest_acc_fl = longest_acc_fl[longest_acc_fl['State'] == "FL"]
    # get year: 2020
    longest_acc_fl = longest_acc_fl[longest_acc_fl['Start_Time'].dt.year == 2020]
    # print(longest_acc_fl[longest_acc_fl['Start_Time'].dt.year == 2020])
    # get months greater than February
    longest_acc_fl = longest_acc_fl[longest_acc_fl['Start_Time'].dt.month >= 3]
    # get months less than June
    longest_acc_fl = longest_acc_fl[longest_acc_fl['Start_Time'].dt.month <= 5]
    # get the data with the most time
    longest_acc_fl = str((longest_acc_fl['End_Time'] - longest_acc_fl['Start_Time']).max())

    # if the year chosen doesn't have any data, it will print an error message
    if (longest_acc_fl == "NaT"):
        time_in_hours = 0
        print("\nError: No Data Loaded meeting this criteria.")
    else:
        # else, we will extrapolate the data from the times
        # hours from days
        days_in_hours = int(longest_acc_fl.split()[0]) * 24 
        # return time of day
        longest_acc_fl = longest_acc_fl.split()[2] 
        time_in_hours = int(longest_acc_fl.split(":")[0]) # split by : 
        # get minutes from the hour
        time_in_min = int(longest_acc_fl.split(":")[1]) / 60 
        # get seconds from hour
        time_in_sec = int(longest_acc_fl.split(":")[2]) / 3600  
        # Add the days, hours, min, and seconds
        time_in_hours = days_in_hours + time_in_hours + time_in_min + time_in_sec
        # round the result for better readability 
        acc_2020_fl = round(time_in_hours, 2)
    # print the solution
    print(acc_2020_fl, "Hours.")

#**************************************
def printAnswers():
    prompt1()
    prompt2()
    prompt3()
    prompt4()
    prompt5()
    prompt6()
    prompt7()
    prompt8()
    prompt9()
    prompt10()

#**************************************
# associated with choice 4 on menu
def searchAccidentsPlace():

    print("Please type the name of the city you would like to search.\n") 
    cityChoice = input()
    if(cityChoice != 'NA'):
        cityChoiceAccidents  = df['City'] == cityChoice
    else: 
        cityChoiceAccidents = df
    cityTmpDF = df[cityChoiceAccidents]
    cityTotalAccidents = len(cityTmpDF)
    print("The number of accidents in " + cityChoice + " was: ")
    print(cityTotalAccidents)

    print("Please type the name of the state you would like to search.\n") 
    stateChoice = input()
    if(stateChoice != 'NA'):
        stateChoiceAccidents  = df['State'] == stateChoice
    else:
        stateChoiceAccidents = df 
    stateTmpDF = df[stateChoiceAccidents]
    stateTotalAccidents = len(stateTmpDF)
    print("The number of accidents in " + stateChoice + " was: ")
    print(stateTotalAccidents)

    print("Please type the zip code you would like to search.\n") 
    zipChoice = input()
    if(zipChoice != 'NA'):
        zipChoiceAccidents  = df['Zipcode'] == zipChoice
    else:        
        zipChoiceAccidents = df
    zipTmpDF = df[stateChoiceAccidents]
    zipTotalAccidents = len(zipTmpDF) 
    print("The number of accidents in " + zipChoice + " was: ")
    print(zipTotalAccidents)



############################################################################
def searchAccidentsTime():
    print("You will be given the opportunity to search by month, day, and year.\n")
    print("If you only want to limit your search by one or two factors,  \n")  
    print("type: NA, when given those options.")

    yearChoice = input("Please type the year: ")
    monthChoice = input("Please type the month(as an integer for which month. E.G. Jan is 1, Feb is 2, etc.): ")
    dayChoice = input("Please type the day: ")
    
    print(type(df['Start_Time'].dt.year))
    if(yearChoice == monthChoice == dayChoice == 'NA'):
        print("Error: All fields entered as NA")
    else:
        if(yearChoice == 'NA'):
            dfYear = df
        else:
            dfYear = df[df['Start_Time'].dt.year.eq(int(yearChoice))]
        if(monthChoice == 'NA'):
            dfMonth = dfYear 
        else:
            dfMonth = dfYear[dfYear['Start_Time'].dt.month.eq(int(monthChoice))]
        if(dayChoice == 'NA'):
            dfDay = dfMonth
        else:
            dfDay = dfDay[dfMonth['Start_Time'].dt.day.eq(int(dayChoice))]

        print("The number of accidents in this timeframe is: ")
        print(len(dfDay))




def searchAccidentsCondition():
    minTemp = float(input("input the lowest temperture of the range"))
    maxTemp = float(input("input the highest temperture of the range"))
    minVisibility = float(input("input the lowest visibility of the range"))
    maxVisibility = float(input("input the  farthest visibility of the range"))
    temperature = df[df['Temperature(F)'].between(minTemp,maxTemp, inclusive=True)]
    # tempAndVis = tempAndVis['Temperature(F)'] < str()
    Visi = temperature[temperature['Visibility(mi)'].between(minVisibility,maxVisibility, inclusive=True)]
    # tempAndVis = tempAndVis['Visibility(mi)'] > str(minVisibility)
    

    print("The number of accidents in specified tempature and visibility range is: ")

    print(len(Visi))

def menu_selection(action):

    #try:
        if(action =='1'):
            loadData()
            return False
        if(action =='2'):
            processData()
            return False
        if(action =='3'):
            printAnswers()
            return False
        if(action =='4'):
            searchAccidentsPlace()
            return False
        if(action =='5'):
            searchAccidentsTime()
            return False
        if(action =='6'):
            searchAccidentsCondition()
            return False
        if(action =='7'):
            return True
    #except:
    #    print("Error: Invalid input. Please try again.")
    #    return False

# definition for main
loaded = False

def main(): 
    # years = df['years'] = pd.DatetimeIndex(df['Start_Time']).year
    global loaded
    exit = False
    while(exit == False):
        print("Please enter the number of a prompt from the following menu:")
        print("1: Load  the data")
        print("2: Process the data")
        print("3: Print the answers to the questions")
        print("4: Search accidents by place (city, state, zip)") 
        print("5: Search accidents by time(year, month, day)")
        print("6: Search accidents by conditions (temperature range and visibility range)")
        print("7: Quit")
    #    try:
        action = str(input())
        exit = menu_selection(action)
    #    except:
    #        print("An error has occurred. Please check that data is loaded and try again")
# start of main program
main()
