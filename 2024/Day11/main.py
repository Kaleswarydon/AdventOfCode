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
    inp = [int(x) for x in inp[0].split()]  # any to int
    return inp

class Solution:
    def solver_bruteforce(self, input_data, blink_amount):  # takes too long for 30+ blinks
        res = deque(input_data)
        for _ in range(blink_amount):
            tmp = deque()
            while res:
                s = res.popleft()
                ss = str(s)
                if not s:
                    tmp.append(1)
                elif not len(ss) % 2:
                    tmp.append(int(ss[:len(ss) // 2]))
                    tmp.append(int(ss[len(ss) // 2:]))
                else:
                    tmp.append(s * 2024)
            res = tmp
        return len(res)

    def solver(self, input_data, blink_amount): # fails somewhere between 20k-30k blinks because of integer string conversion limit of 4300 digits
        res = 0
        for stone in input_data:
            stone_dict = defaultdict(int)
            stone_dict[stone] = 1
            for blink in range(blink_amount):
                tmp_dict = defaultdict(int)  # creating a separate dict for every step (blink) is still inefficient but good enough
                for k in stone_dict.keys():
                    s = str(k)
                    if not k:
                        tmp_dict[1] += stone_dict[k]
                    elif not len(s) % 2:
                        tmp_dict[int(s[:len(s)//2])] += stone_dict[k]
                        tmp_dict[int(s[len(s)//2:])] += stone_dict[k]
                    else:
                        tmp_dict[k * 2024] += stone_dict[k]
                stone_dict = tmp_dict
            res += sum(stone_dict.values())
        return res

    @timer
    def puzzle1(self, input_data):
        return self.solver_bruteforce(input_data, 25)

    @timer
    def puzzle2(self, input_data):
        return self.solver(input_data, 75)



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