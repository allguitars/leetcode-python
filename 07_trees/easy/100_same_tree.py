# 100. Same Tree
# neetcode: https://youtu.be/vRbbcKXCxOw

# Time: O(p+q)

# Recursive / DFS
# 1. Check the roots to see if they are the same
# 2. Check both left sub-trees
# 3. Check both right sub-trees

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        # base cases:

        # 1. both are empty trees
        if not p and not q:
            return True

        # when passing this point, Not both of them are null
        # they can be both non-empty, or just one of them is empty

        # 2. Only one of them is empty
        if not p or not q:
            return False

        # when passing this point, both of them are non-empty

        # 3. Both nodes are not null, check the values
        if p.val != q.val:
            return False

        # when passing this point, both nodes are non-empty and they have the same values

        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
