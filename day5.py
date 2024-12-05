import sys
file = sys.argv[1]
with open(file) as f:
    data = f.readlines()

rules = {}
updates = []
newline = 0
for i in range(len(data)):
    if data[i] == '\n':
        newline = 1
    elif newline == 0:
        pages = [int(j) for j in data[i].strip().split('|')]
        if pages[0] in rules.keys():
            rules[pages[0]] = rules[pages[0]] + [pages[1]]
        else:
            rules[pages[0]] = [pages[1]]
    elif newline == 1:
        updates.append([int(j) for j in data[i].strip().split(',')])

right_order_idx = []
for n in range(len(updates)):
    i = 0
    rules_followed = 1
    while(rules_followed and i < len(updates[n])):
        for k in range(i+1, len(updates[n])):
            if updates[n][k] in rules.keys():
                if updates[n][i] in rules[updates[n][k]]:
                    rules_followed = 0
                    break
        i += 1
    if rules_followed:
        right_order_idx.append(n)

result = 0
for i in right_order_idx:
    middle_page_idx = len(updates[i])//2 
    result += updates[i][middle_page_idx]
print('part one result: ', result)

incorrect_order_idx = [i for i in range(len(updates)) if i not in right_order_idx]
result = 0
for i in incorrect_order_idx:
    new_update = []
    unused_pages = updates[i]
    while(unused_pages):
        for j in range(len(unused_pages)):
            #check if updates[i][j] would work 
            can_be_candidate = 1 
            for k in range(len(unused_pages)):
                if unused_pages[k] in rules.keys():
                    if unused_pages[j] in rules[unused_pages[k]]:
                        can_be_candidate = 0
            if can_be_candidate:
                new_update.append(unused_pages[j])
        unused_pages = [updates[i][n] for n in range(len(updates[i])) if updates[i][n] not in new_update] 

    middle_page_idx = len(new_update)//2 
    result += new_update[middle_page_idx]
    


print('part two result: ', result)

