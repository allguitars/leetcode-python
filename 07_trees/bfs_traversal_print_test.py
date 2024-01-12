from collections import deque
from tree_operations.tree_node import TreeNode
from tree_operations.build_tree import with_bfs as build
from tree_operations.traverse_tree import with_bfs as traverse


#     1
#   /   \
#  2     3
#       / \
#      4   5

# result:
# 1 2 3 None None 4 5


root = build([1, 2, 3, None, None, 4, 5])
result = traverse(root)
print(result)  # [1, 2, 3, None, None, 4, 5]
# 這個結果符合預期，但是下一個 case 就不對了

#     1
#   /   \
#  2     3
#   \   / \
#   6  4   5
#     / \
#    7   8

# result:
# 1 2 3 None 6 4 5 None None 7 8

# Todo: fix this case
root = build([1, 2, 3, None, 6, 4, 5, None, None, None, None, 7, 8])
result = traverse(root)
print(result)
# [1, 2, 3, None, 6, 4, 5, None, None, None, None, None, None, 7, 8] <- 有出入
