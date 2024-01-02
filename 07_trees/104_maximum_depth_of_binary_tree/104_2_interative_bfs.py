'''
104. Maximum Depth of Binary Tree: https://leetcode.com/problems/maximum-depth-of-binary-tree/
neetcode: https://youtu.be/hTM3phVI6YQ
Amazon

Time: O(n)Time: O(n) <- traverse all the nodes

BFS is level-order traversal

#Easy
#Tree
#BinaryTree
#BFS
#Queue
'''

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        level = 0
        q = deque([root])

        while q:
            for i in range(len(q)):  # 這個方法可以確保目前有幾個元素在 queue 裡面就 pop 幾次
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return level
