   #!/usr/bin/ruby
#! Partially require just CSV Importer
require 'rubygems'
require 'daru'

# Clean Values
df = Daru::DataFrame.from_csv("US_Accidents_data.csv")
print df.size
print "\n"
   # Immeditately drop rows where certain attributes aren't present
   df = df.where(!df['ID'].eq(nil))
   df = df.where(!df['Severity'].eq(nil))
   df = df.where(!df['Zipcode'].eq(nil))
   df = df.where(!df['Start_Time'].eq(nil))
   df = df.where(!df['End_Time'].eq(nil))
   df = df.where(!df['Visibility(mi)'].eq(nil))
   df = df.where(!df['Country'].eq(nil))  
print df.size
print "\n"






