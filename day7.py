import sys
import time
import math
file = sys.argv[1]
with open(file) as f:
    data = f.readlines()


def generate_combinations(n, operators_used):
    combinations = []
    def gencom(n, operators_used, instruction = ''):
        if len(instruction) == n:
            combinations.append(instruction)
        else:
            for i in range(operators_used):
                gencom(n, operators_used, instruction + str(i))
    gencom(n, operators_used)
    return combinations


def calibration_result(operators, operators_used, data):
    total_calibration_result = 0

    # only generate combination of instructions once
    lengths_instructions = []
    for i in range(len(data)):
        tmp = data[i].split(':')
        test_value = int(tmp[0])
        values = [int(j) for j in tmp[1].split()]
        nr_operator_slots = len(values) - 1

        if nr_operator_slots not in lengths_instructions:
            lengths_instructions.append(nr_operator_slots)

    possible_instructions = []
    for i in lengths_instructions:
        possible_instructions.append(generate_combinations(i, operators_used))
        print(len(generate_combinations(i, operators_used)))

    for i in range(len(data)):
        tmp = data[i].split(':')
        test_value = int(tmp[0])
        values = [int(j) for j in tmp[1].split()]
        nr_operator_slots = len(values) - 1

        # get the right set of instructions
        for j in range(len(lengths_instructions)):
            if lengths_instructions[j] == nr_operator_slots:
                instructions = possible_instructions[j]

        for j in range(len(instructions)):
            result = values[0]

            for k in range(len(instructions[j])):
                if instructions[j][k] == operators['+']:
                   result += values[k+1] 
                elif instructions[j][k] == operators['*']:
                    result *= values[k+1]
                elif instructions[j][k] == operators['||']:
                    result = int(str(result)+str(values[k+1]))

                if result > test_value:
                    break

            if result == test_value:
                total_calibration_result += test_value
                break

    return total_calibration_result


operators = {'+': '0', '*' : '1', '||' : '2'}

start = time.time()
print('Total calibration result part one: ', calibration_result(operators, 2, data))
end = time.time()
print('Time for first part: ', end - start)

start = time.time()
print('Total calibration result part two: ', calibration_result(operators, 3, data))
end = time.time()
print('Time for second part: ', end - start)
