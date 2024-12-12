import sys
file = sys.argv[1]
with open(file) as f: 
    data = f.readlines()

def get_neighbours(plant_type, pos_x, pos_y):
    neighbours = []
    if pos_x - 1 >= 0:
        if data[pos_x - 1][pos_y] == plant_type:
            neighbours.append([pos_x-1, pos_y])

    if pos_y - 1 >= 0:
        if data[pos_x][pos_y - 1] == plant_type:
            neighbours.append([pos_x, pos_y - 1])

    if pos_x + 1 < len(data):
        if data[pos_x + 1][pos_y] == plant_type:
            neighbours.append([pos_x + 1, pos_y])

    if pos_y + 1 < len(data[0]):
        if data[pos_x][pos_y + 1] == plant_type:
            neighbours.append([pos_x, pos_y + 1])


    #getting perimeter information
    if not neighbours:
        sides = 4
        perimeter = 4
    if len(neighbours) == 4:
        #might be an inside corner
        #check diagonals
        #  X
        # XXX
        #  X
        perimeter = 0
        sides = 0
        for i in [-1,1]:
            for j in [-1,1]:
                if data[pos_x+i][pos_y+j] != plant_type:
                    sides += 1

    if len(neighbours) == 3:
        # might also be an inside corner
        # the tetris piece in question and all its rotations:
        # X
        # XX
        # X
        perimeter = 1
        sides = 0
        x_values = [i[0] for i in neighbours]
        y_values = [i[1] for i in neighbours]
        min_x = min(x_values)
        max_x = max(x_values)
        min_y = min(y_values)
        max_y = max(y_values)
        if max_y - min_y == 2:
            #down oriented tetris piece
            if max_x == pos_x:
                if data[min_x][min_y] != plant_type:
                    sides += 1
                if data[min_x][max_y] != plant_type:
                    sides += 1
            else: 
                if data[max_x][min_y] != plant_type:
                    sides += 1
                if data[max_x][max_y] != plant_type:
                    sides += 1
        else:
            #left oriened tetris piece
            if max_y == pos_y:
                if data[min_x][min_y] != plant_type:
                    sides += 1
                if data[max_x][min_y] != plant_type:
                    sides += 1
            #right tetris piece
            else: 
                if data[min_x][max_y] != plant_type:
                    sides += 1
                if data[max_x][max_y] != plant_type:
                    sides += 1


    if len(neighbours) == 1:
        perimeter = 3
        sides = 2
    if len(neighbours) == 2:
        #only if there is a corner add one side

        if neighbours[0][0] == neighbours[1][0] or neighbours[0][1] == neighbours[1][1]:
            sides = 0
        else:
            sides = 1

            #could ALSO be an inside corner a la:
            # X
            # XX

            x_values = [i[0] for i in neighbours]
            y_values = [i[1] for i in neighbours]
            max_x = max(x_values)
            min_x = min(x_values)
            max_y = max(y_values)
            min_y = min(y_values)

            for i in [min_x, max_x]:
                for j in [min_y, max_y]:
                    if data[i][j] != plant_type:
                        sides += 1
                        break

        perimeter = 2
    
        
    return neighbours, perimeter, sides

    

perimeter_cost = 0
sides_cost = 0

data = [list(data[i].strip()) for i in range(len(data))]
visited = [[0]*len(data[0]) for i in range(len(data))]
not_all_visited = True

pos_x = 0
pos_y = 0
while(not_all_visited):
    plant_type = data[pos_x][pos_y]
    plot_positions = [[pos_x, pos_y]]
    unvisited_plot_positions = [[pos_x, pos_y]]

    unfinished_plot = True
    perimeter = 0
    sides = 0

    while(unfinished_plot):
        if unvisited_plot_positions: 
            pos_x = unvisited_plot_positions[0][0]
            pos_y = unvisited_plot_positions[0][1]
            neighbours, loc_perimeter, loc_sides = get_neighbours(plant_type, pos_x, pos_y)
            perimeter += loc_perimeter
            sides += loc_sides


            unvisited_plot_positions.pop(0)
            visited[pos_x][pos_y] = 1

            
            if neighbours: 
                for i in range(len(neighbours)):
                    if visited[neighbours[i][0]][neighbours[i][1]] == 0:
                        plot_positions.append(neighbours[i])
                        unvisited_plot_positions.append(neighbours[i])
                        visited[neighbours[i][0]][neighbours[i][1]] = 1
        else:
            unfinished_plot = False


    perimeter_cost += len(plot_positions)*perimeter
    sides_cost += len(plot_positions)*sides
       
    not_all_visited = False
    for i in range(len(visited)):
        for j in range(len(visited)):
            if visited[i][j] == 0:
                pos_x = i
                pos_y = j
                not_all_visited = True

    
    #not_all_visited = False
print('Total cost of fence in relation to the perimeter: ', perimeter_cost)
print('Total cost of fence in relation to the number of sides: ', sides_cost)


