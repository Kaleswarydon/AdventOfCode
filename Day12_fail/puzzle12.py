from itertools import product
from functools import cache

def input_prep(input_data, fold=1):
    res = []
    for x in input_data:
        tmp = x.split()
        #row = [p for p in tmp[0].split('.') if p]
        row = tmp[0].replace('#', '0').replace('.', '1') + '?'
        row *= fold
        streaks = [int(s) for s in [*tmp[1].split(',')]] * fold
        res.append([row[:-1], streaks])
    return res

def test(input_data):
    for x in input_data:
        row = x[0]
        streaks = x[1]
        streaks_new = []

        for i in range(len(streaks)):
            found_streak = False
            for j in range(len(row)):
                if len(row[j]) == streaks[i] and row[j] == '0' * streaks[i]:
                    row.replace('0' * streaks[i], '.', 1)
                    found_streak = True
                    break
            if not found_streak:
                streaks_new.append(streaks[i])
        print(row, streaks_new)

def valid_mapping(l):
    return all([x in ['0', '?'] for x in l])

def test2(input_data):
    res = []
    for x in input_data:
        row = x[0].strip('1')
        #print(row)
        streaks = x[1]

        #print("len row", len(row))
        #print("sum streak", sum(streaks))
        #print("len streak", len(streaks))
        #print(streaks)
        buffer_inbetween = len(streaks) - 1
        #print("buffer inbetween", buffer_inbetween)
        space = len(row) - sum(streaks) - buffer_inbetween
        #print("space free", space)
        poss = (space * len(streaks)) + 1
        #print("upper bound", poss)

        pos_list = []
        for i in range(len(streaks)):
            min_pos = sum(streaks[:i]) + len(streaks[:i+1]) - 1
            max_pos = min_pos + space
            pos_list.append([min_pos, max_pos])
        #print(pos_list)
        real_possible_pos = []
        for i, pos in enumerate(pos_list):
            tmp = []
            for coord in range(pos[0], pos[1] + 1):
                if valid_mapping(row[coord:coord+streaks[i]]):
                    if coord+streaks[i] < len(row):
                        if not (row[coord+streaks[i]] == '1' or row[coord+streaks[i]] == '?'):
                            continue
                    if coord != 0:
                        if not (row[coord - 1] == '1' or row[coord - 1] == '?'):
                            continue
                    tmp.append(coord)
            real_possible_pos.append(tmp)
        #print(real_possible_pos)
        #print()
        res.append([real_possible_pos, streaks])
    return res


def puzzle_solver(input_data):
    res = []
    for x in input_data:
        row = x[0]
        streaks = x[1]
        mutables = row.count('?')
        possibilities = 0
        for i in range(2 ** mutables):
            tmp_row = row
            counter = str(format(i, "0" + str(mutables) + "b"))
            #print("counter", counter)
            for d in counter:
                #print("row1", tmp_row)
                tmp_row = tmp_row.replace('?', str(d), 1)
                #print("row2", tmp_row)
            #print(streaks, tmp_row.split('1'), [len(v) for v in tmp_row.split('1') if v])
            if streaks == [len(v) for v in tmp_row.split('1') if v]:
                possibilities += 1
        res.append([x, possibilities])

    sum_of_poss = sum(list(zip(*res))[1])
    return sum_of_poss

def puzzle_solver2(list_of_arrangements):
    res = []
    for i, a in enumerate(list_of_arrangements):
        res.append(count_possibilities(a))
        print(i, "of", len(list_of_arrangements))
    return res


def count_possibilities(l):
    streaks = l[1]
    l = l[0]
    indices = [len(x) for x in l]
    hits = 0
    for i, ind_tuple in enumerate(product(*map(range, indices))):
        combis = [x[1][x[0]] for x in list(zip(ind_tuple, l))]
        diff = [combis[j + 1] - combis[j] for j in range(len(combis) - 1)]
        #print([streaks[k+1] for k, x in enumerate(diff)])
        illegal_state_checker = True if any(x < 1 + streaks[k] for k, x in enumerate(diff)) else False
        if not illegal_state_checker:
            #print("hit", combis, diff)
            hits += 1
        else:
            #print(combis, diff, streaks)
            pass

    #print(l, hits)
    #print()
    return hits

if __name__ == '__main__':
    input_file = 'input0.txt'
    with open(input_file, 'r') as f:
        input_data = [x.strip() for x in f.readlines()]
    #print(input_data)
    print("Using", input_file)

    # puzzle1
    puzzle1_input_data = input_prep(input_data, fold=1)
    puzzle1 = puzzle_solver(puzzle1_input_data)
    print("puzzle1:", puzzle1)
    puzzle1 = test2(puzzle1_input_data)
    print("puzzle1:", puzzle_solver2(puzzle1))

    # puzzle2
    puzzle2_input_data = input_prep(input_data, fold=5)
    #print(puzzle2_input_data)
    puzzle2 = test2(puzzle2_input_data)
    print("puzzle2:", puzzle_solver2(puzzle2))
