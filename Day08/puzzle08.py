from math import lcm

def input_prep(input_data):
    tmp1 = [list(map(str.strip, x.split("="))) for x in input_data]
    res = {}
    for x in tmp1[2:]:
        node_name = x[0]
        node_dirs = [y.replace('(', '').replace(')', '').strip() for y in x[1].split(',')]
        res.update({node_name: node_dirs})
    instruction = tmp1[0][0]
    return [instruction, res]

def travel1(start, stop, instruction, nodes, mode='len'):
    dd = {'L': 0, 'R': 1}  # direction dict
    path = [start]
    path_len = 0
    current_node = start
    while True:
        for i in instruction:
            next_node = nodes.get(current_node)[dd.get(i)]
            if mode == 'path':
                path.append(next_node)
            else:
                path_len += 1
            current_node = next_node
            stop_con = []
            for st in stop[1]:
                stop_con.append(current_node[st] == stop[0][st])
            if all(stop_con):
                if mode == 'path':
                    return path
                else:
                    return path_len

def travel2(stop, instruction, nodes):
    dd = {'L': 0, 'R': 1}  # direction dict
    start_nodes = [x for x in nodes if x[-1] == 'A']
    res = []
    for start_node in start_nodes:
        res.append(travel1(start_node, stop, instruction, nodes))
    return res

if __name__ == '__main__':
    with open('input1.txt', 'r') as f:
        input_data = f.readlines()

    prep = input_prep(input_data)
    #print(prep)

    # puzzle1
    puzzle1 = travel1(start='AAA', stop=['ZZZ', [0, 1, 2]], instruction=prep[0], nodes=prep[1])
    print("puzzle1", puzzle1)

    # puzzle2
    puzzle2 = travel2(stop=['ZZZ', [2]], instruction=prep[0], nodes=prep[1])
    print("puzzle2", lcm(*puzzle2))
