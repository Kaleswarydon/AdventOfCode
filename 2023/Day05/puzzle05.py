import pandas as pd


def input_preparer(input_data):
    res = {}
    actual_header = ''
    for i in input_data:
        line = i.split(':')
        if len(line) > 1: #headers
            actual_header = line[0]
            if line[1] != '\n': #seeds content
                res.update({line[0]: [[int(i) for i in line[1].strip().split()]]}) #content
            else:
                res.update({line[0]: []})
        else: #content
            if line[0] != '\n':
                tmp = res.get(actual_header)
                tmp.append([int(i) for i in line[0].strip().split()])
                res.update({actual_header: tmp})
    return res

def find_paths(prep, seed_ranges):
    lowest_location = None
    paths = []
    seed_range_len = len(seed_ranges)
    for seed_index, seeds in enumerate(seed_ranges):
        #print("range", seed_index, "of", seed_range_len)
        for s in range(seeds[0], seeds[0] + seeds[1]):
            path = [s]
            for k in list(prep.keys())[1:]:
                added = False
                for l in prep.get(k):
                    dst_range = [l[0], l[0] + l[2] - 1]
                    src_range = [l[1], l[1] + l[2] - 1]
                    if src_range[0] <= path[-1] <= src_range[1]:
                        path.append(dst_range[0] + (path[-1] - src_range[0]))
                        added = True
                        break
                if not added:
                    path.append(path[-1])
            if lowest_location is None or path[-1] < lowest_location:
                lowest_location = path[-1]
            #paths.append(path)
    #return paths
    return lowest_location

def in_ranges(ranges, value):
    for r in ranges:
        if r[0] <= value < r[0] + r[1]:
            return True
    return False

def find_paths_reversed(prep, location_ranges):
    seeds = [[prep.get('seeds')[0][x], prep.get('seeds')[0][x + 1]] for x in range(0, len(prep.get('seeds')[0]), 2)]
    #print(seeds)
    paths = []
    location_range_len = len(location_ranges)
    for location_index, locations in enumerate(location_ranges):
        range_end = locations[0] + locations[-1]
        for l in range(locations[0], range_end):
            path = [l]
            for k in list(prep.keys())[:0:-1]:
                added = False
                for s in prep.get(k):
                    dst_range = [s[1], s[1] + s[2] - 1]
                    src_range = [s[0], s[0] + s[2] - 1]
                    if src_range[0] <= path[-1] <= src_range[1]:
                        path.append(dst_range[0] + (path[-1] - src_range[0]))
                        added = True
                        break
                if not added:
                    path.append(path[-1])
            if in_ranges(seeds, path[-1]):
                #print(path)
                #print("loc", path[0])
                #print("seed", path[-1])
                print()
                print("Found solution: loc", path[0], "seed", path[-1])
                return [path[0], path[-1]]
            #paths.append(path)
            if not l % 100000:
                print(f"\rProcessed {l} of {range_end} ({l / range_end} %)", end="")
        print()
    #end = sorted([[x[0], x[-1]] for x in paths if in_ranges(seeds, x[-1])], key=lambda x: x[0])[0]
    #print(end)
    return paths

if __name__ == '__main__':
    with open('input1.txt', 'r') as f:
        input_data = f.readlines()
    #print(input_data)
    prep = input_preparer(input_data)

    #puzzle1
    seed_ranges1 = [[x, 1] for x in prep.get('seeds')[0]]
    path_list1 = find_paths(prep, seed_ranges1)
    min_location1 = path_list1
    print('puzzle1:', min_location1)

    #puzzle2:
    #seed_ranges2 = [[prep.get('seeds')[0][x], prep.get('seeds')[0][x + 1]] for x in range(0, len(prep.get('seeds')[0]), 2)]
    #print(seed_ranges2)
    #path_list2 = find_paths(prep, seed_ranges2)
    #min_location2 = path_list2
    #print('puzzle2:', min_location2)

    #puzzle2_reversed
    #location_ranges2 = [[x[1], x[2]] for x in list(reversed(prep.get('humidity-to-location map')))]
    location_ranges2 = [[0, 1094349260]]
    #location_ranges2 = [[0, 56]]
    #print(location_ranges2)
    path_list2 = find_paths_reversed(prep, location_ranges2)
    print('puzzle2:', path_list2)