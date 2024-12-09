import sys
file = sys.argv[1]
with open(file) as f:
    data = f.readlines()
for i in range(len(data)):
    data[i] = list(data[i].strip())

antennas = {}
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] != '.' and data[i][j] not in antennas.keys():
            antennas[data[i][j]] = [i, j]
        elif data[i][j] in antennas.keys():
            antennas[data[i][j]] = antennas[data[i][j]] + [i, j]
            

def possible_antinodes(pos_1, pos_2, length, width):
    diff_x = pos_2[0] - pos_1[0]
    diff_y = pos_2[1] - pos_1[1]
    antinodes = []
    antinode_1 = []
    antinode_2 = []

    antinode_1.append(pos_1[0] - diff_x)
    antinode_2.append(pos_2[0] + diff_x)
    antinode_1.append(pos_1[1] - diff_y)
    antinode_2.append(pos_2[1] + diff_y)

    if antinode_1[0] >= 0 and antinode_1[1] >= 0:
        if antinode_1[0] < length and antinode_1[1] < width:
            antinodes.append(antinode_1)
    
    if antinode_2[0] >= 0 and antinode_2[1] >= 0:
        if antinode_2[0] < length and antinode_2[1] < width:
            antinodes.append(antinode_2)

    return antinodes

def harmonics_antinodes(pos_1, pos_2, length, width):
    diff_x = pos_2[0] - pos_1[0]
    diff_y = pos_2[1] - pos_1[1]
    antinodes = []
    
    #from pos_1
    on_map = True
    i = 1
    while(on_map):
        new_x = pos_1[0] - diff_x * i
        new_y = pos_1[1] - diff_y * i
        if new_x >= 0 and new_x < length and new_y >= 0 and new_y < width:
            antinodes.append([new_x, new_y])
            i += 1
        else:
            on_map = False

    #from pos_2
    on_map = True
    i = 1
    while(on_map):
        new_x = pos_2[0] + diff_x * i
        new_y = pos_2[1] + diff_y * i
        if new_x >= 0 and new_x < length and new_y >= 0 and new_y < width:
            antinodes.append([new_x, new_y])
            i += 1
        else:
            on_map = False

    return antinodes

result = 0
for i in range(len(antennas.keys())):
    antenna = [*antennas][i]
    positions = antennas[antenna]
    for j in range(0, len(positions) - 2, 2):
        for k in range(j + 2, len(positions), 2):
            antinodes = possible_antinodes(positions[j:j+2], positions[k:k+2], len(data), len(data[0]))
            
            for n in antinodes:
                data[n[0]][n[1]] = '#'

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == '#': result += 1
print('Part one: ', result)


result = 0
for i in range(len(antennas.keys())):
    antenna = [*antennas][i]
    positions = antennas[antenna]
    for j in range(0, len(positions) - 2, 2):
        for k in range(j + 2, len(positions), 2):
            antinodes = harmonics_antinodes(positions[j:j+2], positions[k:k+2], len(data), len(data[0]))
            
            for n in antinodes:
                data[n[0]][n[1]] = '#'

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == '#': result += 1
        if data[i][j] in antennas: result += 1
print('Part two: ', result)
