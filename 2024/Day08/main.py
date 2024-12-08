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
    inp = [list(x) for x in inp]  # any to int
    return inp

class Solution:
    def is_valid_coord(self, coord, dims):
        return 0 <= coord[0] < dims[0] and 0 <= coord[1] < dims[1]

    def get_antenna_coords(self, grid):
        all_antennas = set()
        antenna_dict = defaultdict(list)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                symb = grid[i][j]
                if symb != '.':
                    all_antennas.add((i, j))
                    antenna_dict[symb].append((i, j))
        return all_antennas, antenna_dict

    def get_antinodes(self, dims, antenna_dict: defaultdict, harmonics=False):
        all_antinodes = set()
        antinode_dict = defaultdict(list)
        for ant in antenna_dict.keys():
            ant_coords = antenna_dict[ant]
            for i in range(len(ant_coords)):
                for j in range(i + 1, len(ant_coords)):
                    trans = (ant_coords[j][0] - ant_coords[i][0], ant_coords[j][1] - ant_coords[i][1])
                    i_antinodes = [(ant_coords[i][0] - trans[0], ant_coords[i][1] - trans[1])]
                    if not self.is_valid_coord(i_antinodes[-1], dims):
                        i_antinodes.pop()
                    j_antinodes = [(ant_coords[j][0] + trans[0], ant_coords[j][1] + trans[1])]
                    if not self.is_valid_coord(j_antinodes[-1], dims):
                        j_antinodes.pop()
                    if harmonics:
                        i_antinodes.append((ant_coords[i][0], ant_coords[i][1]))
                        next_i_antinode = (-1, -1) if not i_antinodes else i_antinodes[-1]
                        while self.is_valid_coord(next_i_antinode, dims):
                            i_antinodes.append(next_i_antinode)
                            next_i_antinode = (next_i_antinode[0] - trans[0], next_i_antinode[1] - trans[1])
                        j_antinodes.append((ant_coords[j][0], ant_coords[j][1]))
                        next_j_antinode = (-1, -1) if not j_antinodes else j_antinodes[-1]
                        while self.is_valid_coord(next_j_antinode, dims):
                            j_antinodes.append(next_j_antinode)
                            next_j_antinode = (next_j_antinode[0] + trans[0], next_j_antinode[1] + trans[1])
                    current_antinodes = [*i_antinodes, *j_antinodes]
                    all_antinodes.update(current_antinodes)
                    antinode_dict[ant].extend(current_antinodes)
        return all_antinodes, antinode_dict

    def insert_antinodes_into_grid(self, grid, antinode_dict):  # debug function for visualization
        dims = len(grid), len(grid[0])
        for k in antinode_dict.keys():
            for c in antinode_dict[k]:
                if self.is_valid_coord(c, dims):
                    if grid[c[0]][c[1]] == '.':
                        grid[c[0]][c[1]] = k + '#'
        return grid

    @timer
    def puzzle1(self, input_data):
        # dicts are for debugging only, wouldve worked with the sets only
        all_antennas, antenna_dict = self.get_antenna_coords(input_data)
        #print(antenna_dict)
        all_antinodes, antinode_dict = self.get_antinodes((len(input_data), len(input_data[0])), antenna_dict)
        #print(antinode_dict)
        #input_data = self.insert_antinodes_into_grid(input_data, antinode_dict)
        #print(input_data)
        return len(all_antinodes)

    @timer
    def puzzle2(self, input_data):
        # dicts are for debugging only, wouldve worked with the sets only
        all_antennas, antenna_dict = self.get_antenna_coords(input_data)
        #print(antenna_dict)
        all_antinodes, antinode_dict = self.get_antinodes((len(input_data), len(input_data[0])), antenna_dict, harmonics=True)
        #print(antinode_dict)
        #input_data = self.insert_antinodes_into_grid(input_data, antinode_dict)
        #print(input_data)
        return len(all_antinodes)

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