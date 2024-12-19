import sys
file = sys.argv[1]
with open(file) as f:
    data = f.readlines()


A = int(data[0][11:])
B = int(data[1][11:])
C = int(data[2][11:])
output = ''
program = [int(i) for i in data[4][8:-1].split(',')]

def combo_operand(y):
    if y <= 3: return y
    elif y == 4: return A
    elif y == 5: return B
    elif y == 6: return C
    elif y == 7: print('errrorororor')

def adv(y):
    global A
    A = int(A / 2**y)

def bxl(y):
    global B
    B = B ^ y

def bst(y):
    global B
    B = y % 8

def out(y):
    global output
    output += str(y % 8) + ','

def bxc():
    global B
    B = B ^ C

def bdv(y):
    global B
    B = int(A / 2**y)

def cdv(y):
    global C
    C = int(A / 2**y)

not_finished = True
i = 0



for j in range(0, 8):
    A = 117440 + 8**j + j
    B = 0
    C = 0
    i = 0
    print('start A, B, C', A, B, C)
    while(not_finished):
        instruction = program[i]
        operand = program[i+1]
        if instruction == 0:
            adv(combo_operand(operand))
        elif instruction == 1:
            bxl(operand)
        elif instruction == 2:
            bst(combo_operand(operand))
        elif instruction == 3:
            if A != 0: 
                i = operand
                continue
        elif instruction == 4:
            bxc()
        elif instruction == 5:
            out(combo_operand(operand))
        elif instruction == 6:
            bdv(combo_operand(operand))
        elif instruction == 7:
            cdv(combo_operand(operand))


        i += 2  

        if i > len(program) - 2:
            not_finished = False
    print('A, B, C', A, B, C)
    print('output ', output[:-1])

## Part two
## In the last iteration A needs to be 0 and B%8also 
# so at end A = 0 and B = x*8 C = 



