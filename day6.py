import sys
file = sys.argv[1]
with open(file) as f:
    data = f.readlines()
data = [i.strip() for i in data]
data = [list(i) for i in data]
data_t = []

def transpose(data):
    
    width = len(data[0])
    length = len(data)
    data_t = [[0]*length for i in range(width)]
    for i in range(width):
        for j in range(length):
            data_t[i][j] = data[j][i]
    return data_t


width = len(data[0])
length = len(data)
for i in range(length):
    for j in range(width):
        if data[i][j] == '^':
            starting_pos_x = i
            starting_pos_y = j

result = 0
in_map = 1
right_turns = 0
pos_x = starting_pos_x
pos_y = starting_pos_y
while(in_map):
    in_map = 0
    if right_turns == 0: #up
        for i in range(pos_x, -1, -1):
            if data[i][pos_y] == '#':
                in_map = 1
                right_turns += 1
                pos_x = i + 1
                break
            data[i][pos_y] = 'X'

    if right_turns == 1: #right
        for i in range(pos_y, width):
            if data[pos_x][i] == '#':
                in_map = 1
                right_turns += 1
                pos_y = i - 1
                break
            data[pos_x][i] = 'X'

    if right_turns == 2: #down
        for i in range(pos_x, length):
            if data[i][pos_y] == '#':
                in_map = 1
                right_turns += 1
                pos_x = i - 1
                break
            data[i][pos_y] = 'X'

    if right_turns == 3: #left
        for i in range(pos_y, -1, -1):
            if data[pos_x][i] == '#':
                in_map = 1
                right_turns += 1
                pos_y = i + 1
                break
            data[pos_x][i] = 'X'
   
    if right_turns == 4:
        right_turns = 0

    
for i in range(length):
    for j in range(width):
        if data[i][j] == 'X':
            result += 1


print('part one: ', result)


