import numpy as np

def print_list_pretty(l):
    for x in l:
        print(x)

def get_col(matrix, row_id):
    return [matrix[i][row_id] for i in range(len(matrix))]

def symb_to_bit(l):
    translation = {'.': 1, '#': 0}
    res = []
    for x in l:
        if x in translation.keys():
            res.append(str(translation.get(x)))
        else:
            res.append(x)
    return ''.join(res)

def bit_to_symb(l):
    translation = {'1': '.', '0': '#'}
    res = []
    for x in l:
        if x in translation.keys():
            res.append(str(translation.get(x)))
        else:
            res.append(x)
    return ''.join(res)

def input_prep(input_data):
    res = []
    block = []
    for line in input_data:
        if line:
            line = symb_to_bit(line)
            block.append(line)
        else:
            res.append(block)
            block = []
    if block:
        res.append(block)
    return res


def transpose(m):
    return [''.join(j) for j in [get_col(m, i) for i in range(len(m[0]))]]

def find_mirror(block, mode='row'):
    # find rows
    stack1 = []
    stack2 = []
    current = []
    temp = []
    for i, x in enumerate(block):
        temp.append(x)
        if stack1:
            print(stack1, x)
            xor = bin(int(x, 2) ^ int(stack1[-1], 2)).strip('0').strip('b')
            if not xor:
                xor = '0'
            eq_test = int(xor)
            if not eq_test > 1:
                stack1.pop()
                current.append(i)
        else:
            stack1 = temp[:-1]
            stack1.append(x)
            if current:
                stack2.append(current)
                current = []
    if current:
        stack2.append(current)
    res = []
    #print("asdadsda", block)
    for m in stack2:
        print("deb", m, len(block), m[-1])
        if m[-1] == len(block) - 1 or 0 in get_before(m):
            res.append(get_before(m) + m)
    print("mode", mode, "res", res, "stack2", stack2)
    print()
    return res

def get_before(indices):
    return list(reversed([indices[0] - (i + 1) for i in range(len(indices))]))
def puzzle_solver(input_data):
    rows = []
    cols = []
    for ind, block in enumerate(input_data):
        print(ind)
        #print("xd", find_mirror(block))
        rows.append(find_mirror(block))
        #print("ccccc", rows)
        cols.append(find_mirror(transpose(block), mode='col'))
        #print(rows[ind], cols[ind])
    cntr = 0
    for u, v in zip(rows, cols):
        if not u and not v:
            print(cntr, u, v)
        cntr += 1

    res = []
    for r in rows:
        for x in r:
            #print(100 * (max(x[:int(len(x) / 2)]) + 1))
            res.append(100 * (max(x[:int(len(x) / 2)]) + 1))
    for c in cols:
        for y in c:
            res.append(max(y[:int(len(y) / 2)]) + 1)
    print(len(res), len(rows), len(cols))
    return sum(res)


if __name__ == '__main__':
    input_file = 'input1.txt'
    with open(input_file, 'r') as f:
        input_data = [x.strip() for x in f.readlines()]
    input_data = input_prep(input_data)

    test = [bit_to_symb(x) for x in input_data[0]]
    print_list_pretty(test)
    print("Using", input_file)


    # puzzle1

    puzzle1 = puzzle_solver(input_data)
    print("puzzle1:", puzzle1)

    # puzzle2
    #puzzle2_coords = get_galaxy_cords(input_data, row_indices_to_expand, col_indices_to_expand, expansion_factor=1000000)
    #puzzle2 = puzzle_solver(puzzle2_coords)
    #print("puzzle2:", puzzle2)