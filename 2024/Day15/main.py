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
    tmp = []
    res = []
    for x in inp:
        if not x:
            res.append(list(tmp))
            tmp = []
            continue
        tmp.append(list(x))
    steps = []
    for t in tmp:
        steps.extend(t)
    res.append(''.join(steps))
    return res

def prepare_input2(inp):  # individual input preparation
    res = []
    for i in range(len(inp)):
        row = []
        for j in range(len(inp[0])):
            if inp[i][j] == '@':
                row.extend(['@', '.'])
            elif inp[i][j] == 'O':
                row.extend(['[', ']'])
            else:
                row.extend([inp[i][j]] * 2)

        res.append(row)
    return res

class Solution:
    def group_steps(self, steps):
        curr = steps[0]
        cntr = 0
        res = []
        for s in steps:
            if s == curr:
                cntr += 1
            else:
               res.append(curr + ',' + str(cntr))
               curr = s
               cntr = 1
        if cntr:
            res.append(curr + ',' + str(cntr))
        return res


    def find_start_pos(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '@':
                    return i,j

    def is_valid_coord(self, coord, dims):
        return 0 <= coord[0] < dims[0] and 0 <= coord[1] < dims[1]

    def get_matrix_slice(self, start_coord, step_symb, max_grid_dim):
        """
        returns a 1d slice range of a 2d grid, from start to end of grid
        """
        def order(x, y):
            if y < x:
                x, y = y + 1 if y > -1 else 0, x + 1 if x > -1 else 0
            if x == y:
                y += 1
            return x, y
        step_dict = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
        a, b = start_coord[0], start_coord[0] + (step_dict.get(step_symb)[0] * max_grid_dim) + step_dict.get(step_symb)[0]
        c, d = start_coord[1], start_coord[1] + (step_dict.get(step_symb)[1] * max_grid_dim) + step_dict.get(step_symb)[1]
        return [order(a, b), order(c, d)]

    def p1_solver(self, inp):
        """
        let robot walk and shove crates around in warehouse
        """
        step_dict = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
        grid, steps = inp
        grid = np.array(grid)
        # print(grid)
        start = self.find_start_pos(grid)
        curr_pos = start
        for step in steps:
            s0 = step_dict.get(step)[0]
            s1 = step_dict.get(step)[1]
            stack = [curr_pos]
            # print(stack[-1])
            while (grid[stack[-1][0] + s0][stack[-1][1] + s1] != '.' and
                   grid[stack[-1][0] + s0][stack[-1][1] + s1] != '#'):
                # print(stack[-1], grid[stack[-1][0]][stack[-1][1]])
                stack.append((stack[-1][0] + s0, stack[-1][1] + s1))
            x, y = curr_pos
            # print(grid[curr_pos[0]][curr_pos[1]])
            if grid[stack[-1][0] + s0][stack[-1][1] + s1] != '#':
                while stack:
                    x, y = stack.pop()
                    grid[x][y], grid[x + s0][y + s1] = grid[x + s0][y + s1], grid[x][y]
                curr_pos = (x + s0, y + s1)
        return grid

    def solver(self, inp):
        """
        let robot walk and shove crates around in warehouse
        """
        step_dict = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
        grid, steps = inp
        grid = np.array(grid)
        # print(grid)
        start = self.find_start_pos(grid)
        curr_pos = start
        for step_ind, step in enumerate(steps):
            s0 = step_dict.get(step)[0]
            s1 = step_dict.get(step)[1]
            stack = [[curr_pos]]
            #print(stack[-1])
            step_allowed = True
            while not all([grid[z[0] + s0][z[1] + s1] == '.' for z in stack[-1]]):
                next_layer = set()
                for o in stack[-1]:
                    if step in ['^', 'v']:
                        if grid[o[0] + s0][o[1] + s1] == '[':
                            next_layer.add((o[0] + s0, o[1] + s1 + 1))
                        if grid[o[0] + s0][o[1] + s1] == ']':
                            next_layer.add((o[0] + s0, o[1] + s1 - 1))
                    if grid[o[0] + s0][o[1] + s1] != '.':
                        next_layer.add((o[0] + s0, o[1] + s1))
                stack.append(next_layer)
                #print(step_ind, step, stack)
                if any([grid[z[0]][z[1]] == '#' for z in next_layer]):
                    step_allowed = False
                    break
            #print(step, stack, [''.join(x) for x in grid])
            if step_allowed:
                #print("allowed")
                for l in stack[::-1]:
                    for c in l:
                        x, y = c
                        grid[x][y], grid[x + s0][y + s1] = grid[x + s0][y + s1], grid[x][y]
                curr_pos = (curr_pos[0] + s0, curr_pos[1] + s1)
            #print(step, [''.join(x) for x in grid])
        return grid


    @timer
    def puzzle1(self, inp):
        final_grid = self.solver(inp)
        res = 0
        for i in range(len(final_grid)):
            for j in range(len(final_grid[0])):
                if final_grid[i][j] == 'O':
                    res += (i * 100) + j
        return res

    @timer
    def puzzle2(self, inp):
        grid, steps = inp
        grid = np.array(prepare_input2(grid))
        final_grid = self.solver((grid, steps))
        res = 0
        for i in range(len(final_grid)):
            for j in range(len(final_grid[0])):
                if final_grid[i][j] == '[':
                    res += (i * 100) + j
        return res

if __name__ == '__main__':
    sol = Solution()

    input_puzzle_1_0_example = read_input("input_puzzle_1_0_example.txt", 'l', " ")  # small test input
    input_puzzle_1_0_example_1 = read_input("input_puzzle_1_0_example_1.txt", 'l', " ")  # small test input
    input_puzzle_1_1 = read_input("input_puzzle_1_1.txt", 'l', " ")  # real puzzle input
    print(sol.puzzle1(input_puzzle_1_0_example))
    print(sol.puzzle1(input_puzzle_1_0_example_1))
    print(sol.puzzle1(input_puzzle_1_1))

    input_puzzle_2_0_example = read_input("input_puzzle_2_0_example.txt", 'l', " ")
    input_puzzle_2_0_example_1 = read_input("input_puzzle_2_0_example_1.txt", 'l', " ")
    input_puzzle_2_1 = read_input("input_puzzle_2_1.txt", 'l', " ")
    print(sol.puzzle2(input_puzzle_2_0_example))
    print(sol.puzzle2(input_puzzle_2_0_example_1))
    print(sol.puzzle2(input_puzzle_2_1))