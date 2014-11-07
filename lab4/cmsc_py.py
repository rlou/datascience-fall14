import pandas
from pandas import DataFrame
import re

cmsc = open("cmsc.txt").read().splitlines()

class_re = re.compile('.*(CMSC[0-9]{3}).*')
section_re = re.compile('^([0-9]{4})$')
seats_re = re.compile('.*Seats.*')
instructor_re = re.compile('^([A-Za-z]+.*\s[A-Za-z]+.*[A-Za-z]+)$')
time_re = re.compile('([A-Za-z]+).*([0-9]+:[0-9]+[a-z]{2}\s\-\s[0-9]+:[0-9]+[a-z]{2}).*')
building_re = re.compile('^([A-Z]{3})\s+[0-9]{4}')
room_re = re.compile('[A-Z]+.*([0-9]{4})$')

for line in cmsc:
	class_temp = re.match(class_re, line)
	section_temp = re.match(section_re, line)
	seats_temp = re.match(seats_re, line)
	instructor_temp = re.match(instructor_re, line)
	time_temp = re.match(time_re, line)
	building_temp = re.match(building_re, line)
	room_temp = re.match(room_re, line)

	if (class_temp):
		classname = class_temp.group(1)
	if (section_temp):
		section = section_temp.group(1)
		print classname + ", " + section_temp.group(1) + ",",
	if (seats_temp):
		for i in re.findall('\d+', line):
			print i + ",",
	if (instructor_temp):
		print instructor_temp.group(1) + ",",
	if(time_temp):
		print time_temp.group(1) + ", " + time_temp.group(2) + ",",
	if(building_temp):
		print building_temp.group(1) + ",",
	if(room_temp):
		print room_temp.group(1) + "\n",

