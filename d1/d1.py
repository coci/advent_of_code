"""
desciption :
	- combinations() return all combination in iteration like :
		a = [1,2,3]
		result combinations(a,2) == > [[1,2],[1,3],[2,3]]

	- reduce() applies function over the sequence
	- operator.mul will multiple all the elements of sequence

"""
from itertools import combinations
from functools import reduce
import operator

data = list(map(int,open('input.txt').readlines()))

def find_numbers(number_of_element):
	for combination in combinations(data,number_of_element): # find all combination
		if sum(combination) == 2020 : # if sum combination equls to 2020
			return reduce(operator.mul,combination) # multiple all of the elements in the sequence

#part one
find_numbers(2)

#part two
find_numbers(3)
