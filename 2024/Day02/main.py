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
    return inp

class Solution:
    def is_valid_row(self, row):
        if row[0] < row[-1]:
            #print("inc")
            is_valid_triple = lambda x, y, z: ((1 <= y - x <= 3) and (1 <= z - y <= 3))
        elif row[0] > row[-1]:
            #print("dec")
            is_valid_triple = lambda x, y, z: ((1 <= x - y <= 3) and (1 <= y - z <= 3))
        else:
            return False
        valid = True
        for i in range(1, len(row) - 1):
            if not is_valid_triple(row[i - 1], row[i], row[i + 1]):
                valid = False
                break
        return valid

    def puzzle1(self, input_data):
        #print(input_data)
        res = 0
        for row in input_data:
            res += int(self.is_valid_row(row))
        return res

    def puzzle2(self, input_data):
        # print(input_data)
        res = 0
        for row in input_data:
            tmp = 0
            for i in range(len(row)):
                tmp += int(self.is_valid_row(row[:i] + row[i+1:]))
                if tmp:
                    break
            res += tmp
        return res

if __name__ == '__main__':
    sol = Solution()

    input_puzzle_1_0_example = read_input("input_puzzle_1_0_example.txt", 'm', " ")  # small test input
    input_puzzle_1_1 = read_input("input_puzzle_1_1.txt", 'm', " ")  # real puzzle input
    print(sol.puzzle1(input_puzzle_1_0_example))
    print(sol.puzzle1(input_puzzle_1_1))

    input_puzzle_2_0_example = read_input("input_puzzle_2_0_example.txt", 'm', " ")
    input_puzzle_2_1 = read_input("input_puzzle_2_1.txt", 'm', " ")
    print(sol.puzzle2(input_puzzle_2_0_example))
    print(sol.puzzle2(input_puzzle_2_1))