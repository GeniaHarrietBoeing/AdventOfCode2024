import sys
import re
file = sys.argv[1]
with open(file) as f:
    data = f.readlines()
data = [data[i].strip() for i in range(len(data))]

result = 0

tmp_data = []
    
#vertical
for j in range(len(data[0])):
    tmp = ''
    for i in range(len(data)):
        tmp += data[i][j]
    tmp_data.append(tmp)

#diagonal 
for i in range(len(data[0])):
    #right leaning upper half
    tmp = ''
    for j in range(len(data)):
        if i + j < len(data[0]):
            tmp += data[j][i+j]    
    tmp_data.append(tmp)

    #left leaning upper half
    tmp = ''
    for j in range(len(data)):
        if i + j + 1 <= len(data[0]):
            tmp += data[j][len(data[0])-i-j-1]
    tmp_data.append(tmp)
#Note : skip middle diagonal
for i in range(1, len(data[0])):
    #right leaning lower half reversed
    tmp = ''
    for j in range( len(data)):
        if i + j + 1 <= len(data[0]):
            tmp += data[-1-j][-1-i-j]
    tmp_data.append(tmp)
    tmp = ''
    #left leaning lower half 
    for j in range(len(data)):
        if i + j + 1 <= len(data[0]):
            tmp += data[-1-j][i+j]
    tmp_data.append(tmp)

part_one_data = data + tmp_data
result = 0
for i in range(len(part_one_data)):
    #horizontal
    result += len(re.findall('XMAS', part_one_data[i])) + len(re.findall('SAMX', part_one_data[i]))

print('Part one: ', result)

## Part two:
result = 0
for i in range(len(data)-2):
    for j in range(len(data[0])-2):
        if data[i][j] == 'M' and data[i+1][j+1] == 'A' and data[i+2][j+2] == 'S':
            if data[i][j+2] == 'M' and data[i+2][j] == 'S':
                result += 1
            elif data[i][j+2] == 'S' and data[i+2][j] == 'M':
                result += 1

        if data[i][j] == 'S' and data[i+1][j+1] == 'A' and data[i+2][j+2] == 'M':
            if data[i][j+2] == 'M' and data[i+2][j] == 'S':
                result += 1
            elif data[i][j+2] == 'S' and data[i+2][j] == 'M':
                result += 1
print('Part two: ', result)

