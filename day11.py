import sys
import time
file = sys.argv[1]
with open(file) as f:
    data = [int(i) for i in f.readline().strip().split()]

def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone))%2 == 0:
            str_stone = str(stone)
            stone_l = int(str_stone[0:len(str_stone)//2])
            stone_r = int(str_stone[len(str_stone)//2:])
            new_stones.append(stone_l)
            new_stones.append(stone_r)
        else:
            new_stones.append(stone*2024)
    return new_stones

# I want to memoize a certain amount of nr of blinks for 0-9:
# mem [(stone_value, nr_step)] = all the possible resulting stones

start = time.time()
mem = {}
nr_blinks = int(sys.argv[2])
steps = nr_blinks // 2
for nr_blink in range(1, steps):
    for i in range(10):
        tmp = []
        if nr_blink == 1:
            tmp = blink([i])
        else:
            stones = mem[(i, nr_blink-1)]
            tmp = blink(stones)
        mem[(i, nr_blink)] = tmp
end1 = time.time()
print('done memorising ', steps, ' steps. This step took ', end1 - start, 'seconds')

def recursive_blink(n, stone):
    resulting_stones = 0
    def rec_blink(n, stone):
        nonlocal resulting_stones 
        if (stone, n) in mem.keys():
            resulting_stones += len(mem[(stone,n)])
        else:     
            if n == 0:
                resulting_stones += 1
            else:
                if stone == 0:
                    rec_blink(n-1, 1)
                elif len(str(stone))%2 == 0:
                    str_stone = str(stone)
                    stone_l = int(str_stone[0:len(str_stone)//2])
                    stone_r = int(str_stone[len(str_stone)//2:])
                    rec_blink(n-1, stone_l)
                    rec_blink(n-1, stone_r)
                else:
                    rec_blink(n-1, stone*2024)
    rec_blink(n, stone)
    return resulting_stones

stones = data
result = 0
#immediately follow each stone to the end
for i in range(len(stones)):
    result += recursive_blink(nr_blinks, stones[i])
end2 = time.time()
print('Nr of stones after ', nr_blinks, ' blinks: ', result)
print('The recursion after memoisation took: ', end2 - end1, ' seconds')


