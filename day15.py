import sys
file = sys.argv[1]
with open(file) as f:
    data = f.readlines()

warehouse = []
movements = []
warehouse_done = False
for i in range(len(data)):
    if data[i] == '\n':
        warehouse_done = True
        continue
    if not warehouse_done:
        warehouse.append(list(data[i].strip()))
    elif warehouse_done:
        movements += list(data[i].strip())

def push_object(object_x, object_y, direction):
    successful_movement = False

    if direction == '<':
        for i in range(object_y - 1, 0, -1):
            if warehouse[object_x][i] == '.':
                warehouse[object_x][i] = 'O'
                successful_movement = True
                return successful_movement
            elif warehouse[object_x][i] == '#':
                return successful_movement
            
    if direction == '>':
        for i in range(object_y + 1, len(warehouse[0])):
            if warehouse[object_x][i] == '.':
                warehouse[object_x][i] = 'O'
                successful_movement = True
                return successful_movement
            elif warehouse[object_x][i] == '#':
                return successful_movement

    if direction == '^':
        for i in range(object_x - 1, 0, -1):
            if warehouse[i][object_y] == '.':
                warehouse[i][object_y] = 'O'
                successful_movement = True
                return successful_movement
            elif warehouse[i][object_y] == '#':
                return successful_movement

    if direction == 'v':
        for i in range(object_x + 1, len(warehouse)):
            if warehouse[i][object_y] == '.':
                warehouse[i][object_y] = 'O'
                successful_movement = True
                return successful_movement
            elif warehouse[i][object_y] == '#':
                return successful_movement

# starting position:
for i in range(len(warehouse)):
    for j in range(len(warehouse[0])):
        if warehouse[i][j] == '@':
            start_x = i
            start_y = j
print('starting position', start_x, start_y)




# move the robot
rob_x = start_x
rob_y = start_y
counter = 0
for i in range(len(movements)):
    successful_movement = False
    if movements[i] == '<':
        if warehouse[rob_x][rob_y - 1] == '.':
            successful_movement = True
        elif warehouse[rob_x][rob_y - 1] == 'O':
            successful_movement = push_object(rob_x, rob_y - 1, movements[i])
        if successful_movement:
            warehouse[rob_x][rob_y - 1] = '@'
            warehouse[rob_x][rob_y] = '.'
            rob_y -= 1

    if movements[i] == '>':
        if warehouse[rob_x][rob_y + 1] == '.':
            successful_movement = True
        elif warehouse[rob_x][rob_y +1] == 'O':
            successful_movement = push_object(rob_x, rob_y + 1, movements[i])
        if successful_movement:
            warehouse[rob_x][rob_y + 1] = '@'
            warehouse[rob_x][rob_y] = '.'
            rob_y += 1
    
    if movements[i] == '^':
        if warehouse[rob_x - 1][rob_y] == '.':
            successful_movement = True
        elif warehouse[rob_x - 1][rob_y] == 'O':
            successful_movement = push_object(rob_x - 1, rob_y, movements[i])
        if successful_movement:
            warehouse[rob_x - 1][rob_y] = '@'
            warehouse[rob_x][rob_y] = '.'
            rob_x -= 1

    if movements[i] == 'v':
        if warehouse[rob_x + 1][rob_y] == '.':
            successful_movement = True
        elif warehouse[rob_x + 1][rob_y] == 'O':
            successful_movement = push_object(rob_x + 1, rob_y, movements[i])
        if successful_movement:
            warehouse[rob_x + 1][rob_y] = '@'
            warehouse[rob_x][rob_y] = '.'
            rob_x += 1

gps_coordinate = 0

for i in range(len(warehouse)):
    for j in range(len(warehouse[0])):
        if warehouse[i][j] == 'O':
            gps_coordinate += 100*i + j

print('Part one: ', gps_coordinate)



