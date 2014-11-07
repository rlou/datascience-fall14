import re
import numpy
import pandas
from pandas import DataFrame

worldcup = open("worldcup.txt", "r")
countrycode_re = re.compile('.*fb\|([A-Z]{3}).*')
year_re = re.compile('.*([0-9]{4})\sFIFA\sWorld.*')

placenum = 0
countrycode_arr = []
year_arr = []
placenum_arr = []

for line in worldcup:
	countrycode_temp = re.match(countrycode_re, line)
	
	if (countrycode_temp):
		countrycode = countrycode_temp.group(1)
		placenum = 0
	
	placings = line.split(",")
	for place in placings:
		year = re.match(year_re, place)
		if (year):
			countrycode_arr.append(countrycode)
			year_arr.append(year.group(1))
			placenum_arr.append(placenum)
	
	placenum += 1

table = {'Country': countrycode_arr, 'Year': year_arr, 'Place': placenum_arr}
df = DataFrame(data = table)
print df.pivot_table(values = 'Place', rows = 'Country', cols = 'Year', fill_value = '-')
