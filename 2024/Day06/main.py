from gc import enable

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
    def wrapper(*args, **kwargs):
        start = time.time()
        res = f(*args, **kwargs)
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
    inp = [list(x) for x in inp]  # any to int
    return inp

class Solution:
    def __init__(self):
        self.directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    def turn_right(self, d):
        to_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
        return to_right.get(d)

    def find_start(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in self.directions.keys():
                    return i, j

    def walk(self, grid, start):
        i, j = start
        dir_symb = grid[i][j]
        path = {(i, j)}
        loop_detect = defaultdict(list)
        #print(dir_symb)
        x, y = self.directions.get(dir_symb)
        while True:
            try:
                while grid[i+x][j+y] != '#':
                    i += x
                    j += y
                    if 0 > i or i >= len(grid) or 0 > j or j >= len(grid[0]):
                        raise IndexError
                    path.add((i, j))
                if dir_symb in loop_detect[(i, j)]:
                    #print("trying to add", dir_symb, (x,y), "to", loop_detect[(i, j)], "at", (i,j))
                    #print(path)
                    return set()
                else:
                    loop_detect[(i, j)].append(dir_symb)
                dir_symb = self.turn_right(dir_symb)
                x, y = self.directions.get(dir_symb)
            except:
                break
        #print(path)
        return path

    #@timer
    def puzzle1(self, input_data):
        #print(input_data)
        start = self.find_start(input_data)
        path = self.walk(input_data, start)
        return len(path)

    #@timer
    def puzzle2(self, input_data):
        #print(input_data)
        start = self.find_start(input_data)
        path = self.walk(input_data, start)
        res = 0
        for i, j in path:
            if (i, j) == start:
                continue
            tmp_symb = input_data[i][j]
            input_data[i][j] = '#'
            tmp_path = self.walk(input_data, start)
            if not tmp_path:
                #print(i,j)
                res += 1
            input_data[i][j] = tmp_symb
        return res

if __name__ == '__main__':
    sol = Solution()

    input_tiny = read_input("input_tiny.txt", 'l', " ")

    input_puzzle_1_0_example = read_input("input_puzzle_1_0_example.txt", 'l', " ")  # small test input
    input_puzzle_1_1 = read_input("input_puzzle_1_1.txt", 'l', " ")  # real puzzle input
    print(sol.puzzle1(input_tiny))
    print(sol.puzzle1(input_puzzle_1_0_example))
    print(sol.puzzle1(input_puzzle_1_1))


    input_puzzle_2_0_example = read_input("input_puzzle_2_0_example.txt", 'l', " ")
    input_puzzle_2_1 = read_input("input_puzzle_2_1.txt", 'l', " ")
    print(sol.puzzle2(input_tiny))
    print(sol.puzzle2(input_puzzle_2_0_example))
    print(sol.puzzle2(input_puzzle_2_1))