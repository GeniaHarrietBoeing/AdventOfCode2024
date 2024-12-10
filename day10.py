import sys
file = sys.argv[1]
with open(file) as f:
    data = f.readlines()
data = [[int(i) for i in list(data[j].strip())] for j in range(len(data))]

potential_trailheads = []
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 0:
            potential_trailheads.append([i,j])


def get_surrounding_matches(n, pos):
    matches = []

    if pos[0]-1 >= 0:
        if data[pos[0]-1][pos[1]] == n:
            matches.append([pos[0]-1, pos[1]])
    if pos[0]+1 < len(data):
        if data[pos[0]+1][pos[1]] == n:
            matches.append([pos[0]+1, pos[1]])
    if pos[1]-1 >= 0:
        if data[pos[0]][pos[1]-1] == n:
            matches.append([pos[0], pos[1]-1])
    if pos[1]+1 < len(data[0]):
        if data[pos[0]][pos[1]+1] == n:
            matches.append([pos[0], pos[1]+1])

    return matches

trailheads_score = 0
for i in range(len(potential_trailheads)):
    path_found = True
    height = 1
    trails = [potential_trailheads[i]]
    #print('starting point: ', potential_trailheads[i])
    while(path_found):
        #print('height', height)
        #print('trails', trails)
        next_steps = []
        if height == 10:
            trailheads_score += len(trails)
            break
        for k in range(len(trails)):
            matches = get_surrounding_matches(height, trails[k])
            #print('matches for ', trails[k], matches)
            if matches:
                for l in matches:
                    if l not in next_steps:
                        next_steps.append(l)
        if not next_steps:
            path_found = False
       # print('next steps: ', next_steps)
        trails = next_steps
        height += 1
print('Part 1 ', trailheads_score)

    

distinct_trails = 0
for i in range(len(potential_trailheads)):
    path_found = True
    height = 1
    trails = [potential_trailheads[i]]
    #print('starting point: ', potential_trailheads[i])
    while(path_found):
        #print('height', height)
        #print('trails', trails)
        next_steps = []
        if height == 10:
            distinct_trails += len(trails)
            break
        for k in range(len(trails)):
            matches = get_surrounding_matches(height, trails[k])
            #print('matches for ', trails[k], matches)
            if matches:
                for l in matches:
                    next_steps.append(l)
        if not next_steps:
            path_found = False
       # print('next steps: ', next_steps)
        trails = next_steps
        height += 1
print('Part 2 ', distinct_trails)
