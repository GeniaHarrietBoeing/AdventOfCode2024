import sys
file = sys.argv[1]
seconds = int(sys.argv[2])

with open(file) as f:
    data = f.readlines()

length = 103
width = 101

#length = 7
#width = 11

def get_position_after_walking(x, v, s):

    while(s > 0):
        new_x = x[0] + v[0]
        new_y = x[1] + v[1]

        if new_x < 0:
            new_x = width + new_x
        elif new_x >= width:
            new_x = new_x - width
        if new_y < 0:
            new_y = length + new_y
        elif new_y >= length:
            new_y = new_y - length
        s -= 1

    return [new_x, new_y]


half_length = length // 2 
half_width = width // 2
Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0



for i in range(len(data)):
    tmp = data[i].split()
    x = [int(j) for j in tmp[0].split('=')[1].split(',')]
    v = [int(j) for j in tmp[1].split('=')[1].split(',')]
    new_x = get_position_after_walking(x, v, seconds)

    
    
    if new_x[0] < half_width:
        if new_x[1] < half_length: 
            Q1 += 1
        elif new_x[1] > half_length:
            Q2 += 1
    elif new_x[0] > half_width:
        if new_x[1] < half_length: 
            Q3 += 1
        elif new_x[1] > half_length:
            Q4 += 1

print('Part one: ', Q1 * Q2 * Q3 * Q4)
print('Q1, Q2, Q3, Q4', Q1, Q2, Q3, Q4)

#for i in field:
#    print(''.join(str(x) for x in i))


no_christmas_tree = True
seconds = 0


x_pos = []
v = []
for i in range(len(data)):
    tmp = data[i].split()
    x_pos.append([int(j) for j in tmp[0].split('=')[1].split(',')])
    v.append([int(j) for j in tmp[1].split('=')[1].split(',')])

field = [['.' for i in range(width)] for j in range(length)]
for i in range(len(x_pos)):
    print(x_pos[i])
    if field[x_pos[i][1]][x_pos[i][0]] == '.':
        field[x_pos[i][1]][x_pos[i][0]] = 1
    else:
        field[x_pos[i][1]][x_pos[i][0]] += 1

for i in field:
    print(''.join(str(x) for x in i))

while(no_christmas_tree):
    for i in range(len(x_pos)):
        new_x = get_position_after_walking(x_pos[i], v[i], 1)

        if field[new_x[1]][new_x[0]] == '.':
            field[new_x[1]][new_x[0]] = 1
        else:
            field[new_x[1]][new_x[0]] += 1
        
        if field[x_pos[i][1]][x_pos[i][0]] == 1:
            field[x_pos[i][1]][x_pos[i][0]] = '.'
        else:
            field[x_pos[i][1]][x_pos[i][0]] -= 1
        
        x_pos[i][0] = new_x[0]
        x_pos[i][1] = new_x[1]

    for i in range(len(field)):
        counter = 0
        for j in range(len(field[0])):
            if field[i][j] != '.':
                counter += 1
            elif field[i][j] == '.':
                counter = 0

            if counter > 7:
                print('seconds', seconds)
                no_christmas_tree = False
                break
    
    if seconds % 100 == 0:
        print(seconds, counter)
    
    seconds += 1

for i in field:
    print(''.join(str(x) for x in i))

for i in field:
    print(''.join(str(x) for x in i))

print('Part two: ', seconds)

