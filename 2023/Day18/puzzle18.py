import numpy as np


def print_list_pretty(l):
    for x in l:
        print(x)

def get_col(matrix, row_id):
    return [matrix[i][row_id] for i in range(len(matrix))]


def transpose(m):
    if type(m[0]) is not list and type(m[0]) is not str:
        return m
    res = [get_col(m, i) for i in range(len(m[0]))]
    if type(m[0]) is str:
        return [''.join(j) for j in [get_col(m, i) for i in range(len(m[0]))]]
    else:
        return res

def walk(coords, direction):
    dirs = {
        'U': (coords[0] - 1, coords[1]),
        '3': (coords[0] - 1, coords[1]),

        'D': (coords[0] + 1, coords[1]),
        '1': (coords[0] + 1, coords[1]),

        'L': (coords[0], coords[1] - 1),
        '2': (coords[0], coords[1] - 1),

        'R': (coords[0], coords[1] + 1),
        '0': (coords[0], coords[1] + 1),
    }
    return dirs.get(direction)

def get_coords(input_data):
    coord_list = []
    current_coords = (0, 0)
    for instruction in input_data:
        direction = instruction[0]
        steps = instruction[1]
        for step in range(int(steps)):
            current_coords = walk(current_coords, direction)
            coord_list.append(current_coords)
    return coord_list

def shift_coords(coord_list):
    shift_x = 0
    shift_y = 0
    res = []
    for c in coord_list:
        if c[0] < shift_x:
            shift_x = c[0]
        if c[1] < shift_y:
            shift_y = c[1]
    for c in coord_list:
        res.append((c[0] + abs(shift_x), c[1] + abs(shift_y)))
    return res

def get_dims(coord_list):
    max_x = 0
    max_y = 0
    for c in coord_list:
        if c[0] > max_x:
            max_x = c[0]
        if c[1] > max_y:
            max_y = c[1]
    return max_x + 1, max_y + 1

def get_grid(coord_list):
    dims = get_dims(coord_list)
    grid = [['.'] * dims[1] for _ in range(dims[0])]
    for i in range(dims[0]):
        for j in range(dims[1]):
            if (i, j) in coord_list:
                grid[i][j] = '#'
    return grid

def coord_legal(coords, dims):
    return 0 <= coords[0] < dims[0] and 0 <= coords[1] < dims[1]

def get_surrounding_coords(coords):
    above = [(coords[0] - 1, coords[1] - 1), (coords[0] - 1, coords[1]), (coords[0] - 1, coords[1] + 1)]
    side = [(coords[0], coords[1] - 1), (coords[0], coords[1] + 1)]
    under = [(coords[0] + 1, coords[1] - 1), (coords[0] + 1, coords[1]),(coords[0] + 1, coords[1] + 1)]
    return above + side + under

def find_outer_coords(grid):
    dims = (len(grid), len(grid[0]))
    outer_coords = []
    for i in range(dims[0]):
        for j in range(dims[1]):
            if i == 0 or i == dims[0] - 1 or j == 0 or j == dims[1] - 1:
                if grid[i][j] == '.':
                    outer_coords.append((i, j))
    #print("outer_coords", outer_coords)
    res = []
    while outer_coords:
        o = outer_coords.pop(0)
        res.append(o)
        neighbors = [x for x in get_surrounding_coords(o) if coord_legal(x, dims)]
        for n in neighbors:
            if grid[n[0]][n[1]] == '.' and n not in res and n not in outer_coords:
                outer_coords.append(n)
        print(f"\rProcessing... Queue size: {len(outer_coords)}", end="")
    print(f"\rProcessing... Done.\n", end="")
    return res

def find_area(grid):
    dims = (len(grid), len(grid[0]))
    return (dims[0] * dims[1]) - len(find_outer_coords(grid))

#################################################################################################
# Part 2
#################################################################################################

def get_circumfence(input_data):
    steps_counter = 0
    for instruction in reversed(input_data):
        hex_num = instruction[2].strip('(').strip(')').strip('#')
        steps_counter += int(hex_num[:-1], 16)
    return steps_counter

def get_coords2(input_data): #reversed coords for shoelace
    res = 0
    current_coords = (0, 0)
    start = (0, 0)
    for i, instruction in enumerate(reversed(input_data)):
        hex_num = instruction[2].strip('(').strip(')').strip('#')
        direction = str((int(hex_num[-1]) + 2) % 4)
        steps = int(hex_num[:-1], 16)
        #print()
        #print(steps, direction)
        #print()
        for step in range(int(steps)):
            temp = current_coords
            current_coords = walk(current_coords, direction)
            res += int(np.cross(temp, current_coords)) #shoelace
        print(f"\rProcessing... {round(((i + 1) / len(input_data)) * 100, 3)} %", end="")
    print(f"\rProcessing... Done.\n", end="")
    return res

def puzzle2_solver(input_data):
    circ = get_circumfence(input_data)
    inner_area = get_coords2(input_data)
    return ((circ + inner_area) // 2) + 1


if __name__ == '__main__':
    input_file = 'input1.txt'
    with open(input_file, 'r') as f:
        input_data = [x.strip().split() for x in f.readlines()]
    print("Using", input_file)
    #print(input_data)


    # puzzle1
    raw_coords = get_coords(input_data)
    shifted_coords = shift_coords(raw_coords)
    grid = get_grid(shifted_coords)
    #print_list_pretty(grid)
    puzzle1 = find_area(grid)
    print("puzzle1:", puzzle1)

    # puzzle2
    puzzle2 = puzzle2_solver(input_data)
    print("puzzle2:", puzzle2)