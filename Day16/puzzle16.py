

def edge_legal(edge, dims):
    return coord_legal(edge.get('to'), dims)


def coord_legal(coords, dims):
    return 0 <= coords[0] < dims[0] and 0 <= coords[1] < dims[1]


def get_next_coords(coords: tuple, direction: str):
    if direction == 'u':  # up
        return coords[0] - 1, coords[1]
    if direction == 'd':  # down
        return coords[0] + 1, coords[1]
    if direction == 'l':  # left
        return coords[0], coords[1] - 1
    if direction == 'r':  # right
        return coords[0], coords[1] + 1


def get_next_dirs(tile_symb: str, prev_dir: str):
    directions = []
    if [tile_symb, prev_dir] in [['.', 'u'],
                                 ['/', 'r'],
                                 ['?', 'l'],
                                 ['|', 'u'], ['|', 'l'],  ['|', 'r'],
                                 ]:
            directions.append('u')
    if [tile_symb, prev_dir] in [['.', 'd'],
                                 ['/', 'l'],
                                 ['?', 'r'],
                                 ['|', 'd'], ['|', 'l'],  ['|', 'r'],
                                 ]:
            directions.append('d')
    if [tile_symb, prev_dir] in [['.', 'l'],
                                 ['/', 'd'],
                                 ['?', 'u'],
                                 ['-', 'u'], ['-', 'd'], ['-', 'l']
                                 ]:
            directions.append('l')
    if [tile_symb, prev_dir] in [['.', 'r'],
                                 ['/', 'u'],
                                 ['?', 'd'],
                                 ['-', 'u'], ['-', 'd'], ['-', 'r']
                                 ]:
        directions.append('r')
    return directions


def get_next_edges(edge: dict, input_data: list):
    res = []
    next_dirs = get_next_dirs(input_data[edge.get('to')[0]][edge.get('to')[1]], edge.get('dir'))
    for d in next_dirs:
        res.append({'from': edge.get('to'), 'to': get_next_coords(edge.get('to'), d), 'dir': d})
    return res


def puzzle1_solver(input_data: list, start_edge: dict):
    dims = (len(input_data), len(input_data[0]))
    graph = []
    tmp_edge_list = [start_edge]
    while tmp_edge_list:
        actual_edge = tmp_edge_list.pop(0)
        for e in get_next_edges(actual_edge, input_data):
            if edge_legal(e, dims) and e not in graph:
                tmp_edge_list.extend([e])
        if actual_edge not in graph:
            graph.append(actual_edge)
    res = set()
    for ed in graph:
        res.add(ed.get('from'))
        res.add(ed.get('to'))
    return len(res)


def puzzle2_solver(input_data):
    res = []
    start_edges = []
    dims = (len(input_data), len(input_data[0]))
    for i in range(dims[0]):
        for j in range(dims[1]):
            if i == 0 or i == dims[0] - 1 and j == 0 or j == dims[1] - 1:
                if i == 0:
                    start_edges.append({'from': (i, j), 'to': (i, j), 'dir': 'd'})
                if i == dims[0] - 1:
                    start_edges.append({'from': (i, j), 'to': (i, j), 'dir': 'u'})
                if j == 0:
                    start_edges.append({'from': (i, j), 'to': (i, j), 'dir': 'r'})
                if j == dims[1] - 1:
                    start_edges.append({'from': (i, j), 'to': (i, j), 'dir': 'l'})
    for ind, s in enumerate(start_edges):
        res.append(puzzle1_solver(input_data, s))
        print(f"\rProcessing... {round(((ind + 1) / len(start_edges)) * 100, 3)} %", end="")
    print(f"\rProcessing... Done.\n", end="")
    return max(res)


if __name__ == '__main__':
    input_file = 'input1.txt'
    with open(input_file, 'r') as f:
        input_data = [list(x.replace('\\', '?').strip()) for x in f.readlines()]
    print("Using", input_file)
    #print(input_data)


    # puzzle1
    puzzle1 = puzzle1_solver(input_data, {'from': (0, 0), 'to': (0, 0), 'dir': 'r'})
    print("puzzle1:", puzzle1)

    # puzzle2
    puzzle2 = puzzle2_solver(input_data)
    print("puzzle2:", puzzle2)
