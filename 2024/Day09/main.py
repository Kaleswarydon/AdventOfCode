from math import trunc

prnt = print
from icecream import ic as print
from collections import defaultdict, deque, Counter
import heapq
from typing import List, Counter
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
    inp = inp[0]  # any to int
    return inp

class Solution:
    def get_partial_sum(self, start, rnge):
        return ((rnge ** 2) + (2 * start * (rnge + 1)) + rnge) // 2

    #@timer
    def puzzle1(self, input_data):
        #print(input_data)
        res = []
        cntr = 0
        for i in range(len(input_data)):
            for j in range(int(input_data[i])):
                #print(i,j)
                if not i % 2:
                    res.append(cntr)
                else:
                    res.append('.')
            if not i % 2:
                cntr += 1
        l = 0
        r = len(res) - 1
        while l < r:
            while l < r and res[l] != '.':
                l += 1
            if l >= r:
                break
            res[l] = res.pop()
            r -= 1
        chksm = 0
        for m, n in enumerate(res):
            chksm += m * n
        return chksm


    #@timer
    def puzzle2(self, input_data):
        res = []
        cntr = 0
        for i in range(len(input_data)):
            for j in range(int(input_data[i])):
                # print(i,j)
                if not i % 2:
                    res.append(cntr)
                else:
                    res.append('.')
            if not i % 2:
                cntr += 1
        c_dict = defaultdict(int)
        for x in res:
            if x != '.':
                c_dict[x] += 1
        d = defaultdict(list)
        for b in range(len(res)):
            if res[b] != '.':
                d[res[b]].append(b)
        for c in sorted(c_dict.keys(), reverse=True):
            streak = 0
            for m in range(len(res)):
                if res[m] == '.':
                    streak += 1
                    if streak == c_dict[c]:
                        #print(streak,c_dict[c], c, m, m - streak + 1)
                        if m < d[c][0]:
                            for n in range(m - streak + 1, m - streak + 1 + c_dict[c]):
                                res[n] = c
                            for z in d[c]:
                                res[z] = '.'
                        break
                else:
                    streak = 0
        chksm = 0
        for m, n in enumerate(res):
            if n != '.':
                chksm += m * n
        return chksm

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