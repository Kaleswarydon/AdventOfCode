from math import trunc

prnt = print
from icecream import ic as print
from collections import defaultdict, deque
import heapq
from typing import List
import sys
sys.path.append("../../")
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
import time

null = None

def timer(f):
    def wrapper(*arg, **kwargs):
        start = time.time()
        res = f(*arg, **kwargs)
        stop = time.time()
        runtime = f"func {f.__name__} took {round(stop - start, 4)} seconds"
        print(runtime)
        return res
    return wrapper

def read_input(input_file, mode="line", sep=','):
    with open(input_file, 'r') as f:
        if mode == "l":  # line
            input_data = [x.strip() for x in f.readlines()]
        elif mode == "m":  # matrix
            input_data = [x.strip().split(sep) for x in f.readlines()]
        else:
            input_data = None
    return prepare_input(input_data)

def prepare_input(inp):  # individual input preparation
    res = []
    curr = defaultdict(list)
    while inp:
        data = inp.pop()
        if ": " not in data:
            res.append(curr)
            curr = defaultdict(list)
            continue
        tmp = data.split(": ")
        data_descriptor = tmp[0].replace("Button ", '')[0]
        data_coords = [int(x) for x in tmp[1].replace('X', '').replace('Y', '').replace('=', '').split(', ')]
        curr[data_descriptor] = data_coords
    res.append(curr)
    return res[::-1]

class Solution:
    @timer
    def puzzle1(self, input_data):
        button_cost = {'A': 3, 'B': 1}
        res = []
        for m in input_data:
            # lazily brute force linear eq with 2 unknown (< 100 each) to be able to move to part2
            min_cost = float("inf")
            for a in range(100):
                for b in range(100):
                    if (a * m['A'][0]) + (b * m['B'][0]) == m['P'][0] and \
                        (a * m['A'][1]) + (b * m['B'][1]) == m['P'][1]:
                        cost = (a * button_cost.get('A')) + (b * button_cost.get('B'))
                        if cost < min_cost:
                            min_cost = cost
            res.append(min_cost)
        #print(res)
        return sum([x for x in res if type(x) is int])

    @timer
    def puzzle2(self, input_data):
        for x in input_data:
            x['P'][0] += 10000000000000
            x['P'][1] += 10000000000000
        button_cost = {'A': 3, 'B': 1}
        res = 0
        for m in input_data:
            # cramers rule as brute force isnt feasible anymore
            a1 = m['A'][0]
            a2 = m['A'][1]
            b1 = m['B'][0]
            b2 = m['B'][1]
            c1 = m['P'][0]
            c2 = m['P'][1]
            det_x = (b2 * c1) - (b1 * c2)
            det_y = (a1 * c2) - (a2 * c1)
            det_coeff = ((a1 * b2) - (a2 * b1))
            x, xm = divmod(det_x, det_coeff)
            y, ym = divmod(det_y, det_coeff)
            if xm or ym:  # if det_x / det_coeff or det_y / det_coeff isnt an int = no solution in a discrete grid
                continue
            res += (x * button_cost.get('A')) + (y * button_cost.get('B'))
        return res

if __name__ == '__main__':
    sol = Solution()

    input_puzzle_1_0_example = read_input("input_puzzle_1_0_example.txt", 'l', " ")  # small test input
    input_puzzle_1_1 = read_input("input_puzzle_1_1.txt", 'l', " ")  # real puzzle input
    print(sol.puzzle1(input_puzzle_1_0_example))
    print(sol.puzzle1(input_puzzle_1_1))

    input_puzzle_2_0_example = read_input("input_puzzle_2_0_example.txt", 'l', " ")
    input_puzzle_2_1 = read_input("input_puzzle_2_1.txt", 'l', " ")
    print(sol.puzzle2(input_puzzle_2_0_example))
    print(sol.puzzle2(input_puzzle_2_1))