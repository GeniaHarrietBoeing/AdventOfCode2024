import sys
import copy
file = sys.argv[1]
with open(file) as f:
    data = f.readlines()

def second_warehouse(row):
    new_row = ''
    for i in row:
        if i == '.':
            new_row += '..'
        elif i == '#':
            new_row += '##'
        elif i == '@':
            new_row += '@.'
        elif i == 'O':
            new_row += '[]'
    return new_row


warehouse = []
movements = []
warehouse_done = False
for i in range(len(data)):
    if data[i] == '\n':
        warehouse_done = True
        continue
    if not warehouse_done:
        warehouse.append(list(second_warehouse(data[i].strip())))
    elif warehouse_done:
        movements += list(data[i].strip())




def push_object(object_x, object_y, direction):
    # always left side of object position given!!!!!
    successful_movement = False

    if direction == '<':
        for i in range(object_y - 1, 0, -1):
            if warehouse[object_x][i] == '.':
                for j in range(i, object_y, 2):
                    warehouse[object_x][j] = '['
                    warehouse[object_x][j+1] = ']'
                successful_movement = True
                return successful_movement
            elif warehouse[object_x][i] == '#':
                return successful_movement
            
    if direction == '>':
        for i in range(object_y + 2, len(warehouse[0])):
            if warehouse[object_x][i] == '.':
                for j in range(i, object_y - 1, -2):
                    warehouse[object_x][j] = ']'
                    warehouse[object_x][j-1] = '['
                successful_movement = True
                return successful_movement
            elif warehouse[object_x][i] == '#':
                return successful_movement

    if direction == '^': 
        #no possible path
        if warehouse[object_x - 1][object_y] == '#' or warehouse[object_x - 1][object_y + 1] == '#':
            return successful_movement
        # obstructed but possible path perhaps, either obstructed by single obstacle or pair
        # pair
        if warehouse[object_x - 1][object_y] == ']' and warehouse[object_x - 1][object_y + 1] == '[':
                successful_movement_1 = push_object(object_x - 1, object_y - 1, direction)
                successful_movement_2 = push_object(object_x - 1, object_y + 1, direction)
        # single
        else:
            if warehouse[object_x - 1][object_y] == '[':
                successful_movement = push_object(object_x - 1, object_y, direction)
            elif warehouse[object_x - 1][object_y] == ']':
                successful_movement = push_object(object_x - 1, object_y - 1, direction)
            elif warehouse[object_x - 1][object_y + 1] == '[':
                successful_movement = push_object(object_x - 1, object_y + 1, direction)
        # direct unobstructed path available for object
        if warehouse[object_x - 1][object_y] == '.':
            if warehouse[object_x - 1][object_y + 1] == '.':
                successful_movement = True
                warehouse[object_x - 1][object_y] = '['
                warehouse[object_x - 1][object_y + 1] = ']'
                warehouse[object_x ][object_y + 1] = '.'
                warehouse[object_x ][object_y ] = '.'

                return successful_movement

    if direction == 'v': 
        #no possible path
        if warehouse[object_x + 1][object_y] == '#' or warehouse[object_x + 1][object_y + 1] == '#':
            return successful_movement
        # obstructed but possible path perhaps, either obstructed by single obstacle or pair
        # pair
        if warehouse[object_x + 1][object_y] == ']' and warehouse[object_x + 1][object_y + 1] == '[':
                successful_movement_1 = push_object(object_x + 1, object_y - 1, direction)
                successful_movement_2 = push_object(object_x + 1, object_y + 1, direction)
        # single
        else:
            if warehouse[object_x + 1][object_y] == '[':
                successful_movement = push_object(object_x + 1, object_y, direction)
            elif warehouse[object_x + 1][object_y] == ']':
                successful_movement = push_object(object_x + 1, object_y - 1, direction)
            elif warehouse[object_x + 1][object_y + 1] == '[':
                successful_movement = push_object(object_x + 1, object_y + 1, direction)
        # direct unobstructed path available for object
        if warehouse[object_x + 1][object_y] == '.':
            if warehouse[object_x + 1][object_y + 1] == '.':
                successful_movement = True
                warehouse[object_x + 1][object_y] = '['
                warehouse[object_x + 1][object_y + 1] = ']'
                warehouse[object_x ][object_y + 1] = '.'
                warehouse[object_x ][object_y ] = '.'

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

for i in warehouse:
    print(''.join(i))


######## ALWAYS GIVE PUSH_OBJECT THE LEFT SIDE OF THE OBJECT!!!!!!!!!!!
for i in range(len(movements)):
    successful_movement = False
    if movements[i] == '<':
        if warehouse[rob_x][rob_y - 1] == '.':
            successful_movement = True
        elif warehouse[rob_x][rob_y - 1] == ']':
            successful_movement = push_object(rob_x, rob_y - 2, movements[i])
        if successful_movement:
            warehouse[rob_x][rob_y - 1] = '@'
            warehouse[rob_x][rob_y] = '.'
            rob_y -= 1

    if movements[i] == '>':
        if warehouse[rob_x][rob_y + 1] == '.':
            successful_movement = True
        elif warehouse[rob_x][rob_y + 1] == '[':
            successful_movement = push_object(rob_x, rob_y + 1, movements[i])
        if successful_movement:
            warehouse[rob_x][rob_y + 1] = '@'
            warehouse[rob_x][rob_y] = '.'
            rob_y += 1
    
    if movements[i] == '^':
        cp_warehouse = copy.deepcopy(warehouse)
        if warehouse[rob_x - 1][rob_y] == '.':
            successful_movement = True
        elif warehouse[rob_x - 1][rob_y] == '[':
            successful_movement = push_object(rob_x - 1, rob_y, movements[i])
        elif warehouse[rob_x - 1][rob_y] == ']':
            successful_movement = push_object(rob_x - 1, rob_y - 1, movements[i])
        if successful_movement:
            warehouse[rob_x - 1][rob_y] = '@'
            warehouse[rob_x][rob_y] = '.'
            rob_x -= 1
        if not successful_movement:
            for k in range(len(warehouse)):
                for l in range(len(warehouse[0])):
                    warehouse[k][l] = cp_warehouse[k][l]

    if movements[i] == 'v': 
        cp_warehouse = copy.deepcopy(warehouse)
        if warehouse[rob_x + 1][rob_y] == '.':
            successful_movement = True
        elif warehouse[rob_x + 1][rob_y] == '[':
            successful_movement = push_object(rob_x + 1, rob_y, movements[i])
        elif warehouse[rob_x + 1][rob_y] == ']':
            successful_movement = push_object(rob_x + 1, rob_y - 1, movements[i])
        if successful_movement:
            warehouse[rob_x + 1][rob_y] = '@'
            warehouse[rob_x][rob_y] = '.'
            rob_x += 1
        
        if not successful_movement:
            for k in range(len(warehouse)):
                for l in range(len(warehouse[0])):
                    warehouse[k][l] = cp_warehouse[k][l]

for i in warehouse:
    print(''.join(i))

gps_coordinate = 0

for i in range(len(warehouse)):
    for j in range(len(warehouse[0])):
        if warehouse[i][j] == '[':
            gps_coordinate += 100 * i + j

print('Part one: ', gps_coordinate)



