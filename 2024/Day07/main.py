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
import itertools

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
    prep_input = []
    for row in inp:
        res, fac = row.split(': ')
        fac = fac.split(' ')
        prep_input.append([int(res), [int(y) for y in fac]])
    return prep_input

class Solution:
    def __init__(self):
        self.op = {
            '+': lambda a,b: a + b,
            '*': lambda a,b: a * b,
            "||": lambda a,b: int(str(a) + str(b))
        }
    def apply_ops_to_facs(self, ops: tuple, facs: list):
        res = facs[0]
        for i in range(len(facs) - 1):
            res = self.op.get(ops[i])(res, facs[i+1])
        return res

    def puzzle_sol(self, input_data, ops: list):
        res = 0
        for i in range(len(input_data)):
            op_combs = itertools.product(ops, repeat=len(input_data[i][1]) - 1)
            while True:
                try:
                    c = next(op_combs)
                    tmp = self.apply_ops_to_facs(c, input_data[i][1])
                    if tmp == input_data[i][0]:
                        res += tmp
                        break
                except StopIteration:
                    break
        return res

    @timer
    def puzzle1(self, input_data):
        #print(input_data)
        return self.puzzle_sol(input_data, ['+', '*'])


    @timer
    def puzzle2(self, input_data):
        #print(input_data)
        return self.puzzle_sol(input_data, ['+', '*', "||"])

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