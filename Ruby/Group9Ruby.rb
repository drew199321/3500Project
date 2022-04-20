#!/usr/bin/ruby
#! Partially require just CSV Importer
require 'rubygems'
require 'daru'

print ("Loading and cleaning data set: \n")
print ("************************************\n") 
starting = Process.clock_gettime(Process::CLOCK_MONOTONIC)
print("The current time is: ", (starting))
print ("Starting script\n")
print("Performing clean up\n")
df = Daru::DataFrame.from_csv("US_Accidents_data_quick.csv")
print "\n"
# Immediattely drop rows where certain attributes aren't present
df = df.where(!df['ID'].eq(nil))
df = df.where(!df['Severity'].eq(nil))
df = df.where(!df['Zipcode'].eq(nil))
df = df.where(!df['Start_Time'].eq(nil))
df = df.where(!df['End_Time'].eq(nil))
df = df.where(!df['Visibility(mi)'].eq(nil))
df = df.where(!df['Country'].eq(nil))  
df = df.where(!df['Distance(mi)'].eq(0))  
# eliminate rows where start and end time are the same. 
# This appears to be an empty set
df = df.where(!df['Start_Time'].eq(['End_Time']))  
# need to eliminate rows with 3 or more nil/0 entries


ending = Process.clock_gettime(Process::CLOCK_MONOTONIC)
print("The time after loading and cleaning is: ",(ending))
print("The number of rows remaining after our cleaning process is: ") 
print df.size
print "\n"
# #calculating elapsed time
time = ending - starting
print("Our process took ",(time)," seconds")
print("\n")
# now start answering questions

currentTime = Process.clock_gettime(Process::CLOCK_MONOTONIC)
print"****************************************"
print (currentTime), ("  The month with the most accidents :")


ending = Process.clock_gettime(Process::CLOCK_MONOTONIC)
