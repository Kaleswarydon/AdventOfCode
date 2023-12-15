
def get_pairwise_diff(val_list):
    res = []
    i = 0
    while True:
        try:
            res.append(val_list[i + 1] - val_list[i])
            i += 1
        except:
            return res

def compute_sequences(input_list):
    tmp = input_list
    while any(tmp[-1]):
        tmp.append(get_pairwise_diff(tmp[-1]))
    return tmp

def extrapolate1(seq_list):
    return sum([x[-1] for x in seq_list])

def extrapolate2(seq_list):
    res = [0.0]
    for s in list(reversed(seq_list[:-1])):
        res.append(s[0] - res[-1])
    return res[-1]

def puzzle1_solver(input_data):
    res = []
    for x in input_data:
        res.append(extrapolate1(compute_sequences([x])))
    return res

def puzzle2_solver(input_data):
    res = []
    for x in input_data:
        res.append(extrapolate2(compute_sequences([x])))
    return res

if __name__ == '__main__':
    with open('input1.txt', 'r') as f:
        input_data = [[float(y) for y in x.strip().split()] for x in f.readlines()]

    # puzzle1
    print("puzzle1:", int(sum(puzzle1_solver(input_data))))

    # puzzle2
    print("puzzle2:", int(sum(puzzle2_solver(input_data))))
