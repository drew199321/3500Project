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
from sqlite3 import DateFromTicks
import sys
import warnings
import csv
from xml.dom import ValidationErr
from numpy import average
import pandas as pd
from datetime import datetime
import time

# Supress user warnings
warnings.filterwarnings("ignore")

# The ANSI escape codes are used to change colors on screen.
# Welcome Message 
print("\033[1;32m\nWelcome to a data processing application to find records of \n"
        "accidents that occurred in the U.S. from 2016 to 2021.\n\n"
        "You will need to (1) load the information first and then\n"
        "(2) Process the data before you can search.\n"
        "**********************************************************************"
        "***\u001b[0m")
# Define global set here
df = 0
timeToLoad = 0
timeToProcess = 0
timeToPrompt = 0
timeQueryOne = 0
timeQueryTwo = 0
timeQueryThree = 0

# loadData imports csv file and displays total columns read
def loadData():
    start_time = time.time()
    print("\033[1;32mLoading input data set:")
    print("**********************************************\u001b[0m")
    print('[', datetime.now(), '] Starting Script')
    global df
    csv_file = "US_Accidents_data.csv"
    # pandas reads the csv file and is stored in the dataframe
    df = pd.read_csv(csv_file)
    print('[', datetime.now(), '] Loading', csv_file)  
    print('[', datetime.now(), '] Total Columns Read:', len(df.columns)) 
    print('[', datetime.now(), '] Total Rows Read:', len(df))
    end_time = time.time()
    global timeToLoad
    timeToLoad = end_time - start_time
    print ('Time to load is:\u001b[32m', round(timeToLoad, 4), '\u001b[0m'
        'seconds\n')
    return timeToLoad

# processData cleans the data
def processData():
    start_time = time.time()
    # Drop rows with missing data from any of the specified columns
    global df
    print("\033[1;32mProcessing and cleaning input data set:")
    print("******************************************************\u001b[0m")
    print('[', datetime.now(), '] Performing Data Cleanup')

    # drops all rows with data missing in specified columns
    df.dropna(subset=['ID', 'Severity', 'Zipcode', 'Start_Time',
        'End_Time', 'Visibility(mi)', 'Weather_Condition', 'Country'], 
        inplace=True) 

    # Drop Rows missing 3 columns
    df.dropna(thresh=len(df.columns)-2, inplace=True)

    # Drop Rows where Distance = 0
    df = df.drop(df.loc[df['Distance(mi)'] == 0].index)

    # Drop rows where start and endtime are the same(equal zero)
    df['Start_Time'] = pd.to_datetime(df['Start_Time'])
    df['End_Time'] = pd.to_datetime(df['End_Time'])
    df = df[df['Start_Time'] != df['End_Time']]

    # Print the total rows read into the dataframe after clensing 
    print('[', datetime.now(), '] Total Rows Read after cleaning is:', len(df))
    end_time = time.time()
    global timeToProcess
    timeToProcess = end_time - start_time
    print('Time to process is:\u001b[32m', round(timeToProcess, 4), '\u001b[0m'
        'seconds\n')
    return df, timeToProcess

    # Starting functions that answer the questions
    # 1. In what month were there more accidents reported?
def prompt1():
    print('\n\u001b[34mPrompt 1:\u001b[0m')
    months = df['month'] = pd.DatetimeIndex(df['Start_Time']).month
    print('[', datetime.now(), '] In what month were there more accidents '
            'reported?')
    # Get Month of most accidents and convert decimal output to string
    month = months.value_counts()[:1].index.to_list()
    if ({month[0]} == 1):
        print('[', datetime.now(), '] January')
    elif ({month[0]} == 2):
        print('[', datetime.now(), '] February')
    elif ({month[0]} == 3):
        print('[', datetime.now(), '] March')
    elif ({month[0]} == 4):
        print('[', datetime.now(), '] April')
    elif ({month[0]} == 5):
        print('[', datetime.now(), '] May')
    elif ({month[0]} == 6):
        print('[', datetime.now(), '] June')
    elif ({month[0]} == 7):
        print('[', datetime.now(), '] July')
    elif ({month[0]} == 8):
        print('[', datetime.now(), '] August')
    elif ({month[0]} == 9):
        print('[', datetime.now(), '] September')
    elif ({month[0]} == 10):
        print('[', datetime.now(), '] October')
    elif ({month[0]} == 11):
        print('[', datetime.now(), '] November')
    else: 
        print('[', datetime.now(), '] December')

# 2. What is the state that had the most accidents in 2020?
def prompt2():
    print('\n\u001b[34mPrompt 2\u001b[0m')
    print('[', datetime.now(), '] What is the state that had the most '
            'accidents in 2020?')

    # Get years from Start_Time column
    years = df['years'] = pd.DatetimeIndex(df['Start_Time']).year

    # Only gather rows with year equal to 2020
    acc2020 = df[years == 2020]
    
    # Gather the state from State column and pass in the acc2020 for year
    state2020 = acc2020['State'].value_counts()[:1].index.to_list()
    print('[', datetime.now(), ']', state2020)

# 3. What is the state that had the most accidents of severity 2 in 2021?
def prompt3():
    print("\n\u001b[34mPrompt 3:\u001b[0m")
    print('[', datetime.now(), '] What is the state that had the most accidents'  
            'of severity 2 in 2021?')
    # Get Years from Start_Time column
    years = df['years'] = pd.DatetimeIndex(df['Start_Time']).year

    # Gather only rows from 2021 Start_Time
    acc2021 = df[years == 2021]

    # Gather only rows where severity equals 2
    severity2 = acc2021['Severity'] == 2

    # Store severity of 2 from 2021 in state1
    state1 = acc2021[severity2]
    
    # Store state with most accidents in 2021 into state2
    state2 = state1['State'].value_counts()[:1].index.to_list()
    print('[', datetime.now(), ']', state2)
    # print(f"The state with the most accidents of severity 2 in 2021 is: {state2}\n")


# 4. What severity is the most common in Virginia?
def prompt4():
    print("\n\u001b[34mPrompt 4:\u001b[0m")
    print('[', datetime.now(), '] What severity is the most common in Virginia?')
    # Get Viginia from dataframe and store it in stateVirginia
    stateVirginia = df['State'] == "VA"
    virginiaColumns = df[stateVirginia]

    # Get the most severity occurances in virginia
    virginiaSeverity = virginiaColumns['Severity'].value_counts()[:1].index.to_list()
    print('[', datetime.now(), ']', virginiaSeverity)

# 5. What are the 5 cities that had the most accidents in 2019 in California?
def prompt5():
    print("\n\u001b[34mPrompt 5\u001b[0m")
    print('[', datetime.now(), '] What are the 5 cities that had the most'
            'accidents in 2019 in California?')
    
    # Get years from Start_Time
    years = df['years'] = pd.DatetimeIndex(df['Start_Time']).year

    # Get State of California from dataframe and store it in stateCalifornia
    stateCalifornia = df['State'] == "CA"

    # Get the accidents from 2019
    acc2019 = df[years == 2019]
   
    # Store all the accidents from 2019 in California in caliAccidents2019
    caliAccidents2019 = acc2019[stateCalifornia]

    # Will give the top five cities w/ the most accidents
    topCaliforniaCities = caliAccidents2019['City'].value_counts().head() 
    print('[', datetime.now(), ']\n', topCaliforniaCities)

# 6. What was the average humidity and average temperature of all accidents of 
# severity 4 that occurred in 2021?
def prompt6():
    print("\n\u001b[34mPrompt 6:\u001b[0m")
    print('[', datetime.now(), '] What was the average humidity and average'
            'temperature of all accidents of severity 4 that occurred in 2021?')
    
    # Get years from Start_Time Column
    years = df['years'] = pd.DatetimeIndex(df['Start_Time']).year

    # Get number of accidents in 2021
    acc2021 = df[years == 2021]
    
    # Severity of 4
    severityFour = df['Severity'] == 4

    # Severity of 4 in 2021
    yearAndSeverity = acc2021[severityFour]
    
    # Humidity of severity 4 accidents in 2021
    humiditySevFour = yearAndSeverity['Humidity(%)'].mean()
    
    # Temperature of severity 4 accidents in 2021
    tempSevFour = yearAndSeverity['Temperature(F)'].mean()

    # If there is data in the avg temp, give results
    if (pd.isna(tempSevFour) == False):
        print('[', datetime.now(), ']')
        print('Average temp: ', round(tempSevFour, 3))
    # If there is no data, Let the user know.
    else:
        print('[', datetime.now(), '] Unable to Find data for year, severity,'
        'and temperature.')
    # If there is data in the avg humidity, give results
    if (pd.isna(humiditySevFour) == False):
        print('[', datetime.now(), ']')
        print('Average humidity: ', round(humiditySevFour, 3))
    # If there is no data, Let the user know.
    else:
        print('[', datetime.now(), '] Unable to Find data for year, severity,'
        'and humididty.')

# 7. What are the 3 most common weather conditions (weather_conditions) when 
# accidents occurred?
def prompt7():
    print("\n\u001b[34mPrompt 7:\u001b[0m")
    print('[', datetime.now(), '] What are the 3 most common weather conditions'
            '(weather_conditions) when accidents occurred?')

    # Get the top 3 most common weather conditions w/ .head(3) on the dataframe
    weatherConditions = df['Weather_Condition'].value_counts().head(3) 
    print('[', datetime.now(), ']\n', weatherConditions)

# 8. What was the maximum visibility of all accidents of severity 2 that 
# occurred in the state of New Hampshire?
def prompt8():
    print("\n\u001b[34mPrompt 8:\u001b[0m")
    print('[', datetime.now(), '] What was the maximum visibility of all'
            'accidents of severity 2 that occurred in the state of New'
            'Hampshire?')

    # Get New Hampshire from State column            
    stateNewHampshire = df['State'] == "NH"

    # Store it in a temp dataframe
    tempDF = df[stateNewHampshire]

    # Get all accidents w/ severity of 2 
    severity = df['Severity'] == 2

    # Pass severity of 2 into the temp dataframe
    stateSeverity = tempDF[severity]

    # Get the highest visibility from new hampshire w/ severity of 2
    visibility = stateSeverity['Visibility(mi)'].max()
    print('[', datetime.now(), ']', visibility)

# 9. How many accidents of each severity were recorded in Bakersfield?
def prompt9():
    print("\n\u001b[34mPrompt 9:\u001b[0m")
    print('[', datetime.now(), '] How many accidents of each severity were '
            'recorded in Bakersfield?')
    # Get city of bakersfield frome City Column in dataframe
    bakersfield = df['City'] == "Bakersfield"

    # Assign all severity levels to respective variables
    severityBak1 = df['Severity'] == 1
    severityBak2 = df['Severity'] == 2
    severityBak3 = df['Severity'] == 3
    severityBak4 = df['Severity'] == 4

    # Store City of Bakersfield in temp dataframe
    tmpDF = df[bakersfield]

    # Get the number of rows of each severity level in Bakersfield
    bakersfieldSev1 = len(tmpDF[severityBak1])
    bakersfieldSev2 = len(tmpDF[severityBak2])
    bakersfieldSev3 = len(tmpDF[severityBak3])
    bakersfieldSev4 = len(tmpDF[severityBak4])

    # Print Results
    print('[', datetime.now(), ']')
    print("Accidents in Bakersfield with Severity 1: ", bakersfieldSev1)
    print("Accidents in Bakersfield with Severity 2: ", bakersfieldSev2)
    print("Accidents in Bakersfield with Severity 3: ", bakersfieldSev3)
    print("Accidents in Bakersfield with Severity 4: ", bakersfieldSev4)

# 10 What was the longest accident (in hours) recorded in Florida in the Spring (March, April, and May) of 2020?
def prompt10():
    print('\n\u001b[34mPrompt 10:\u001b[0m')
    print('[', datetime.now(), '] What was the longest accident (in hours) recorded in Florida in'
            'the Spring (March, April, and May) of 2020?')

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
    print('[', datetime.now(), ']', acc_2020_fl, 'Hrs\n')
    # print(acc_2020_fl, "Hours.")

# printAnswers will call all the prompt functions and time it
def printAnswers():
    global timeToPrompt
    start_time = time.time()
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
    end_time = time.time()
    timeToPrompt = end_time - start_time
    return timeToPrompt

# Give the user the ability to search for accidents in city, state, and zip
def searchAccidentsPlace():
    global timeQueryOne

    print("\n\u001b[34mYou will be given the opportunity to search by city, "
        "state, or zip code.")
    print("********************************************************************"
        "\u001b[0m")

    # Ask user for city
    print("\n\u001b[36mPlease type the name of the city you would like to"
        " search.\u001b[0m") 
    # Store their input and capitalize the first letter in each word
    cityChoice = input().title()
    
    # Allow user to ommit a choice 
    if(cityChoice != 'NA'):
        start_time = time.time()
        cityChoiceAccidents  = df['City'] == cityChoice
    else: 
        start_time = time.time()
        cityChoiceAccidents = df
    # Get the user's choice and store in temp dataframe
    cityTmpDF = df[cityChoiceAccidents]
    # Get the total rows of accidents in that city
    cityTotalAccidents = len(cityTmpDF)

    # Print results
    print("\nThe number of accidents in \u001b[35m" + cityChoice + "\u001b[0m was:")
    print('\033[1;32m', cityTotalAccidents, '\u001b[0m')
    end_time = time.time()

    # store time to process cityTime
    cityTime = end_time - start_time

    # Prompt user to choose a state
    print("\n\u001b[36mPlease type the name of the state you would like to search."
        "\nFormat: CA, NV, WA, etc.\u001b[0m") 
    
    # Store their choice and convert to uppercase to match dataframe
    stateChoice = input().upper()
    if(stateChoice != 'NA'):
        start_time = time.time()
        stateChoiceAccidents  = df['State'] == stateChoice
    else:
        start_time = time.time()
        stateChoiceAccidents = df 
    
    # store the user's state choice in temp dataframe
    stateTmpDF = df[stateChoiceAccidents]

    # Get total rows of the state choice
    stateTotalAccidents = len(stateTmpDF)

    # Print results
    print("The number of accidents in \u001b[35m" + stateChoice + "\u001b[0m was:")
    print('\033[1;32m',stateTotalAccidents, '\u001b[0m')
    end_time = time.time()
    stateTime = end_time - start_time

    # Prompt user for zipcode
    print("\n\u001b[36mPlease type the zip code you would like to search."
        "\nFormat: 12345\u001b[0m") 
    
    # Store their choice
    zipChoice = input()

    # Allow user to ommit zipcode
    if(zipChoice != 'NA'):
        start_time = time.time()
        zipChoiceAccidents  = df['Zipcode'] == zipChoice
    else:        
        start_time = time.time()
        zipChoiceAccidents = df
    
    # Store their query in temp dataframe
    zipTmpDF = df[zipChoiceAccidents]
    zipTotalAccidents = len(zipTmpDF) 
    print("The number of accidents in \u001b[35m" + zipChoice + "\u001b[0m was:")
    print('\033[1;32m', zipTotalAccidents, '\u001b[0m')
    end_time = time.time()
    zipTime = end_time - start_time

    # Get the acumulated time of the user's location queries
    timeQueryOne = cityTime + stateTime + zipTime
    print("\nTime for location search : \u001b[32m", round(timeQueryOne, 4), 
        '\u001b[0m\n')
    return timeQueryOne

# searchAccidents time will give the total number of accidents in the US on any day 
def searchAccidentsTime():
    global timeQueryTwo
    print("\n\u001b[34mYou will be given the opportunity to search by month, "
        "day, and year.")
    print("If you only want to limit your search by one or two factors,")  
    print("Type: NA, when given those options.")
    print("********************************************************************"
        "\u001b[0m")

    # Get the year from user
    yearChoice = input("\n\u001b[36mPlease type the year between 2016 and 2021: "
        "\u001b[0m")
    
    # Get the month from user
    monthChoice = input("\u001b[36mPlease type the month as integer (Jan is 1,"
        "Feb is 2, etc.): \u001b[0m")

    # Get the day from user
    dayChoice = input("\u001b[36mPlease type the day: \u001b[0m")

    # try / except will make sure all the fields had values
    try:
        if(yearChoice == monthChoice == dayChoice == 'NA'):
            print("\u001b[31mError: All fields entered as NA\u001b[0m")
        else:
            if(yearChoice == 'NA'):
                dfYear = df
                yearTime = 0
            else:
                start_time = time.time()
                dfYear = df[df['Start_Time'].dt.year.eq(int(yearChoice))]
                end_time = time.time()
                yearTime = end_time - start_time
            if(monthChoice == 'NA'):
                dfMonth = dfYear 
                monthTime = 0
            else:
                start_time = time.time()
                dfMonth = dfYear[dfYear['Start_Time'].dt.month.eq(int(monthChoice))]
                end_time = time.time()
                monthTime = end_time - start_time
            if(dayChoice == 'NA'):
                dfDay = dfMonth
                dayTime = 0
            else:
                start_time = time.time()
                dfDay = dfMonth[dfMonth['Start_Time'].dt.day.eq(int(dayChoice))]
                end_time = time.time()
                dayTime = end_time - start_time

            # Get the accumulated time of the users' time query
            timeQueryTwo = dayTime + monthTime + yearTime

            # Format Output based on input
            if (dayChoice != 'NA' and monthChoice != 'NA' and 
                yearChoice != 'NA'):

                # print in mm/dd/yyyy format
                print(f'The number of accidents on \u001b[35m{monthChoice}/' + 
                    f'{dayChoice}/{yearChoice}\u001b[0m is:')
                print('\u001b[32m', len(dfDay), '\u001b[0m\n')
            else:
                # print generic time frame if any field is NA 
                print("The number of accidents in this timeframe is: ")
                print('\u001b[32m', len(dfDay), '\u001b[0m\n')

    except:
        print("An error has occurred. Please enter a valid input and try again.")

# searchAccidentsCondition will find accidents within temp and visibility ranges
def searchAccidentsCondition():
    global timeQueryThree
    # Get minimum temp from user
    minTemp = float(input("\n\u001b[36mInput the lowest temperature of the" 
        " range in \u2109 :\u001b[0m "))

    # Get maximum temp from user
    maxTemp = float(input("\u001b[36mInput the highest temperature of the range "
        " in \u2109 :\u001b[0m "))
    
    # Get minimum visibility from user
    minVisibility = float(input("\u001b[36mInput the lowest visibility of the "
        "range (0-10) in miles:\u001b[0m "))
    
    # Get maximum visibility from user
    maxVisibility = float(input("\u001b[36mInput the farthest visibility of "
        "the range (0-10) in miles:\u001b[0m "))
    start_time = time.time()
    # Get the temp from dataframe
    temperature = df[df['Temperature(F)'].between(minTemp, maxTemp, inclusive=True)]

    # Store the queries in Visi
    Visi = temperature[temperature['Visibility(mi)'].between(minVisibility,maxVisibility, inclusive=True)]
    end_time = time.time() 
    timeQueryThree = end_time - start_time   

    # print results 
    print('\nThe number of accidents with temperature between\u001b[35m', 
        minTemp,'\u2109\u001b[0m  and \u001b[35m', maxTemp,'\u2109\u001b[0m'
            '\nand visibility between\u001b[35m', minVisibility,'mi\u001b[0m  '
            'and \u001b[35m', maxVisibility, 'mi\u001b[0m is:')
    print('\u001b[32m', len(Visi), '\u001b[0m\n')

# menuSelection provides ability to load & process data, see results of prompts
# and search through the dataframe
def menuSelection(action):
    # Define global time variables
    global timeToLoad
    global timeToPrompt
    global timeToProcess
    global timeQueryOne
    global timeQueryTwo
    global timeQueryThree

    # Based on integer input, the user can navigate the options
    try:
        if(action =='1'):
            # load data into the dataframe
            loadData()
            return False
        
        elif(action =='2'):
            # If the user hasn't loaded the data yet, don't process data 
            if(timeToLoad == 0):
                print('\u001b[31m\n!!!PLEASE LOAD DATA BEFORE PROCESSING!!!'
                    '\u001b[0m\n')
            else:
                # Process the data after it's loaded
                processData()
            return False
        elif(action =='3'):
            # If the data hasn't been loaded or processed, don't load prompts
            if(timeToLoad == 0 or timeToProcess == 0):
                print ('\u001b[31m\n!!! PLEASE LOAD AND PROCESS DATA'
                    ' BEFORE LOADING ANSWERS TO PROMPTS!!!\u001b[0m\n')
            else:
                # Load the prompts and print answers
                printAnswers()      
            return False
        elif(action =='4'):
            # If the data hasn't been loaded or processed, don't search
            if(timeToLoad == 0 or timeToProcess == 0):
                print ('\u001b[31m\n!!!PLEASE LOAD AND PROCESS DATA'
                    ' BEFORE SEARCHING CITY, STATE AND ZIP CODE!!!\u001b[0m\n')
            else:
                # Search data for city, state, or Country
                searchAccidentsPlace()
            return False
        elif(action =='5'):
            # If the data hasn't been loaded or processed, don't search
            if(timeToLoad == 0 or timeToProcess == 0):
                print ('\u001b[31m\n!!!PLEASE LOAD AND PROCESS DATA'
                    ' BEFORE SEARCHING YEAR, MONTH AND DAY!!!\u001b[0m\n')
            else:
                # Search data for day, month, year
                searchAccidentsTime()
            return False
        elif(action =='6'):
            if(timeToLoad == 0 or timeToProcess == 0):
                # If the data hasn't been loaded or processed, don't search
                print ('\u001b[31m\n!!! PLEASE LOAD AND PROCESS DATA'
                    ' BEFORE SEARCHING TEMPERATURE RANGE AND VISIBILITY!!!'
                    '\u001b[0m\n')
            else:
                # Search temperature and visibility range
                searchAccidentsCondition()
            return False
        elif(action =='7'):
            # Print the running total of time to process all the data and queries
            totalTime = timeToLoad + timeToProcess + timeToPrompt + timeQueryOne + timeQueryTwo + timeQueryThree
            print('Total Running Time:\u001b[32m', round(totalTime, 4), 
                '\u001b[0mseconds')
            # Exit program
            return True
        else:
            # If the user puts anything but an integer between 1 and 7 throw error
            print("\u001b[31mInvalid input. Please try again.\u001b[0m")
            return False
    except:
        # Throw error if they press CTRL + C
        print("\u001b[31mAn error has occurred. Please check that data is "
            "loaded and try again.\u001b[0m")
        return False

# definition for main
loaded = False

def main(): 

    global loaded
    exit = False
    # Load Menu while until they press 7
    while(exit == False):
        # Menu header
        print("\u001b[35m\n****************************************************"
            "*********************")
        print("*\t\t\t\tMENU\t\t\t\t\t*")
        print("****************************************************************"
            "*********\u001b[0m")
        # Print options
        print("1: Load  the data")
        print("2: Process the data")
        print("3: Print the answers to the questions")
        print("4: Search accidents by place (city, state, zip)") 
        print("5: Search accidents by time(year, month, day)")
        print("6: Search accidents by conditions (temperature range and"
        " visibility range)")
        print("7: Quit")
        try:
            action = str(input())
            exit = menuSelection(action)
        except:
            print("An error has occurred. Please check that data is loaded and"
                " try again")
# start of main program
main()
