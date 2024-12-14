import sys
import re
import numpy as np
file = sys.argv[1]
with open(file) as f:
    data = f.readlines()


max_pushes = 100
nr_tokens  = 0

for i in range(0, len(data), 4):
    A = [int(i) for i in re.findall(r'[\d]+', data[i])]
    B = [int(i) for i in re.findall(r'[\d]+', data[i + 1])]
    P = [int(i) for i in re.findall(r'[\d]+', data[i + 2])]
 
    found_solution = False
    
    for k in range(max_pushes):
        for l in range(max_pushes):
            x = A[0]*k + B[0]*l
            y = A[1]*k + B[1]*l
            if x == P[0] and y == P[1]:
                tmp_cost = 3*k + 1*l
                if found_solution:
                    if tmp_cost < cost:
                        cost = tmp_cost
                else:
                    found_solution = True
                    cost = tmp_cost
    if found_solution:
        nr_tokens += cost
print('Tokens part one: ', nr_tokens)


nr_tokens  = 0

for i in range(0, len(data), 4):
    A = [int(i) for i in re.findall(r'[\d]+', data[i])]
    B = [int(i) for i in re.findall(r'[\d]+', data[i + 1])]
    P = [int(i) + 10000000000000 for i in re.findall(r'[\d]+', data[i + 2])]

    A_inv = [[0 for i in range(2)] for j in range(2)]
    det = (A[0]*B[1] - A[1]*B[0])
    A_inv[0][0] = B[1]
    A_inv[0][1] = (-B[0])
    A_inv[1][0] = (-A[1])
    A_inv[1][1] = A[0]

    #solution = A_inv * P
    nr_a_pushes = (A_inv[0][0] * P[0] + A_inv[0][1] * P[1]) / det
    nr_b_pushes = (A_inv[1][0] * P[0] + A_inv[1][1] * P[1]) / det

    
    if int(nr_a_pushes) == nr_a_pushes and int(nr_b_pushes) == nr_b_pushes:
        nr_tokens += int(nr_a_pushes) * 3 + int(nr_b_pushes) 


print('Tokens part two: ', nr_tokens)
