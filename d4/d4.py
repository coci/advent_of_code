import re

with open("input.txt",'r') as file:
	data = file.readlines()

data = [ i.strip() for i in data ]
data = " ".join(data).split("  ")


clear_data = []
for i in data:
	Dict = dict((x.strip(), y.strip()) for x, y in (element.split(':') for element in i.split(' ')))
	clear_data.append(Dict)


def part_one(data):
	needed_word = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
	counter = 0
	for i in data:
		keys = list(i.keys())
		if all(word in keys for word in needed_word):
			counter += 1

	print(counter)


def data_validation(i):
	byr_status = 1920 <= int(i['byr']) <= 2002
	iyr_status = 2010 <= int(i['iyr']) <= 2020
	eyr_status = 2020 <= int(i['eyr']) <= 2030

	hgt_status = False
	if i['hgt'][-2::] in ['cm','in']:
		if i['hgt'][-2::] == 'cm':

			if 150 <=int(i['hgt'][:-2]) <= 193:
				hgt_status = True
		else:
			if 59 <=int(i['hgt'][:-2]) <= 76:
				hgt_status = True

	hcl_status = False
	if len(i['hcl']) == 7 and i['hcl'][0] == "#":
		if bool(re.match("[0-9]+", i['hcl'])):
			hcl_status = True

		if not bool(re.match("[f-z]+", i['hcl'])):
			hcl_status = True

	ecl_status = False
	if i['ecl'] in ['amb' ,'blu', 'brn' ,'gry' ,'grn' ,'hzl','oth']:
		ecl_status = True

	pid_status = False
	if len(i['pid']) == 9 :
		pid_status = True
	return byr_status and iyr_status and eyr_status and hgt_status and hcl_status and ecl_status and pid_status


def part_two(data):
	needed_word = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
	counter = 0
	for i in data:
		keys = list(i.keys())
		if all(word in keys for word in needed_word):
			if data_validation(i) :
				counter+=1
	print(counter)

part_two(clear_data)


