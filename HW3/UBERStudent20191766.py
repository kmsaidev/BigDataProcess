#!/usr/bin/python3
import sys
import calendar

class Quantity:
	def __init__(self, vehicles, trips):
		self.vehicles = vehicles
		self.trips = trips

dayofweek = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
input = sys.argv[1]
output = sys.argv[2]

dic = dict()
with open(input, "rt") as fp:
	for line in fp:
		data = line.split(",")
		temp = data[1].split("/")
		day = calendar.weekday(int(temp[2]), int(temp[0]), int(temp[1]))
		dow = dayofweek[day]
		info = data[0], dow
		if info not in dic:
			dic[info] = Quantity(int(data[2]), int(data[3]))
		else:
			dic[info].vehicles += int(data[2])
			dic[info].trips += int(data[3])

keys = dic.keys()
result = ""
for key in keys:
	value = dic[key]
	result += key[0] + "," + key[1] + " " + str(value.vehicles) + "," + str(value.trips) + "\n"

with open(output, "wt") as fp:
	fp.write(result)	
