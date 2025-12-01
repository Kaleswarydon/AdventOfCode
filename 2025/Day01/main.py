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
    # inp = [[int(y) for y in x] for x in inp]  # any to int
    inp = [[-1 if x[0] == 'L' else 1, int(x[1:])] for x in inp]
    return inp

class Solution:
    #@timer
    def puzzle1(self, inp):
        #print(inp)
        curr_pos = 50
        cntr = 0
        for item in inp:
            direction, amount = item
            curr_pos = (curr_pos + (direction * amount)) % 100
            if not curr_pos:
                cntr += 1
        return cntr

    #@timer
    def puzzle2(self, inp):
        print(inp)

if __name__ == '__main__':
    sol = Solution()

    input_puzzle_1_0_example = read_input("input_puzzle_1_0_example.txt", 'l', " ")  # small test input
    input_puzzle_1_1 = read_input("input_puzzle_1_1.txt", 'l', " ")  # real puzzle input
    print(sol.puzzle1(input_puzzle_1_0_example))  # 3
    print(sol.puzzle1(input_puzzle_1_1))

    input_puzzle_2_0_example = read_input("input_puzzle_2_0_example.txt", 'l', " ")
    input_puzzle_2_1 = read_input("input_puzzle_2_1.txt", 'l', " ")
    #print(sol.puzzle2(input_puzzle_2_0_example))
    #print(sol.puzzle2(input_puzzle_2_1))