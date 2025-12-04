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
    # inp = [[int(y) for y in x] for x in inp]  # any to int
    return inp

class Solution:
    def is_coord_valid(self, coord, dims):
        return 0 <= coord[0] < dims[0] and 0 <= coord[1] < dims[1]

    def custom_bfs(self, grid, start_coord):
        visited = {start_coord}
        fences = defaultdict(list)
        dims = (len(grid), len(grid[0]))
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        q = deque([start_coord])
        group_symb = grid[start_coord[0]][start_coord[1]]
        while q:
            curr = q.popleft()
            for d in directions:
                potential_next = (curr[0] + d[0], curr[1] + d[1])
                if self.is_coord_valid(potential_next, dims) and grid[potential_next[0]][potential_next[1]] == group_symb:
                    if potential_next not in visited:
                        q.append(potential_next)
                        visited.add(potential_next)
                else:
                    fences[d].append(potential_next)
        return visited, fences

    def get_groups(self, input_data):
        dims = (len(input_data), len(input_data[0]))
        all_coords = {(i, j) for j in range(dims[1]) for i in range(dims[0])}
        groups = defaultdict(list)
        while all_coords:
            group_start = all_coords.pop()
            group, fences = self.custom_bfs(input_data, group_start)
            groups[input_data[group_start[0]][group_start[1]]].append((group, fences))
            all_coords.difference_update(group)
        return groups

    def get_region_sides(self, fences_dict):
        #print(fences_dict)
        sides = 0
        for d in fences_dict.keys():
            tmp = defaultdict(list)
            if not d[0]:
                for x, y in fences_dict[d]:
                    heapq.heappush(tmp[y], x)
            else:
                for x, y in fences_dict[d]:
                    heapq.heappush(tmp[x], y)
            #print(d, fences_dict[d], tmp)
            for m in tmp.keys():
                prev = tmp[m][0]
                heapq.heappop(tmp[m])
                sides += 1
                while tmp[m]:
                    curr = heapq.heappop(tmp[m])
                    if not curr == prev + 1:
                        sides += 1
                    prev = curr
        return sides

    #@timer
    def puzzle1(self, input_data):
        groups = self.get_groups(input_data)
        res = 0
        for k in groups.keys():
            for g, f in groups[k]:
                res += len(g) * sum([len(v) for v in f.values()])
        return res

    #@timer
    def puzzle2(self, input_data):
        groups = self.get_groups(input_data)
        res = 0
        for k in groups.keys():
            for g, f in groups[k]:
                sides = self.get_region_sides(f)
                res += len(g) * sides
                #print(k, len(g), sides)
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