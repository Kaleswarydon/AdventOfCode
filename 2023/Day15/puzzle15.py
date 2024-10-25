

def hash_func(inp):
    current = 0
    for c in inp:
        current += ord(c)
        current *= 17
        current %= 256
    return current

def puzzle1_solver(input_data):
    res = 0
    for x in input_data:
        res += hash_func(x)
    return res

def get_index(l, item):
    for i in range(len(l)):
        if l[i] == item:
            return i
    return -1

def init_seq(input_data):
    hash_map = {}
    for x in input_data:

        if '-' in x:
            info = x.split('-')
            lens_label = info[0]
            #focal_len = info[1]
            #operation = '-'
            box = hash_func(lens_label)
            box_content = hash_map.get(box)
            if not box_content:
                box_content = [[], []]
            if lens_label in box_content[0]:
                ind = get_index(box_content[0], lens_label)
                if ind != len(box_content[0]) - 1:
                    box_content = [box_content[0][:ind] + box_content[0][ind + 1:], box_content[1][:ind] + box_content[1][ind + 1:]]
                else:
                    box_content = [box_content[0][:-1], box_content[1][:-1]]
                hash_map.update({box: box_content})
        else:
            info = x.split('=')
            lens_label = info[0]
            focal_len = info[1]
            #operation = '='
            box = hash_func(lens_label)
            box_content = hash_map.get(box)
            if not box_content:
                box_content = [[], []]
            if lens_label in box_content[0]:
                ind = get_index(box_content[0], lens_label)
                box_content[1][ind] = focal_len
            else:
                box_content = [box_content[0] + [lens_label], box_content[1] + [focal_len]]
            hash_map.update({box: box_content})
    return hash_map

def puzzle2_solver(input_data):
    res = []
    hash_map = init_seq(input_data)
    for k in list(hash_map.keys()):
        box_content =  hash_map.get(k)
        if not box_content == [[], []]:
            lens_score = 0
            for ind in range(len(box_content[0])):
                lens_score += (k + 1) * (ind + 1) * int(box_content[1][ind])
            res.append(lens_score)
    return sum(res)


if __name__ == '__main__':
    input_file = 'input1.txt'
    with open(input_file, 'r') as f:
        input_data = [x.strip().split(',') for x in f.readlines()][0]
    print("Using", input_file)
    #print(input_data)


    # puzzle1
    puzzle1 = puzzle1_solver(input_data)
    print("puzzle1:", puzzle1)

    # puzzle2
    puzzle2 = puzzle2_solver(input_data)
    print("puzzle2:", puzzle2)
