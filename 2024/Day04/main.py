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
    # inp = [[int(y) for y in x] for x in inp]  # any to int
    return inp

class Solution:
    def find_word(self, input_data, search_term, directions):
        res = []
        for i in range(len(input_data)):
            for j in range(len(input_data[0])):
                if input_data[i][j] == search_term[0]:
                    for d in directions:
                        tmp_i = i
                        tmp_j = j
                        search_ind = 1
                        while 0 <= tmp_i + d[0] < len(input_data) and \
                                0 <= tmp_j + d[1] < len(input_data[0]) and \
                                search_ind < len(search_term):
                            if input_data[tmp_i + d[0]][tmp_j + d[1]] == search_term[search_ind]:
                                search_ind += 1
                                tmp_i += d[0]
                                tmp_j += d[1]
                            else:
                                break
                        if search_ind == len(search_term):
                            res.append(((i, j), d))
        return res

    def puzzle1(self, input_data):
        res = self.find_word(input_data, "XMAS", [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)])
        return len(res)

    def puzzle2(self, input_data):
        res = self.find_word(input_data, "MAS", [(-1, 1), (1, 1), (1, -1), (-1, -1)])
        x = defaultdict(int)
        for (s1, s2), (d1,d2) in res:
            x[(s1 + d1, s2 + d2)] += 1
        cntr = 0
        for m in x:
            if not x[m] % 2:
                cntr += 1
        return cntr

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