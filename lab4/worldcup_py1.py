import re

worldcup = open("worldcup.txt", "r")
countrycode_re = re.compile('.*fb\|([A-Z]{3}).*')
year_re = re.compile('.*([0-9]{4})\sFIFA\sWorld.*')

placenum = 0
for line in worldcup:
        countrycode_temp = re.match(countrycode_re, line)

        if (countrycode_temp):
                countrycode = countrycode_temp.group(1)
                placenum = 0

        placings = line.split(",")
        for place in placings:
                year = re.match(year_re, place)
                if (year):
                        print countrycode + ", " + year.group(1) + ", " + str(placenum)
        
        placenum += 1

