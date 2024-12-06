import sys
import copy
file = sys.argv[1]
with open(file) as f:
    X = f.readlines()
X = [i.strip() for i in X]
X = [list(i) for i in X]



data = copy.deepcopy(X)
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
nr_loops = 0
for k in range(length):
    for l in range(width):
        data = copy.deepcopy(X)
        data[k][l] = '#'
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
                    if 'U' in data[i][pos_y]:
                        nr_loops += 1
                        in_map = 0
                        break
                    data[i][pos_y] +=  'U'

            elif right_turns == 1: #right
                for i in range(pos_y, width):
                    if data[pos_x][i] == '#':
                        in_map = 1
                        right_turns += 1
                        pos_y = i - 1
                        break
                    if 'R' in data[pos_x][i]:
                        nr_loops += 1
                        in_map = 0
                        break
                    data[pos_x][i] +=  'R'

            elif right_turns == 2: #down
                for i in range(pos_x, length):
                    if data[i][pos_y] == '#':
                        in_map = 1
                        right_turns += 1
                        pos_x = i - 1
                        break
                    if 'D' in data[i][pos_y]:
                        nr_loops += 1
                        in_map = 0
                        break
                    data[i][pos_y] +=  'D'

            elif right_turns == 3: #left
                for i in range(pos_y, -1, -1):
                    if data[pos_x][i] == '#':
                        in_map = 1
                        right_turns += 1
                        pos_y = i + 1
                        break
                    if 'L' in data[pos_x][i]:
                        nr_loops += 1
                        in_map = 0
                        break
                    data[pos_x][i] += 'L'
           
            if right_turns == 4:
                right_turns = 0
    
print('part two: ', nr_loops)
