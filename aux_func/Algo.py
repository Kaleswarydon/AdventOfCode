from collections import defaultdict, deque

####################################### HELPERS #######################################

def make_edge_list(src_list, dest_list, weight_list):
    assert len(src_list) == len(dest_list) == len(weight_list)
    return [[src_list[i], dest_list[i], weight_list[i]] for i in range(len(src_list))]


def make_edge(a, b, directed: bool=False):
    return (a, b) if directed else frozenset({a, b})


def gravity(m, grav_center):
    """
    apply "gravity" to a matrix, slide stones towards center of grav
    '.': free spot
    '#': stones
    '*': stationary obstacle that doesnt move
    :param m: List[List[chr]]
    :param grav_center: string
    :return: List[List[chr]]
    """
    for j in range(len(m[0])):
        free_tiles = 0
        for i in range(len(m) - 1, -1, -1):
            match m[i][j]:
                case '.':
                    free_tiles += 1
                case '*':
                    free_tiles = 0
                case '#':
                    m[i][j] = '.'
                    m[i + free_tiles][j] = '#'
                case _:
                    pass
    return m


def rotate_clockwise(m):  # rotate matrix 90deg (clockwise)
    return [[m[j][i] for j in range(len(m) - 1, -1, -1)] for i in range(len(m[0]))]


def is_coord_valid(coord: list | tuple, dims: list | tuple):
    return 0 <= coord[0] < dims[0] and 0 <= coord[1] < dims[1]


def surrounding_coords(coord: list | tuple):
    return [
        # upper row from left to right
        (coord[0] - 1, coord[1] - 1),
        (coord[0] - 1, coord[1] + 0),
        (coord[0] - 1, coord[1] + 1),

        # adjacents left/right
        (coord[0] + 0, coord[1] - 1),
        (coord[0] + 0, coord[1] + 1),

        # lower row from left to right
        (coord[0] + 1, coord[1] - 1),
        (coord[0] + 1, coord[1] + 0),
        (coord[0] + 1, coord[1] + 1)
            ]

##############################################################################

#-----------------------------------------------------------------------------

####################################### ALGOS #######################################

def floyd_warshall(edges, directed=False):
    dist = defaultdict(lambda: float("inf"))
    vertices = set()
    for src, dest, weight in edges:
        dist[make_edge(src, dest, directed)] = min(weight, dist[make_edge(src, dest, directed)])
        dist[make_edge(src, src, directed)] = 0
        dist[make_edge(dest, dest, directed)] = 0
        vertices.update({src, dest})
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[make_edge(i, j, directed)] > dist[make_edge(i, k, directed)] + dist[make_edge(k, j, directed)]:
                    dist[make_edge(i, j, directed)] = dist[make_edge(i, k, directed)] + dist[make_edge(k, j, directed)]
    return dist


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.cluster_count = n
        self.cluster_size = [1] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            return self.find(self.parent[x])
        return x

    def union(self, x, y):
        c1 = self.find(x)
        c2 = self.find(y)
        if c1 == c2:
            return 0
        if self.cluster_size[c1] > self.cluster_size[c2]:
            self.cluster_size[c1] += self.cluster_size[c2]
            self.parent[c2] = c1
        else:
            self.cluster_size[c2] += self.cluster_size[c1]
            self.parent[c1] = c2
        self.cluster_count -= 1
        return 1


def binary_search(l, r, arr, target):
    while l <= r:
        m = (l + r) // 2
        if arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    return r

##############################################################################


if __name__ == '__main__':
    #print(binary_search([10], 5))  # -1
    print(surrounding_coords((1,1)))
    pass