import sys
import copy
file = sys.argv[1]
with open(file) as f:
    data = f.readline().strip()
data = [int(i) for i in data]

n_files = len(data)//2 + 1
length_map = sum(data)
free_space = sum([data[i] for i in range(1, len(data), 2)])
filled_space = sum([data[i] for i in range(0, len(data), 2)])

expanded_map = [-1]*length_map
idx = 0
for i in range(0, len(data), 2):
    for j in range(data[i]):
        expanded_map[idx + j] = i // 2
    if i + 1 < len(data):   
        idx += data[i] + data[i+1]

free_space_map = [-1]*free_space
idx = 0
for i in range(len(data)-1, 0, -2):
    for j in range(data[i]):
        if idx + j < free_space:
            free_space_map[idx + j] = i // 2
        else:
            break
    idx += data[i]

compact_map = [-1]*filled_space
idx = 0
for i in range(filled_space):
    if expanded_map[i] != -1:
        compact_map[i] = expanded_map[i]
    else:
        compact_map[i] = free_space_map[idx]
        idx += 1

result = 0
for i in range(len(compact_map)):
    result += i * compact_map[i]
print('Part one result: ', result)

block_map = expanded_map
data_original = copy.deepcopy(data)
idx_end = len(data) - 1
while(idx_end > 0):
    for i in range(1, idx_end, 2):
        if data[i] >= data_original[idx_end]:
            for j in range(data_original[idx_end]):
                block_map[sum([data[k] for k in range(i)]) + j] = idx_end // 2
                block_map[sum([data[k] for k in range(idx_end)]) + j ] = -1
            data[i-1] += data_original[idx_end]
            data[i] -=  data_original[idx_end]
            break
    idx_end -= 2

result = 0
for i in range(len(block_map)):
    if block_map[i] != -1:
        result += i * block_map[i]
print('Part two result: ', result)





