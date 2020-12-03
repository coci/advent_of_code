from functools import reduce
import operator

with open('input.txt','r') as file :
	data = file.readlines()

def find_trees(data):

	all_move_need = len(data) * 8
	require_reapeat_pattern = (all_move_need // len(data[0]))

	# make repeated data
	data = [i.rstrip("\n") * require_reapeat_pattern for i in data]

	# all possibilities
	slopes = [{"r":1,"d":1},{"r":3,"d":1},{"r":5,"d":1},{"r":7,"d":1},{"r":1,"d":2}]

	trees_on_each_step = []

	for slop in slopes:
		current_index = 0
		tree_count = 0
		for i in range(slop['d'],len(data),slop['d']):
			current_index += slop['r']
			if data[i][current_index] == "#":
				tree_count += 1
		trees_on_each_step.append(tree_count)
	print(trees_on_each_step)


find_trees(data)

