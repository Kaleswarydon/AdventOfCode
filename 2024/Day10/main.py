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
    inp = [[int(y) for y in x] for x in inp]  # any to int
    return inp

class Solution:
    def find_all_start_coords(self, grid, start_val):
        res = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == start_val:
                    res.append((i,j))
        return res

    def is_coord_valid(self, coord, dims):
        return 0 <= coord[0] < dims[0] and 0 <= coord[1] < dims[1]

    def custom_bfs(self, grid, start_coord, stop_val):  # proceed path if next value is current value + 1
        end_coords = set()
        trail_count = 0
        dims = (len(grid), len(grid[0]))
        directions = [(-1,0), (0, 1), (1, 0), (0, -1)]
        q = deque([start_coord])
        while q:
            curr = q.popleft()
            if grid[curr[0]][curr[1]] == stop_val:
                end_coords.add(curr)
                trail_count += 1
                #print(res, curr, grid[curr[0]][curr[1]])
                continue
            for d in directions:
                potential_next = (curr[0] + d[0], curr[1] + d[1])
                if self.is_coord_valid(potential_next, dims) and \
                    grid[potential_next[0]][potential_next[1]] == grid[curr[0]][curr[1]] + 1:
                    q.append(potential_next)
        #print(res)
        return len(end_coords), trail_count

    def solver(self, input_data):
        start_coords = self.find_all_start_coords(input_data, 0)
        # print(start_coords)
        end_coords_count_list = []
        path_count_list = []
        for sx, sy in start_coords:
            end_coords_count, path_count = self.custom_bfs(input_data, (sx, sy), 9)
            end_coords_count_list.append(end_coords_count)
            path_count_list.append(path_count)
        return sum(end_coords_count_list), sum(path_count_list)

    #@timer
    def puzzle1(self, input_data):
        res, _ = self.solver(input_data)
        return res

    #@timer
    def puzzle2(self, input_data):
        _, res = self.solver(input_data)
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