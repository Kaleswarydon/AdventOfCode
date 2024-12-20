from icecream import ic as print
from collections import defaultdict, deque
import heapq
from typing import List
import sys
sys.path.append("../../")
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie

null = None

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
    inp = [[int(y) for y in x] for x in inp]
    inp = [sorted(list(x)) for x in list(zip(*inp))]
    return inp

class Solution:
    def puzzle1(self, input_data):
        res = 0
        for x, y in zip(*input_data):
            res += abs(x - y)
        return res

    def puzzle2(self, input_data):
        freq = defaultdict(int)
        for x in input_data[1]:
            freq[x] += 1
        res = 0
        for y in input_data[0]:
            res += y * freq[y]
        return res


if __name__ == '__main__':
    sol = Solution()

    input_puzzle_1_0_example = read_input("input_puzzle_1_0_example.txt", 'm', "   ")  # small test input
    input_puzzle_1_1 = read_input("input_puzzle_1_1.txt", 'm', "   ")  # real puzzle input
    print(sol.puzzle1(input_puzzle_1_0_example))
    print(sol.puzzle1(input_puzzle_1_1))

    input_puzzle_2_0_example = read_input("input_puzzle_2_0_example.txt", 'm', "   ")
    input_puzzle_2_1 = read_input("input_puzzle_2_1.txt", 'm', "   ")
    print(sol.puzzle2(input_puzzle_2_0_example))
    print(sol.puzzle2(input_puzzle_2_1))