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
import warnings
import csv
from numpy import average
import pandas as pd
from datetime import datetime

with warnings.catch_warnings():
    warnings.simplefilter(action = "ignore", category = FutureWarning)

print("Welcome to a data processing application to find records of accidents\n")
print("that occurred in the U.S. from 2016 to 2021.\n")
print("You will need to load (1) the information first and then (2) Process\n")
print("it before you can perform any searches on the data.")

print("************************************")
# Define global set here
df = 0

def loadData():
    print("Loading and cleaning input data set:")
    print("************************************")
    # Dataset = pd.read_csv("./Datasets/InputDataSample.csv")
    print('[', datetime.now(), '] Starting Script')
    Dataset = pd.read_csv("US_Accidents_data.csv")
    global df
    df = pd.DataFrame(Dataset)
    totalData = len(df)
    print(totalData)

# CLEAN DATA
def processData():
    # Drop rows with missing data from any of the specified columns
    global df
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
    return df


    #**************************************
    # starting functions that answer the questions
    # 1. In what month were there more accidents reported?
def prompt1():
    print("Prompt 1")
    months = df['month'] = pd.DatetimeIndex(df['Start_Time']).month
    print(months.value_counts().head(1))

# 2. What is the state that had the most accidents in 2020?
def prompt2():
    print("Prompt 2")
    years = df['years'] = pd.DatetimeIndex(df['Start_Time']).year
    acc2020 = df[years == 2020]
    state2020 = acc2020['State'].value_counts().head(1)
    print(state2020)

# 3. What is the state that had the most accidents of severity 2 in 2021?
def prompt3():
    print("Prompt 3")
    years = df['years'] = pd.DatetimeIndex(df['Start_Time']).year
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
def prompt4():
    print("Prompt 4")
    stateVirginia = df['State'] == "VA"
    virginiaColumns = df[stateVirginia]
    virginiaSeverity = virginiaColumns['Severity'].value_counts().head()
    print(virginiaSeverity)

# 5. What are the 5 cities that had the most accidents in 2019 in California?
def prompt5():
    print("Prompt 5")
    years = df['years'] = pd.DatetimeIndex(df['Start_Time']).year
    stateCalifornia = df['State'] == "CA"
    acc2019 = df[years == 2019]
    # print(acc2019)
    caliAccidents2019 = acc2019[stateCalifornia]
    topCaliforniaCities = caliAccidents2019['City'].value_counts().head() 
    print(topCaliforniaCities)

# 6. What was the average humidity and average temperature of all accidents of 
# severity 4 that occurred in 2021?
def prompt6():
    print("Prompt 6")
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
    print('average humidity: ', humiditySevFour)
    print('average temp: ', tempSevFour)

# 7. What are the 3 most common weather conditions (weather_conditions) when accidents occurred?
def prompt7():
    print("Prompt 7")
    weatherConditions = df['Weather_Condition'].value_counts().head(3) 
    print(weatherConditions)

# 8. What was the maximum visibility of all accidents of severity 2 that occurred in the state of New Hampshire?
def prompt8():
    print("Prompt 8")
    stateNewHampshire = df['State'] == "NH"
    tempDF = df[stateNewHampshire]
    severity = df['Severity'] == 2
    stateSeverity = tempDF[severity]
    visibility = stateSeverity['Visibility(mi)'].max()
    # print(df)
    print("The maximum visibility of all accidents of severity 2 that occurred in the state of New Hampshire:")
    print(visibility)

# 9. How many accidents of each severity were recorded in Bakersfield?
def prompt9():
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
def searchByCity():
    print("Please type the name of the city you would like to search.\n") 
    cityChoice = input()
    cityChoiceAccidents  = df['City'] == cityChoice
    cityTmpDF = df[cityChoiceAccidents]
    cityTotalAccidents = len(cityTmpDF)
    if (cityTotalAccidents == 0):
        while cityTotalAccidents  == 0:
            print("Your selection has no entries. Either your city ")
            print("choice has very safe drivers or there is a spelling mismatch.")  
            print("\nPlease try again, make sure to capitalize the ")
            print("first letter. If you meant to search by state or zip type NA") 
            cityChoice = input()
            if(cityChoice == 'NA'):
                break
            cityChoiceAccidents  = df['City'] == cityChoice
            cityTmpDF = df[cityChoiceAccidents]
            cityTotalAccidents = len(cityTmpDF)

    if (cityChoice != 'NA'):
        print("The number of accidents in " + cityChoice + " was: ")
        print(cityTotalAccidents)

def searchByState():
    print("Please type the name of the state you would like to search.\n") 
    stateChoice = input("Use USPS abbreviations i.e. CA")
    stateChoiceAccidents  = df['State'] == stateChoice
    stateTmpDF = df[stateChoiceAccidents]
    stateTotalAccidents = len(stateTmpDF)
    if (stateTotalAccidents == 0):
        while stateTotalAccidents  == 0:
            print("Your selection has no entries. Either your state ")
            print("choice has very safe drivers or there is a spelling mismatch.")  
            print("\nPlease try again, use USPS state abbreviations i.e. CA.")
            print("Type: NA, if you want to go back.")
            stateChoice = input()
            if(stateChoice == 'NA'):
                break
            stateChoiceAccidents  = df['State'] == stateChoice
            stateTmpDF = df[stateChoiceAccidents]
            stateTotalAccidents = len(stateTmpDF)
    
    if(stateChoice != 'NA'):
        print("The total number of accidents in " + stateChoice + " is: ",stateTotalAccidents)

def searchByZip():
    print("Please type the 5 digit zip code you want to search.")
    zipChoice = input()
    zipChoiceAccidents  = df['Zipcode'] == zipChoice
    zipTmpDF = df[zipChoiceAccidents]
    zipTotalAccidents = len(zipTmpDF)
    if (zipTotalAccidents == 0):
        while zipTotalAccidents  == 0:
            print("Your selection has no entries. Either your zip code")
            print("choice has very safe drivers or the zip code you entered does not ")
            print("\n exist. Please try again, or type: NA, to go back.")
            zipChoice = input()
            if(zipChoice == 'NA'):
                break
            zipChoiceAccidents  = df['Zipcode'] == zipChoice
            zipTmpDF = df[zipChoiceAccidents]
            zipTotalAccidents = len(zipTmpDF)

    if (zipChoice != 'NA'):
        print("The number of accidents in " + zipChoice + " was: ")
        print(zipTotalAccidents)

def  searchAccidentsPlace():
    exit = False
    while(exit == False):
        print("Please enter the number of a prompt from the following menu:")
        print("1: Search by city")
        print("2:Search by state")
        print("3: Search by zip code")
        print("4: Exit this menu")
        action = input()
        if(action =='1'):
            searchByCity()
            return False
        if(action =='2'):
            searchByState()
            return False
        if(action =='3'):
            searchByZip()
            return False
        if(action =='4'):
            return True
        else:
            print("Error: Invalid input. Please try again.")
            return False

def searchByMonth(monthChoice):
    if(monthChoice == 'NA'):
        return df
##**** need help with te following search
    monthChoiceAccidents = df['Month'] = pd.DatetimeIndex(df['Start_Time']).month == monthChoice
    monthTmpDF = df[monthChoiceAccidents]
    monthTotalAccidents = len(monthTmpDF)
    if (monthTotalAccidents == 0):
        while monthTotalAccidents  == 0:
            print("Your selection has no entries. Please type a number 1-12\n")
            print("or type: NA, to avoid limiting your selection by a month")
            monthChoice = input()
            if(monthChoice == 'NA'):
                monthTmpDF = df
                break
            monthTmpDF = df[monthChoiceAccidents]
            monthTotalAccidents = len(monthTmpDF)
    return monthTmpDF

############################################################################
def searchByDay(currentDF,dayChoice):
    if(dayChoice == 'NA'):
        return currentDF
### need help with following line
    dayChoiceAccidents = df['day'] = pd.DatetimeIndex(df['Start_Time']).day == dayChoice
    dayTmpDF = currentDF[dayChoiceAccidents]
    dayTotalAccidents = len(dayTmpDF)
    if (dayTotalAccidents == 0):
        while dayTotalAccidents  == 0:
            print("Your selection has no entries. Please type a number 1-31\n")
            print("or type: NA, to avoid limiting your selection by a day")
            dayChoice = input()
            if(dayChoice == 'NA'):
                dayTmpDF = df
                break
            dayTmpDF = df[dayChoiceAccidents]
            dayTotalAccidents = len(dayTmpDF)
    return dayTmpDF

############################################################################
def searchByYear(currentDF, yearChoice):
    if(yearChoice == 'NA'):
        return currentDF
### need help with following line
    yearChoiceAccidents = df['year'] = pd.DatetimeIndex(df['Start_Time']).year == yearChoice
    yearTmpDF = df[yearChoiceAccidents]
    yearTotalAccidents = len(yearTmpDF)
    if (yearTotalAccidents == 0):
        while yearTotalAccidents  == 0:
            print("Please type a number 2016 to 2021\n")
            print("or type: NA, to avoid limiting your selection by a year")
            yearChoice = input()
            if(yearChoice == 'NA'):
                yearTmpDF = df
                break
            yearTmpDF = df[yearChoiceAccidents]
            yearTotalAccidents = len(yearTmpDF)
    return yearTmpDF

def searchAccidentsTime():
    print("You will be given the opportunity to search by month, day, and year.\n")
    print("If you only want to limit your search by one or two factors,  \n")  
    print("type: NA, when given those options.")
    month = input("Please type the month: ")
    monthDF = searchByMonth(month)
    answer = len(monthDF)
    print("the answer is: ",answer) 

    day = input("Please type the day: ")
    dayDF = searchByDay(monthDF, day)
    answer = len(dayDF)
    print("the answer is: ",answer) 
    year = input("Please type the year you would like to search") 
    yearDF = searchByYear(dayDF, year)
    answer = len(yearDF)
    print("the answer is: ",answer) 

def searchAccidentsCondition():
    minTemp = input("input the lowest temperture of the range")
    maxTemp = input("input the highest temperture of the range")
    minVisibility = input("input the lowest visibility of the range")
    maxVisibility = input("input the  farthest visibility of the range")
    tempAndVis = df['Temperature(F)'] > minTemp
    tempAndVis = tempAndVis['Temperature(F)'] < maxTemp
    tempAndVis = tempAndVis['Visibility(mi)'] < maxVisibility
    tempAndVis = tempAndVis['Visibility(mi)'] > minVisibility
    totalInRange = len(tempAndVis)
    print("The number of accidents in specified tempature and visibility range is: ")
    print(totalInRange)

def menu_selection(action):

    try:
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
    except:
        print("Error: Invalid input. Please try again.")
        return False

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
        try:
            action = input()
            exit = menu_selection(action)
        except:
            print("An error has occurred. Please check that data is loaded and try again")
# start of main program
main()
