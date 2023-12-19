import operator
import math

import numpy as np


def prep_input(input_data):
    filter_dict = {}
    part_list = []
    parts = False
    part_cntr = 0
    for line in input_data:
        if line == '\n':
            parts = True
            continue
        if not parts:
            line = line.split('{')
            wf = line[0]
            line = line[1].strip().strip('}').split(',')
            tmp = []
            for rule in line:
                tmp.append(rule.split(':'))
            current_item = wf
            #print(tmp)
            for i in range(len(tmp)):
                if i:
                    current_item = wf + str(i)
                next_item = [wf + str(i + 1)]
                try:
                    if len(tmp[i + 1]) == 1:
                        next_item = tmp[i + 1]
                    op_str = '<' if '<' in tmp[i][0] else '>'
                    expanded = tmp[i][0].split(op_str)
                    filter_dict.update({current_item: [expanded[0], op_str, expanded[1], tmp[i][1], *next_item]})
                except:
                    pass
        else:
            part_dict = {}
            _ = [part_dict.update({x[0]: x[1]}) for x in [p.split('=') for p in line.strip().strip('{').strip('}').split(',')]]
            part_list.append(part_dict)
            part_cntr += 1
    return filter_dict, part_list

def filter_interpretation(fi):
    operator_dict = {
        '<=': operator.le,
        '==': operator.eq,
        '!=': operator.ne,
        '>=': operator.ge,
        '<': operator.lt,
        '>': operator.gt
    }
    return operator_dict.get(fi)

def filter_part(filter_dict, part):
    #print(filter_dict)
    actual_filter = 'in'
    while True:
        if actual_filter == 'A':
            return sum([int(x) for x in part.values()])
        if actual_filter == 'R':
            return 0
        filter_val = filter_dict.get(actual_filter)
        filter_instruction = filter_val[1]
        op_fn = filter_interpretation(filter_instruction)
        var = filter_val[0]
        val = int(filter_val[2])
        if op_fn(int(part.get(var)), int(val)):
            actual_filter = filter_val[3]
        else:
            actual_filter = filter_val[4]
        #print(actual_filter, op_fn(int(part.get(var)), int(val)), int(part.get(var)), filter_instruction, int(val), )





def puzzle1_solver(filter_dict, part_list):
    res = []
    for part in part_list:
        res.append(filter_part(filter_dict, part))
    return sum(res)

def get_mult(range_dict):
    res = 1
    for x in range_dict.keys():
        data = range_dict.get(x)
        res *= (data[1] - data[0]) + 1
    return res

def process_ranges(filter_dict, fi, part_range):
    if fi == 'A':
        return get_mult(part_range)
    if fi == 'R':
        return 0
    filter_stage = filter_dict.get(fi)
    pr0 = part_range.copy()
    pr1 = part_range.copy()
    old_val_tuple = part_range.get(filter_stage[0])
    pr0_lower = old_val_tuple[0]
    pr0_upper = int(filter_stage[2])
    pr1_lower = int(filter_stage[2])
    pr1_upper = old_val_tuple[1]
    pr_fi = [filter_stage[3], filter_stage[4]]
    if filter_stage[1] == '<':
        pr0_upper -= 1
    if filter_stage[1] == '>':
        pr1_lower += 1
        pr_fi.reverse()
    pr0.update({filter_stage[0]: (pr0_lower, pr0_upper)})
    pr1.update({filter_stage[0]: (pr1_lower, pr1_upper)})
    return process_ranges(filter_dict, pr_fi[0], pr0) + process_ranges(filter_dict, pr_fi[1], pr1)

def puzzle2_solver(filter_dict):
    min_max_ranges = [1, 4000]
    var_dict = {
        'x': (1, 4000),
        'm': (1, 4000),
        'a': (1, 4000),
        's': (1, 4000)
    }
    return process_ranges(filter_dict, 'in', var_dict)


if __name__ == '__main__':
    input_file = 'input1.txt'
    with open(input_file, 'r') as f:
        input_data = [x for x in f.readlines()]
    print("Using", input_file)
    filter_dict, part_list = prep_input(input_data)
    #print(filter_dict)


    # puzzle1
    puzzle1 = puzzle1_solver(filter_dict, part_list)
    print("puzzle1:", puzzle1)

    # puzzle2
    puzzle2 = puzzle2_solver(filter_dict)
    print("puzzle2:", puzzle2)