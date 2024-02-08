# Python program to read
# json file

import json

# Opening JSON file
f = open('./input/data.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['constraints']:
	print(i)

for i in data['constraints']['length']:
	print(i)

minimum_length = data['constraints']['length']['minimum']
print(minimum_length)

# Closing file
f.close()
