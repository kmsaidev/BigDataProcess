#!/usr/bin/python3
import sys

input = sys.argv[1]

dic = dict() 
with open(input, "rt") as fp:
	for line in fp:
		data = line.split("::")
		temp = data[2].replace("\n", "")
		genres = temp.split("|")
		for genre in genres:
			if genre not in dic:
				dic[genre] = 1
			else: 
				dic[genre] += 1
		
keys = dic.keys()
result = ""
for key in keys:
	value = dic[key]
	result += key + " " + str(value) + "\n"

output = sys.argv[2]
with open(output, "wt") as fp:
	fp.write(result)
	
