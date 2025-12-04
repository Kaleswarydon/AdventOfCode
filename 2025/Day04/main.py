from math import trunc

import aux_func.Algo

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
import numpy as np

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
    inp = [[y for y in x] for x in inp]
    return inp


def helper(inp, cleanup=False):
    dims = (len(inp), len(inp[0]))
    res = []
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            if inp[i][j] == '@':
                inp[i][j] = 'X'  # mark paper as accessible by default
                paper_rolls = 0
                for (x, y) in aux_func.Algo.surrounding_coords((i, j)):
                    if aux_func.Algo.is_coord_valid((x, y), dims):
                        if inp[x][y] != '.':
                            paper_rolls += 1
                            if paper_rolls > 3:
                                inp[i][j] = '@'
                                break
                if inp[i][j] == 'X':
                    res.append((i, j))
    if cleanup:
        for i in range(len(inp)):
            for j in range(len(inp[0])):
                if inp[i][j] == 'X':
                    inp[i][j] = '.'
    return inp, res


class Solution:
    #@timer
    def puzzle1(self, inp):
        _, res = helper(inp)
        return len(res)

    #@timer
    def puzzle2(self, inp):
        res = 0
        while True:
            inp, removed_paper = helper(inp, True)
            if len(removed_paper) == 0:
                break
            res += len(removed_paper)
        return res


if __name__ == '__main__':
    sol = Solution()

    input_puzzle_1_0_example = read_input("input_puzzle_1_0_example.txt", 'l', " ")  # small test input
    input_puzzle_1_1 = read_input("input_puzzle_1_1.txt", 'l', " ")  # real puzzle input
    print(sol.puzzle1(input_puzzle_1_0_example))
    print(sol.puzzle1(input_puzzle_1_1))

    input_puzzle_2_0_example = read_input("input_puzzle_1_0_example.txt", 'l', " ")
    input_puzzle_2_1 = read_input("input_puzzle_1_1.txt", 'l', " ")
    print(sol.puzzle2(input_puzzle_2_0_example))
    print(sol.puzzle2(input_puzzle_2_1))