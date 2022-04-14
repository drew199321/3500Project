   #!/usr/bin/ruby
#! Partially require just CSV Importer
require 'rubygems'
require 'daru'

# Clean Values
df = Daru::DataFrame.from_csv("US_Accidents_data_quick.csv")
print "Ping1\n"
print df.size
print "\n"
# df2 = df.reject_values nil
   dropRowsID = df.where(!df['ID'].eq(nil) )
   df = df.where(!df['ID'].eq(nil))
   print dropRowsID
   print "\n"

   dropRowsSeverity = df.where(!df['Severity'].eq(nil))
   df = df.where(!df['Severity'].eq(nil))
   print dropRowsSeverity
   print "\n"

   dropRowsZipcode = df.where(!df['Zipcode'].eq(nil))
   df = df.where(!df['Zipcode'].eq(nil))
   print dropRowsZipcode
   print "\n"

   dropRowsStartTime = df.where(!df['Start_Time'].eq(nil))
   df = df.where(!df['Start_Time'].eq(nil))
   print dropRowsStartTime
   print "\n"

   dropRowsEndTime = df.where(!df['End_Time'].eq(nil) )
   df = df.where(!df['End_Time'].eq(nil))
   print dropRowsEndTime
   print "\n"

   dropRowsVisibility = df.where(!df['Visibility(mi)'].eq(nil))
   df = df.where(!df['Visibility(mi)'].eq(nil))
   print dropRowsVisibility
   print "\n"
   
   dropRowsWeatherCondition = df.where(!df['Weather_Condition'].eq(nil) )
   df = df.where(!df['Weather_Condition'].eq(nil))
   print dropRowsVisibility
   print "\n"

   df = df.where(!df['Country'].eq(nil))  
   dropRowsCountry = df.where(!df['Country'].eq(nil))
   print dropRowsCountry
   print "\n"
print "Ping2\n"
print df.size
print "\n"






