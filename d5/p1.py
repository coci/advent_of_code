with open('input.txt', 'r') as file:
    countriesStr = file.read()
str = countriesStr.split("\n")

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def calculaterow(row):
    index =[i for i in range(128)]
    for i in row:
            lower , upper = split_list(index)
            if i == 'F':
                index = lower
            else:
                index = upper
    return index[0]

def calculatecol(col):
    index =[i for i in range(8)]
    for i in col:
        lower, upper = split_list(index)
        if i == 'L':
            index = lower
        else:
            index = upper
    return index[0]

result =[]
for item in range(len(str)):
    result.append(int(calculaterow(str[item][:7])*8 + int(calculatecol(str[item][7:]))))

print(max(result))
