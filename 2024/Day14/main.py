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
import matplotlib.pyplot as plt

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
    inp = [[[int(z) for z in y.split('=')[1].split(',')[::-1]] for y in x.split()] for x in inp]  # exchange x and y coords bc problem says so :(
    return inp

class Solution:
    def step_forward(self, start, step, grid_dims):
        dest = [(start[0] + step[0]) % grid_dims[0], (start[1] + step[1]) % grid_dims[1]]
        #print(start, step, dest)
        return dest

    def detect_loop(self, robot: list[list[int]], grid_dims: tuple):
        start = robot[0]
        curr = robot[0]
        step = robot[1]
        res = [start]
        cntr = 0
        #print(start, step)
        while True:
            curr = self.step_forward(curr, step, grid_dims)
            cntr += 1
            #print(curr)
            if curr == start:
                break
            res.append(curr)
        return res

    def get_safety_factor(self, grid):
        mid_row = (len(grid) // 2).__ceil__()
        mid_col = (len(grid[0]) // 2).__ceil__()
        #print(mid_row, mid_col)
        grid = np.array(grid)
        quadrants = [grid[:mid_row,:mid_col],
                     grid[:mid_row,mid_col+1:],
                     grid[mid_row+1:,:mid_col],
                     grid[mid_row+1:,mid_col+1:]]
        res = 1
        for q in quadrants:
            res *= np.sum(q)
        return res

    def solver(self, robots, grid_dims, steps):
        robot_positions = []
        positions_after_steps = []
        grid = [[0 for _ in range(grid_dims[1])] for _ in range(grid_dims[0])]
        #print(grid)
        for r in robots:
            all_pos = self.detect_loop(r, grid_dims)
            robot_positions.append(all_pos)
            end_pos = all_pos[steps % len(all_pos)]
            positions_after_steps.append(end_pos)
            grid[end_pos[0]][end_pos[1]] += 1
        return grid

    def puzzle0(self, input_data):  # for example data / dims
        #print(input_data)
        grid_dims = (7, 11)
        steps = 100
        grid = self.solver(input_data, grid_dims, steps)
        safety_factor = self.get_safety_factor(grid)
        return safety_factor

    @timer
    def puzzle1(self, input_data):
        #print(input_data)
        grid_dims = (103, 101)
        steps = 100
        grid = self.solver(input_data, grid_dims, steps)
        safety_factor = self.get_safety_factor(grid)
        return safety_factor

    @timer
    def puzzle2(self, input_data):
        #print(input_data)
        grid_dims = (103, 101)
        #grid_dims = (7, 11)  # for example data
        positions = []
        for r in input_data:
            positions.append(self.detect_loop(r, grid_dims))
        print(len(positions[0]))
        for j in range(len(positions[0])):
            grid = [[0 for _ in range(grid_dims[1])] for _ in range(grid_dims[0])]
            for i in range(len(positions)):
                x, y = positions[i][j]
                grid[x][y] = 1
            plt.imsave("imgs/" + str(j) + ".png", grid)


if __name__ == '__main__':
    sol = Solution()

    input_puzzle_0_0_example = read_input("input_small.txt", 'l', " ")  # small test input
    input_puzzle_1_0_example = read_input("input_puzzle_1_0_example.txt", 'l', " ")  # small test input
    input_puzzle_1_1 = read_input("input_puzzle_1_1.txt", 'l', " ")  # real puzzle input
    #print(sol.puzzle0(input_puzzle_1_0_example))
    #print(sol.puzzle1(input_puzzle_1_0_example))
    #print(sol.puzzle1(input_puzzle_1_1))

    input_puzzle_2_0_example = read_input("input_puzzle_2_0_example.txt", 'l', " ")
    input_puzzle_2_1 = read_input("input_puzzle_2_1.txt", 'l', " ")
    #print(sol.puzzle2(input_puzzle_2_0_example))
    print(sol.puzzle2(input_puzzle_2_1))