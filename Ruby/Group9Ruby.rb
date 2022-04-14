   #!/usr/bin/ruby
#! Partially require just CSV Importer
require 'rubygems'
require 'daru'
df = Daru::DataFrame.new(
Daru::DataFrame.from_csv("US_Accidents_data.csv"))
