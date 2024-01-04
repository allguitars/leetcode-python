'''
102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/

NeetCode: https://youtu.be/6ZnyEApgFYg

Time: O(n)
Space: O(n/2) -> O(n)
complete binary tree 的最下面一排會有 ceiling[n/2] 個節點
在最後一層時  這一整排都要放進 queue 所以 worst case 需要這麼多的 space 給 queue

#Medium
#Tree #BinaryTree #BFS
'''

from typing import Optional, List
from collections import deque
from tree_operations.tree_node import TreeNode
from tree_operations.build_tree import with_bfs as build


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root])

        while q:
            level_vals = []

            # go through the whole level at a time
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level_vals.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level_vals:
                res.append(level_vals)

        return res


s = Solution()

root = build([3, 9, 20, None, None, 15, 7])
assert s.levelOrder(root) == [[3], [9, 20], [15, 7]]

root = build([3, 9, 20, 1, 6, 15, 7])
assert s.levelOrder(root) == [[3], [9, 20], [1, 6, 15, 7]]

root = build([])
assert s.levelOrder(root) == []

print('Pass')

'''
#     3
#   /   \
#  9     20
# / \   / \
#      15  7 
'''
