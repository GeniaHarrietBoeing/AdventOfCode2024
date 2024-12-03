import sys
import re
file = sys.argv[1]
with open(file) as f:
    data = f.readlines()
result = 0
for i in range(len(data)):
    instructions = re.findall('mul\(\d{1,3},\d{1,3}\)', data[i])
    for j in range(len(instructions)):
        nr = re.findall('\d{1,3}', instructions[j])
        result += int(nr[0]) * int(nr[1])
print('part one result :', result)


result = 0
enabled = 1
for i in range(len(data)):
    instructions = re.findall('mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)', data[i])
    for j in range(len(instructions)):
        if instructions[j] == 'don\'t()':
            enabled = 0
        elif instructions[j] == 'do()':
            enabled = 1
        elif enabled:
            nr = re.findall('\d{1,3}', instructions[j])
            result += int(nr[0]) * int(nr[1])
print('part two result :', result)
