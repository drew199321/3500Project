   #!/usr/bin/ruby
#! Partially require just CSV Importer
require 'rubygems'
require 'daru'
# I do not  iknow what I can require for ruby to understand daru. 
# It currently has a name error stating daru is an uninitialized variable 
df = DARU::DataFrame.new(
Daru::DataFrame.from_csv("US_Accidents_data.csv")
