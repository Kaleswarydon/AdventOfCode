from collections import deque
from typing import *
from collections import defaultdict
#from icecream import ic as print


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "TreeNode(" + str(self.val) + ")"

    def __repr__(self):
        if self is None:
            return None
        if self.left is None:
            l = "None"
        else:
            l = self.left.val
        if self.right is None:
            r = "None"
        else:
            r = self.right.val
        return "TreeNode(" + str(self.val) + ", " + str(l) + ", " + str(r) + ")"

    def bst_find(self, value: int):  # only works if tree is a bst
        path = []
        def helper(node: TreeNode, v: int):
            if not node or node.val == v:
                return path
            if node.val > v:
                path.append("L")
                return helper(node.left, v)
            else:
                path.append("R")
                return helper(node.right, v)
        return helper(self, value)

def bt_find_path(root: Optional[TreeNode], p: List[int]):  # returns true if path in p is present in binary tree
    path_nodes = deque()
    tmp_q = deque([root])
    while tmp_q:
        item = tmp_q.popleft()
        if item:
            if item.left:
                tmp_q.append(item.left)
            if item.right:
                tmp_q.append(item.right)
            if item.val == p[0]:
                path_nodes.append((item, 1))
    while path_nodes:
        item, ni = path_nodes.popleft()
        if ni == len(p):
            return True
        if item.left and item.left.val == p[ni]:
            path_nodes.append((item.left, ni + 1))
        if item.right and item.right.val == p[ni]:
            path_nodes.append((item.right, ni + 1))
    return False

def bfs_list_to_binary_tree(l: list, root_only=True):
    if not l:
        return None
    current = 0
    current_left_assigned_none = False
    node_list = [TreeNode(val=l[0])]
    for i in range(1, len(l)):
        current_node = node_list[current]
        tmp = None
        while not current_node:
            current += 1
            current_node = node_list[current]
        if current_node:
            if l[i] is not None:
                tmp = TreeNode(val=l[i])
            else:
                tmp = None
            if current_node.left is None and not current_left_assigned_none:
                current_node.left = tmp
                current_left_assigned_none = True
            elif current_node.right is None:
                current_node.right = tmp
                current += 1
                current_left_assigned_none = False
        node_list.append(tmp)
    if root_only:
        return node_list[0]
    return node_list


def binary_tree_to_bfs_list(root: TreeNode, only_values=False):
    res = []
    q = deque([root])
    while q:
        item = q.popleft()
        if item:
            res.append(item.val)
            q.append(item.left)
            q.append(item.right)
        elif not only_values:
            res.append(None)
    while res[-1] is None:
        res.pop()
    return res


def make_balanced_bst_from_inorder_list(node_list): #make balanced bst from inorder list
    def helper(ptr_lo, ptr_hi):
        if ptr_lo > ptr_hi:
            return None
        new_root_index = (ptr_lo + ptr_hi) // 2
        new_root = TreeNode(node_list[new_root_index])
        new_root.left = helper(ptr_lo, new_root_index - 1)
        new_root.right = helper(new_root_index + 1, ptr_hi)
        return new_root
    return helper(0, len(node_list) - 1)

def get_connections(root): # simple bfs
    parents = defaultdict(lambda: ('X', TreeNode(-1)))
    children = defaultdict(lambda: [None, None])
    q = deque([root])
    while q:
        item = q.popleft()
        if item:
            children[item] = [None, None]
            if item.left:
                parents[item.left.val] = ('L', item)
                children[item.val][0] = item.left
            if item.right:
                parents[item.right.val] = ('R', item)
                children[item.val][1] = item.right
            q.append(item.left)
            q.append(item.right)
    return parents, children


######## SEARCH ########
def bfs(root: TreeNode):  # binary version
    return binary_tree_to_bfs_list(root, only_values=True)


def dfs(root, mode='post'):
    res = []

    def preorder(node):
        if node:
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)

    def inorder(node):
        if node:
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

    def postorder(node):
        if node:
            postorder(node.left)
            postorder(node.right)
            res.append(node.val)

    if mode == "pre":
        preorder(root)
    elif mode == "in":
        inorder(root)
    else:  # mode == "post"
        postorder(root)
    return res



##


########################

######## TRAVERSAL ########
def dfs_n_ary_postorder(self, root):
    res = []
    def postorder(node):
        if node:
            for ch in node.children:
                postorder(ch)
            res.append(node.val)
    postorder(root)
    return res

def inorder_traversal(node: TreeNode):
    def helper(node: TreeNode):
        if node is None:
            return
        helper(node.left)
        res.append(node.val)
        helper(node.right)
    res = []
    helper(node)
    return res

###########################



if __name__ == '__main__':
    null = None
    t = bfs_list_to_binary_tree([4,1,6,0,2,5,7,null,null,null,3,null,null,null,8], False)
    print(t)
    a = binary_tree_to_bfs_list(t[0])
    print(a)
    b = bfs(t[0])
    print(b)
    c = inorder_traversal(t[0])
    print(c)