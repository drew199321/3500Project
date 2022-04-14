   #!/usr/bin/ruby
#! Partially require just CSV Importer
require 'rubygems'
require 'daru'

# Clean Values
df = Daru::DataFrame.from_csv("US_Accidents_data.csv")
print "Ping1\n"
print df.size
print "\n"
# df2 = df.reject_values nil
df.filter_rows do |row|
   !df['ID'].eq(nil) |
   !df['Severity'].eq(nil) |
   !df['Zipcode'].eq(nil) |
   !df['Start_Time'].eq(nil) 
   !df['End_Time'].eq(nil) |
   !df['Visibility(mi)'].eq(nil) |
   !df['Weather_Condition'].eq(nil) |
   !df['Country'].eq(nil)
end

print "Ping2\n"
print df.size
print "\n"






