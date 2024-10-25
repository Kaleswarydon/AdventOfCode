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


def score_tile(tile, direction):
    score = 0
    if direction == 'up' or direction == 'north':
        for i, row in enumerate(tile):
            score += (len(tile) - i) * row.count('O')
    return score

def tilt(tile, direction):
    temp_tile = None
    res = []
    sort_mode_reversed = False
    transposed = False
    if direction == 'up' or direction == 'north':
        temp_tile = transpose(tile)
        #print_list_pretty(temp_tile)
        transposed = True
        sort_mode_reversed = True
    if direction == 'down' or direction == 'south':
        temp_tile = transpose(tile)
        #print_list_pretty(temp_tile)
        transposed = True
        sort_mode_reversed = False
    if direction == 'left' or direction == 'west':
        temp_tile = tile
        #print_list_pretty(temp_tile)
        transposed = False
        sort_mode_reversed = True
    if direction == 'right' or direction == 'east':
        temp_tile = tile
        #print_list_pretty(temp_tile)
        transposed = False
        sort_mode_reversed = False

    for row in temp_tile:
        split_at_stationbary_rock = row.split('#')
        tmp_row = []
        for s in split_at_stationbary_rock:
            tmp_row.append(''.join((list(sorted(list(s), reverse=sort_mode_reversed)))))
        res.append('#'.join(tmp_row))
    if transposed:
        res = transpose(res)
    return res


def tilt_cycle(tile, amount):
    temp_tile = tile
    tilt_dict = {}
    intermediate = ()
    for a in range(1, amount + 1):
        temp_tile = tilt(temp_tile, "north")
        temp_tile = tilt(temp_tile, "west")
        temp_tile = tilt(temp_tile, "south")
        temp_tile = tilt(temp_tile, "east")
        hash_val = hash(''.join(temp_tile))
        if not tilt_dict.get(hash_val):
            tilt_dict.update({hash_val: a})
        else:
            intermediate = (a, tilt_dict.get(hash_val))
            break
    return temp_tile, intermediate

def puzzle2_solver(tile, amount):
    temp_tile, intermediate = tilt_cycle(tile, amount)
    modulo = intermediate[0] - intermediate[1]
    rest = (amount - intermediate[1]) % modulo
    temp_tile, _ = tilt_cycle(temp_tile, rest)
    #print_list_pretty(temp_tile)
    return score_tile(temp_tile, "north")

if __name__ == '__main__':
    input_file = 'input1.txt'
    with open(input_file, 'r') as f:
        input_data = [x.strip() for x in f.readlines()]
    print("Using", input_file)
    #print("inp")
    #print_list_pretty(input_data)
    #print()

    # puzzle1
    #print("1")
    puzzle1 = tilt(input_data, "up")
    #print()
    #print("2")
    #print_list_pretty(puzzle1)
    puzzle1_score = score_tile(puzzle1, "up")
    print("puzzle1:", puzzle1_score)

    # puzzle2
    puzzle2 = puzzle2_solver(input_data, 1000000000)
    print("puzzle2:", puzzle2)


