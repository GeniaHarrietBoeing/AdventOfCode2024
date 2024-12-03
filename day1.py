file = 'Data/data_1.txt'
data = []
with open(file) as f:
    data = f.readlines()
data = [[int(j) for j in data[i].split()] for i in range(len(data))]
left_list = [i[0] for i in data]
right_list = [i[1] for i in data]

# part one:

left_list.sort()
right_list.sort()


result = 0
for i in range(len(left_list)):
    result += abs(right_list[i] - left_list[i])
print('part one: ', result)

# part two:


result = 0
for i in range(len(left_list)):

    nr_repeats = 0
    for j in range(len(right_list)):
        if right_list[j] == left_list[i]:
            nr_repeats += 1
    result += nr_repeats * left_list[i]

print('part two: ', result)
