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

        x[0] = new_x
        x[1] = new_y

        s -= 1

    return x


half_length = length // 2 
half_width = width // 2
Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0

field = [['.' for i in range(width)] for j in range(length)]


for i in range(len(data)):
    tmp = data[i].split()
    x = [int(j) for j in tmp[0].split('=')[1].split(',')]
    v = [int(j) for j in tmp[1].split('=')[1].split(',')]
    new_x = get_position_after_walking(x, v, seconds)
    if field[new_x[1]][new_x[0]] == '.':
        field[new_x[1]][new_x[0]] = 1
    else: 
        field[new_x[1]][new_x[0]] += 1


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
