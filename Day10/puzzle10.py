
def get_dir(coords, direction):
    dir_dict = {
        "up": (coords[0] - 1, coords[1]),
        "down": (coords[0] + 1, coords[1]),
        "left": (coords[0], coords[1] - 1),
        "right": (coords[0], coords[1] + 1),
    }
    return dir_dict.get(direction)


def get_connections(tile, coords):
    up = get_dir(coords, 'up')
    down = get_dir(coords, 'down')
    left = get_dir(coords, 'left')
    right = get_dir(coords, 'right')

    if tile == '|':
        return [up, down]
    elif tile == '-':
        return [left, right]
    elif tile == 'L':
        return [up, right]
    elif tile == 'J':
        return [up, left]
    elif tile == '7':
        return [left, down]
    elif tile == 'F':
        return [right, down]
    elif tile == '.':
        return None
    elif tile == 'S':
        return [up, down, left, right]
    else:
        return None

def find_start(input_data):
    for i, x in enumerate(input_data):
        for j, y in enumerate(input_data[i]):
            if y == 'S':
                return (i, j)


def find_loop(input_data):
    start = find_start(input_data)
    for coords in get_connections('S', start):
        path = [start]
        next_coords = coords
        while True:
            tile = input_data[next_coords[0]][next_coords[1]]
            if tile == 'S':
                return path
            conn = get_connections(tile, next_coords)
            #print(all([coords_valid(x, get_dims(input_data)) for x in conn]))
            if conn and all([coords_valid(x, get_dims(input_data)) for x in conn]):
                #print(conn, path[-1])
                conn.remove(path[-1])
                path.append(next_coords)
                next_coords = conn[0]
            else:
                break

def get_dims(input_data):
    return (len(input_data), len(input_data[0]))
def coords_valid(coords, dims):
    for i, x in enumerate(coords):
        if coords[i] < 0 or x >= dims[i]:
            return False
    return True

def count_symbol(field, symbol):
    res = 0
    for i, x in enumerate(field):
        for j, y in enumerate(field[i]):
            if y == symbol:
                res += 1
    return res

def determine_enclosure(input_data, path):
    tmp = [list(x) for x in input_data]
    for i, x in enumerate(tmp):
        inside = False
        for j, y in enumerate(tmp[i]):
            if (i, j) in path:
                if y in ['|', 'J', 'L', 'S']:
                    inside = not inside
            else:
                if inside:
                    tmp[i][j] = 'i'
                else:
                    tmp[i][j] = 'o'

    res = count_symbol(tmp, 'o')
    res2 = count_symbol(tmp, 'i')
    #print_list_pretty(tmp)
    return tmp, res, res2


def print_list_pretty(l):
    for x in l:
        print(x)

if __name__ == '__main__':
    with open('input1.txt', 'r') as f:
        input_data = [x.strip() for x in f.readlines()]
    #print(make_tile_dict(input_data))

    # puzzle1
    puzzle1 = find_loop(input_data)
    print("puzzle1:", int(len(puzzle1) / 2))

    # puzzle2
    puzzle2 = determine_enclosure(input_data, puzzle1)
    print("puzzle2:", puzzle2[2]) #one of those values is the solution <:^)
