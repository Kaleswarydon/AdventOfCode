import math


def input_parser(input_data: list):
    number_list = []
    special_char_list = []
    tmp_number = ''
    tmp_pos = []
    dims = ()
    for line_index, line in enumerate(input_data):
        symb_index = 0
        for symb in line:
            try:
                _ = int(symb)
                tmp_number += symb
                tmp_pos.append((line_index, symb_index))
            except:
                if tmp_number:
                    number_list.append([str(tmp_pos[0]) + "_" + tmp_number, tmp_pos])
                    tmp_number = ''
                    tmp_pos = []
                if symb != '.':
                    special_char_list.append([symb, [(line_index, symb_index)]])
            symb_index += 1
        dims = (line_index + 1, symb_index)
    number_dict = make_pos_dict(number_list)
    special_char_dict = make_pos_dict(special_char_list)
    return number_dict, special_char_dict, dims

def make_pos_dict(coord_list: list):
    pos_dict = {}
    for entry in coord_list:
        for coord in entry[1]:
            pos_dict.update({coord: entry[0]})
    return pos_dict
def get_adjacent_coords(coord: tuple, dims: tuple, with_center=False):
    if coord[0] >= dims[0] or coord[1] >= dims[1]:
        return []
    adjacent_coords = []
    for x in range(coord[0] - 1, coord[0] + 2):
        for y in range(coord[1] - 1, coord[1] + 2):
            if with_center and [x, y] == coord:
                continue
            if not (x < 0 or y < 0) and not (x >= dims[0] or y >= dims[1]):
                adjacent_coords.append((x, y))
    return adjacent_coords

def get_adjacency(number_dict: dict, special_char_dict: dict, dims: tuple):
    adjacency_dict = {}
    number_has_adj_special_char = []
    for s in special_char_dict.keys():
        adj = get_adjacent_coords(s, dims, with_center=True)
        for c in adj:
            if c in number_dict.keys():
                number_has_adj_special_char.append(number_dict.get(c))
                tmp = []
                if adjacency_dict.get(str(s) + '_' + special_char_dict.get(s)):
                    tmp = adjacency_dict.get(str(s) + '_' + special_char_dict.get(s))
                tmp.append(number_dict.get(c))
                adjacency_dict.update({str(s) + '_' + special_char_dict.get(s): list(set(tmp))})
    return adjacency_dict

def puzzle1_res_extractor(adjacency_dict: dict):
    res = []
    for numbers in adjacency_dict.values():
        for n in numbers:
            res.append(n)
    res = list(set(res))
    res = [int(x.split('_')[1]) for x in res]
    return sum(res)

def puzzle2_res_extractor(adjacency_dict: dict):
    res = []
    for spec in adjacency_dict.keys():
        if spec.split('_')[1] == '*' and len(adjacency_dict.get(spec)) == 2:
            tmp = math.prod([int(x.split('_')[1]) for x in adjacency_dict.get(spec)])
            res.append(tmp)
    return sum(res)

if __name__ == '__main__':
    with open('input1.txt', 'r') as f:
        input_data = f.readlines()
        input_data = [x.strip() for x in input_data]
    number_dict, special_char_dict, dims = input_parser(input_data)
    adj_res = get_adjacency(number_dict, special_char_dict, dims)
    print(adj_res)
    #puzzle1
    puzzle1 = puzzle1_res_extractor(adj_res)
    print('puzzle1:', puzzle1)

    #puzzle2
    puzzle2 = puzzle2_res_extractor(adj_res)
    print('puzzle2:', puzzle2)