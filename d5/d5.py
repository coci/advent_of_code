import math
with open("input.txt",'r') as file:
	data = file.readlines()

data = [i.strip() for i in data]

moves = {
	'F' : 'l',
	'B' : 'u',
	'R' : 'u',
	'L' : 'l',
}

def find_seat(data):

    seat_list = []
    
    for string in data:
        row = string[:6]
        column = string[7:]

        row_bound_low = 0
        row_bound_up = 127
        for i in row :
            if moves[i] == 'l':
                row_bound_up = row_bound_up - round(((row_bound_up - row_bound_low) / 2 ))

            else:

                row_bound_low = row_bound_low + round(((row_bound_up - row_bound_low) / 2))


        column_bound_low = 0
        column_bound_up = 7
        for i in column:
            if moves[i] == 'l':
                column_bound_up = column_bound_up - round(((column_bound_up - column_bound_low) / 2))
            else:

                column_bound_low = column_bound_low + round(((column_bound_up - column_bound_low) / 2))

        if string[7] == "B":
            row = row_bound_up
        else:
            row = row_bound_low

        if string[-1] == "R":
            column = column_bound_up
        else:
            column = column_bound_low

        seat_list.append(row*8+column)
    
    
    high = 0
    for i in seat_list:
        if i >= high :
        	high = i
    print(high)
        
    
    
    
find_seat(data)