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
    ordering_rules = []
    page_updates = []
    for x in inp:
        if not x:
            continue
        elif len(l := x.split('|')) == 2:
            ordering_rules.append(l)
        else:
            page_updates.append(x.split(','))
    o_r = defaultdict(set)
    for bef, aft in ordering_rules:
        o_r[aft].add(bef)
    return o_r, page_updates

class Solution:
    def is_after(self, page1: int, page2: int, rule_set: defaultdict) -> bool:
        # returns true if page2 comes after page1, according to the ordering rules
        return page2 in rule_set[page1]

    def is_update_valid(self, list_of_pages: list, rule_set: defaultdict) -> int:
        for i in range(1, len(list_of_pages)):
            if not self.is_after(list_of_pages[i], list_of_pages[i-1], rule_set):
                return i
        return -1

    def fix_update(self, update, rule_set: defaultdict):
        while not (i := self.is_update_valid(update, rule_set)) == -1:
            tmp = update[i]
            update[i] = update[i-1]
            update[i-1] = tmp
        return update

    def puzzle1(self, input_data):
        ordering_rules, page_updates = input_data
        res = 0
        for i, u in enumerate(page_updates):
            v = self.is_update_valid(u, ordering_rules)
            if v == -1:
                res += int(u[len(u) // 2])
        return res

    def puzzle2(self, input_data):
        ordering_rules, page_updates = input_data
        res = 0
        for i, u in enumerate(page_updates):
            v = self.is_update_valid(u, ordering_rules)
            if not v == -1:
                u = self.fix_update(u, ordering_rules)
                res += int(u[len(u) // 2])
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