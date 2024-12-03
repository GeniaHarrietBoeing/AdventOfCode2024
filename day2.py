import sys

file = sys.argv[1]
with open(file) as f:
    data = f.readlines()
data = [[int(i) for i in data[j].split()] for j in range(len(data))]

nr_safe_reports = len(data)
for i in range(len(data)):
    diff = []
    for j in range(1, len(data[i])):
        tmp = data[i][j] - data[i][j-1]
        if abs(tmp) > 3 or abs(tmp) == 0:
            nr_safe_reports -= 1
            break
        if j >= 2:
            if tmp/abs(tmp) != diff[-1]/abs(diff[-1]):
                nr_safe_reports -= 1
                break
        diff.append(tmp)

print('Number of safe reports: ', nr_safe_reports)
        

def differences(report):
    diff = []
    for j in range(1, len(report)):
        tmp = report[j] - report[j-1]
        diff.append(tmp)
    return diff

def rule_signs(diff):
    nr_rule_violations = 0
    for i in range(1, len(diff)):
        if diff[i-1] != 0 and diff[i] != 0:
            if diff[i-1]/abs(diff[i-1]) != diff[i]/abs(diff[i]):
                nr_rule_violations += 1
    return nr_rule_violations

def rule_magnitude_change(diff):
    nr_rule_violations = 0
    for i in diff:
        if abs(i) == 0 or abs(i) > 3:
            nr_rule_violations += 1
    return nr_rule_violations

nr_safe_reports = 0
for i in range(len(data)):
    diff = differences(data[i])
    nr_rule_violations = rule_signs(diff) + rule_magnitude_change(diff)
    if nr_rule_violations > 0:
        for j in range(len(data[i])):
            tmp_data = [data[i][k] for k in range(len(data[i])) if k != j]
            diff = differences(tmp_data)
            nr_rule_violations = rule_signs(diff) + rule_magnitude_change(diff)
            if nr_rule_violations == 0:
                nr_safe_reports += 1 
                break
    else:
        nr_safe_reports += 1 


print('Number of safe reports with Problem Dampener: ', nr_safe_reports)
    

