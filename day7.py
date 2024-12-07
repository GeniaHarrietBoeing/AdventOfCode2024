import sys
file = sys.argv[1]
with open(file) as f:
    data = f.readlines()


def generate_combinations(n, operators):
    combinations = []
    def gencom(n, operators, instruction = ''):
        if len(instruction) == n:
            combinations.append(instruction)
        else:
            for i in operators:
                gencom(n, operators, instruction + i)
    gencom(n, operators)
    return combinations


def calibration_result(operators, data):
    total_calibration_result = 0
    for i in range(len(data)):
        tmp = data[i].split(':')
        test_value = int(tmp[0])
        values = [int(j) for j in tmp[1].split()]
        nr_operator_slots = len(values) - 1
        instructions = generate_combinations(nr_operator_slots, operators)
        for j in range(len(instructions)):
            result = values[0]
            for k in range(len(instructions[j])):
                if instructions[j][k] == '+':
                   result += values[k+1] 
                elif instructions[j][k] == '*':
                    result *= values[k+1]
                elif instructions[j][k] == '|':
                    result = int(str(result)+str(values[k+1]))
            if result == test_value:
                total_calibration_result += test_value
                break
    return total_calibration_result

operators = ['+', '*']
print('Total calibration result part one: ', calibration_result(operators, data))

operators = ['+', '*', '|']
print('Total calibration result part one: ', calibration_result(operators, data))
