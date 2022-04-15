#!/usr/bin/ruby
#! Partially require just CSV Importer
require 'rubygems'
require 'daru'

# Clean Values
starting = Process.clock_gettime(Process::CLOCK_MONOTONIC)
df = Daru::DataFrame.from_csv("US_Accidents_data_quick.csv")
print df.size
print "\n"
#df['Time_Elapsed'] = (df['Start_Time']- df['End_Time']) 
#df['Time elapsed'] = df['Start_Time'] - df['End_Time']

# Immediattely drop rows where certain attributes aren't present
df = df.where(!df['ID'].eq(nil))
df = df.where(!df['Severity'].eq(nil))
df = df.where(!df['Zipcode'].eq(nil))
df = df.where(!df['Start_Time'].eq(nil))
df = df.where(!df['End_Time'].eq(nil))
df = df.where(!df['Visibility(mi)'].eq(nil))
df = df.where(!df['Country'].eq(nil))  
df = df.where(!df['Distance(mi)'].eq(0))  
df = df.where(!df['Start_Time'].eq(['End_Time']))  
# need to eliminate rows with 3 or more nil/0 entries
   print df.size
print "\n"
ending = Process.clock_gettime(Process::CLOCK_MONOTONIC)
# #calculating elapsed time
time = ending - starting
print(time)
