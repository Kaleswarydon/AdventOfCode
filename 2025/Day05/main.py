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
    res = [[], []]
    for x in inp:
        if '-' in x:
            res[0].append([int(y) for y in x.split('-')])
        elif x:
            res[1].append(int(x))
    return res

class Solution:
    #@timer
    def puzzle1(self, inp):
        #print(inp)
        res = 0
        for x in inp[1]:
            for y, z in inp[0]:
                if y <= x <= z:
                    res += 1
                    break
        return res

    #@timer
    def puzzle2(self, inp):
        #print(inp)
        stack = []
        ranges = []
        for y, z in inp[0]:
            heapq.heappush(stack, (y, z))
        while stack:
            [y, z] = heapq.heappop(stack)
            if ranges and ranges[-1][0] <= y <= ranges[-1][1]:
                if z >= ranges[-1][1]:
                    ranges[-1][1] = z
            else:
                ranges.append([y, z])
        res = 0
        for r in ranges:
            res += (r[1] - r[0]) + 1
        return res

if __name__ == '__main__':
    sol = Solution()

    input_puzzle_1_0_example = read_input("input_puzzle_1_0_example.txt", 'l', " ")  # small test input
    input_puzzle_1_1 = read_input("input_puzzle_1_1.txt", 'l', " ")  # real puzzle input
    print(sol.puzzle1(input_puzzle_1_0_example))
    print(sol.puzzle1(input_puzzle_1_1))

    input_puzzle_2_0_example = read_input("input_puzzle_2_0_example.txt", 'l', " ")
    input_puzzle_2_1 = read_input("input_puzzle_2_1.txt", 'l', " ")
    print(sol.puzzle2(input_puzzle_1_0_example))
    print(sol.puzzle2(input_puzzle_1_1))