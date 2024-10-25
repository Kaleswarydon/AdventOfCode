

def print_list_pretty(l):
    for x in l:
        print(x)

def get_col(matrix, row_id):
    return [matrix[i][row_id] for i in range(len(matrix))]

def expand_universe(input_data):
    col_indices_to_expand = []
    row_indices_to_expand = []
    for j in range(len(input_data[0])): #cols
        r = get_col(input_data, j)
        if len(set(r)) == 1:
            col_indices_to_expand.append(j)
    for i, x in enumerate(input_data): #rows
        if len(set(x)) == 1:
            row_indices_to_expand.append(i)
    return row_indices_to_expand, col_indices_to_expand

def get_galaxy_cords(input_data, row_indices_to_expand, col_indices_to_expand, expansion_factor=2):
    res = {}
    cntr = 1
    for i, x in enumerate(input_data):
        for j, y in enumerate(x):
            if y == '#':
                coords = [i, j]
                expanded_coords = [i, j]
                for row in row_indices_to_expand:
                    if coords[0] > row:
                        expanded_coords[0] += expansion_factor - 1
                for col in col_indices_to_expand:
                    if coords[1] > col:
                        expanded_coords[1] += expansion_factor - 1
                res.update({cntr: expanded_coords})
                cntr += 1
    return res

def get_dist(coords1, coords2):
    res = []
    for x, y in zip(coords1, coords2):
        res.append(abs(x - y))
    return sum(res)

def puzzle_solver(coords):
    res = 0
    ind = list(coords.keys())
    for i in range(len(ind)):
        for j in range(i, len(ind)):
            res += get_dist(coords.get(ind[i]), coords.get(ind[j]))
    return res

if __name__ == '__main__':
    input_file = 'input1.txt'
    with open(input_file, 'r') as f:
        input_data = [x.strip() for x in f.readlines()]
    print("Using", input_file)
    row_indices_to_expand, col_indices_to_expand = expand_universe(input_data)

    # puzzle1
    puzzle1_coords = get_galaxy_cords(input_data, row_indices_to_expand, col_indices_to_expand, expansion_factor=2)
    puzzle1 = puzzle_solver(puzzle1_coords)
    print("puzzle1:", puzzle1)

    # puzzle2
    puzzle2_coords = get_galaxy_cords(input_data, row_indices_to_expand, col_indices_to_expand, expansion_factor=1000000)
    puzzle2 = puzzle_solver(puzzle2_coords)
    print("puzzle2:", puzzle2)