# 104. Maximum Depth of Binary Tree: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# neetcode: https://youtu.be/hTM3phVI6YQ

# Time: O(n)

# Pre-order DFS:
# process the current node first and then go to the left sub-tree and right sub-tree

# Stack

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def maxDepth(self, root):
        stack = [[root, 1]]   # stack 每一個元素都存有 node 跟 depth
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return res
