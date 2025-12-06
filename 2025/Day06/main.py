from math import trunc
from collections import defaultdict, deque
import heapq
from typing import List
import sys
sys.path.append("../../")
import aux_func.Algo
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
import time
import numpy as np
import operator
import functools

prnt = print
from icecream import ic as print

null = None


#-----------------------------------------------------------------------------------------------------------------------


def timer(f):
    def wrapper(*arg, **kwargs):
        start = time.time()
        res = f(*arg, **kwargs)
        stop = time.time()
        runtime = f"func {f.__name__} took {round(stop - start, 4)} seconds"
        print(runtime)
        return res
    return wrapper


def read_input(input_file, mode="line", sep=',', strip_spaces=True):
    with open(input_file, 'r') as f:
        if mode == "l":  # line
            input_data = [x.strip() if strip_spaces else x.replace('\n', '') for x in f.readlines()]
        elif mode == "m":  # matrix
            input_data = [x.strip().split(sep) if strip_spaces else x.replace('\n', '').split(sep) for x in f.readlines()]
        else:
            input_data = None
    return prepare_input(input_data)


def prepare_input(inp):  # individual input preparation
    return inp


def get_op_from_char(op_char):
    if op_char == '+':
        return operator.add
    elif op_char == '-':
        return operator.sub
    elif op_char == '*':
        return operator.mul
    elif op_char == '/':
        return operator.truediv
    else:
        return None

class Solution:
    #@timer
    def puzzle1(self, inp):
        inp = [x.split() for x in inp]
        #print(inp)
        inp_rot = aux_func.Algo.rotate_clockwise(inp)
        #print(inp_rot)
        res = 0
        for prob in inp_rot:
            op_chr = prob[0]
            vals = [int(x) for x in prob[1:]]
            op = get_op_from_char(op_chr)
            if op is not None:
                #print(functools.reduce(op, vals))
                res += functools.reduce(op, vals)
        return res

    #@timer
    def puzzle2(self, inp):
        inp = [[y for y in x] for x in inp]
        longest_line = max([len(x) for x in inp])
        #print(inp)
        #print(longest_line)
        for i in range(len(inp)):
            while len(inp[i]) < longest_line:
                inp[i].append(' ')
        #print(inp)
        inp_rot = aux_func.Algo.rotate_clockwise(inp)
        inp_rot.append([''] * longest_line)
        #print(inp_rot)
        res = 0
        tmp = []
        tmp_op_func = None
        tmp_op_symb = ''  # for debugging
        for r in inp_rot:
            l = ''.join(r)
            if l.strip():
                if l[0] in ['+', '-', '*', '/']:
                    tmp_op_func = get_op_from_char(l[0])
                    tmp_op_symb = l[0]
                #print(l)
                tmp.append(int(l[1:].strip()[::-1]))
            else:
                part_sol = functools.reduce(tmp_op_func, tmp)
                #print(tmp_op_symb, tmp, part_sol)
                res += part_sol
                tmp = []
                tmp_op_func = None
                tmp_op_symb = ''
        return res

if __name__ == '__main__':
    sol = Solution()

    input_puzzle_1_0_example = read_input("input_puzzle_1_0_example.txt", 'l', " ")  # small test input
    input_puzzle_1_1 = read_input("input_puzzle_1_1.txt", 'l', " ")  # real puzzle input
    print(sol.puzzle1(input_puzzle_1_0_example))
    print(sol.puzzle1(input_puzzle_1_1))

    input_puzzle_2_0_example = read_input("input_puzzle_1_0_example.txt", 'l', " ", strip_spaces=False)
    input_puzzle_2_1 = read_input("input_puzzle_1_1.txt", 'l', " ", strip_spaces=False)
    print(sol.puzzle2(input_puzzle_2_0_example))
    print(sol.puzzle2(input_puzzle_2_1))