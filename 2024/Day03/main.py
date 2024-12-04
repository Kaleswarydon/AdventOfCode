from boltons.iterutils import split
from icecream import ic as print
from collections import defaultdict, deque
import heapq
from typing import List
import sys
sys.path.append("../../")
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
import re

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
    res = ""
    for x in inp:
        res += x.replace('\n', '')
    #print(res)
    return res

class Solution:
    def puzzle1(self, input_data):
        res = 0
        m = re.findall(r"mul\(\d{1,3},\d{1,3}\)", input_data)
        for e in m:
            e = e.replace("mul(", '').replace(')', '')
            fac1, fac2 = e.split(',')
            res += int(fac1) * int(fac2)
        return res

    def puzzle2(self, input_data):
        res = 0
        status = 1
        for match in re.finditer(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)", input_data):
            if match.group() == "don't()":
                status = 0
            elif match.group() == "do()":
                status = 1
            else:
                fac1, fac2 = match.group().replace("mul(", '').replace(')', '').split(',')
                res += status * int(fac1) * int(fac2)
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