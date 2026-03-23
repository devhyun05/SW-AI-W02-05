# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639


import sys
sys.setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value 
        self.left = left 
        self.right = right 

def insert(root, new_node):
    if not root: 
        return TreeNode(new_node)

    if root.value > new_node: 
        root.left = insert(root.left, new_node)
    else:
        root.right = insert(root.right, new_node)
    
    return root 

def post_order_traversal(root):
    if not root:
        return 

    post_order_traversal(root.left)
    post_order_traversal(root.right)
    print(root.value)

tree_nodes = []

for line in sys.stdin:
    tree_nodes.append(int(line))

root = TreeNode(tree_nodes[0])

for node in tree_nodes[1:]:
    insert(root, node)

post_order_traversal(root)

