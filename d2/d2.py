import re

# read input file
with open("input.txt",'r') as file :
	data = file.readlines()

# store all valid paasword for part one
good_password_part_one = []

# store all valid paasword for part two
good_password_part_two = []

for password in data:

	# search pattern through the data
	match = re.search(r'(\d+)-(\d+) (\w): (\w+)',password)

	first_bound = int(match.group(1))
	second_bound = int(match.group(2))
	letter = match.group(3)
	word = match.group(4)

	
	if not word.count(letter) < first_bound and not word.count(letter) >  second_bound:
		good_password_part_one.append(password)

	if word[first_bound-1] == letter and not 	word[second_bound-1] == letter :
		good_password_part_two.append(password)

	if word[second_bound-1] == letter and not 	word[first_bound-1] == letter :
		good_password_part_two.append(password)


print(len(good_password_part_one))
print(len(good_password_part_two))