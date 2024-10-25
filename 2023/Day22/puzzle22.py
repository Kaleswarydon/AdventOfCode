from copy import deepcopy



def get_coord_from_range(coord_range): #get all distinct coords for one block from its range. only works for positive coords / coord ranges
    min_coord = coord_range[0]
    max_coord = coord_range[1]
    res = []
    for i in range(len(min_coord)):
        tmp = min_coord.copy()
        for j in range(min_coord[i] + 1, max_coord[i]):
            tmp[i] = j
            res.append(tmp.copy())
    return [min_coord] + res + [max_coord]


def input_prep(input_data): #transform input data in more convenient format
    res = {}
    for i, x in enumerate(input_data):
        tmp = []
        for y in x.strip().split('~'):
            tmp.append(list(map(int, y.split(','))))
        res.update({i + 1: get_coord_from_range(tmp)})
    return res


def get_dims_from_dict(prep): #get grid dimensions from input data
    x_max = 0
    y_max = 0
    z_max = 0
    for i in prep.keys():
        for coord in prep.get(i):
            if coord[0] > x_max:
                x_max = coord[0]
            if coord[1] > y_max:
                y_max = coord[1]
            if coord[2] > z_max:
                z_max = coord[2]
    return (x_max, y_max, z_max)


def get_dims_from_grid(grid): #get grid dimensions from grid
    return (len(grid), len(grid[0]), len(grid[0][0]))


def get_grid(prep): # construct grid from input data
    dims = get_dims_from_dict(prep)
    grid = [[['' for z in range(dims[2] + 1)] for y in range(dims[1] + 1)] for x in range(dims[0] + 1)]
    return grid


def populate_grid(grid, prep): #populate (empty) grid with blocks
    for i in prep.keys():
        for coord in prep.get(i):
            grid[coord[0]][coord[1]][coord[2]] = i
    return grid


def get_blocks_from_grid(grid): #scan grid for blocks
    res = {}
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for z in range(len(grid[0][0])):
                block_id = grid[x][y][z]
                if block_id:
                    coord_list = res.get(block_id)
                    if coord_list:
                        coord_list.append([x, y, z])
                    else:
                        coord_list = [[x, y, z]]
                    res.update({block_id: coord_list})
    return res


def get_block_parts_in_z_plane(grid, z): #get all blocks that have at least one part in given z plane
    assert 0 <= z <= len(grid[0][0])
    res = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            cell_val = grid[x][y][z]
            if cell_val:
                res.append(cell_val)
    return set(res)

def is_legal_coord(coord, dims): # disallow negative vals for all and also 0 for z
    return 0 <= coord[0] <= dims[0] and 0 <= coord[1] <= dims[1] and 0 < coord[2] <= dims[2]

def apply_gravity(grid):
    res_grid = deepcopy(grid)
    coord_dict = get_blocks_from_grid(res_grid)
    moved_blocks = []
    dims = get_dims_from_grid(res_grid)
    for z in range(1, len(res_grid[0][0])):
        blocks_in_plane = get_block_parts_in_z_plane(res_grid, z)
        if blocks_in_plane:
            for block_id in blocks_in_plane:
                if block_id in moved_blocks: #probably useless
                    continue
                moved_blocks.append(block_id)
                while True: #let a block fall as far as possible
                    new_block_coords = []
                    for coord in coord_dict.get(block_id):
                        new_block_coords.append([coord[0], coord[1], coord[2] - 1])
                    #if new coords are not occupied (empty or taken by other blocks, own block is fine)
                    if all([is_legal_coord(c, dims) and (res_grid[c[0]][c[1]][c[2]] == block_id or not res_grid[c[0]][c[1]][c[2]]) for c in new_block_coords]):
                        #delete old block coords from grid
                        for old_coord in coord_dict.get(block_id):
                            res_grid[old_coord[0]][old_coord[1]][old_coord[2]] = ''
                        #update block coords in dict
                        coord_dict.update({block_id: new_block_coords})
                        #set new coords in grid
                        for new_coord in coord_dict.get(block_id):
                            res_grid[new_coord[0]][new_coord[1]][new_coord[2]] = block_id
                    else:
                        break
    return res_grid


def puzzle1_solver(grid):
    coord_dict = get_blocks_from_grid(grid)
    remove_block_counter = 0 #counts blocks that can be removed
    for block_id in coord_dict.keys():
        tmp_grid_deleted_block = deepcopy(grid)
        for c in coord_dict.get(block_id):
            tmp_grid_deleted_block[c[0]][c[1]][c[2]] = ''
        tmp_grid_gravity = apply_gravity(tmp_grid_deleted_block)
        if tmp_grid_deleted_block == tmp_grid_gravity:
            remove_block_counter += 1
    return remove_block_counter


def get_block_diff(blocks1: dict, blocks2: dict): #get number of different values of 2 dicts with the same keys
    res = 0
    for k in blocks1.keys():
        if blocks1.get(k) != blocks2.get(k) and blocks1.get(k) and blocks2.get(k): #assuming dict keys are the same and exist
            res += 1
    return res


def puzzle2_solver(grid): #could be merged with puzzle1_solver
    res = 0
    coord_dict = get_blocks_from_grid(grid)
    for block_id in coord_dict.keys():
        tmp_grid_deleted_block = deepcopy(grid)
        for c in coord_dict.get(block_id):
            tmp_grid_deleted_block[c[0]][c[1]][c[2]] = ''
        tmp_grid_gravity = apply_gravity(tmp_grid_deleted_block)
        if tmp_grid_deleted_block != tmp_grid_gravity:
            tmp_coord_dict = get_blocks_from_grid(tmp_grid_gravity)
            res += get_block_diff(coord_dict, tmp_coord_dict)
    return res

if __name__ == '__main__':
    input_file = 'input1.txt'
    with open(input_file, 'r') as f:
        input_data = [x.strip() for x in f.readlines()]
    prep = input_prep(input_data)
    grid = populate_grid(get_grid(prep), prep)
    grid = apply_gravity(grid)
    print("Using", input_file)

    # puzzle1
    puzzle1 = puzzle1_solver(grid)
    print("puzzle1:", puzzle1)

    # puzzle2
    puzzle2 = puzzle2_solver(grid)
    print("puzzle2:", puzzle2)
