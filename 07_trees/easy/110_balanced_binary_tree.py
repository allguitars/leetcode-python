# 110. Balanced Binary Tree
# neetcode: https://youtu.be/QfJsau0ItOY

# Time: O(n^2) for recursive DFS
# 若是由下往上檢查，則為 O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(root):
            if not root:
                return [True, 0]     # isBalanced?, height

            left_result, right_result = dfs(root.left), dfs(root.right)

            # both left and right subtrees are both balanced and the difference between their
            # heights <= 1, meaning from the root subtree is also balanced
            balanced = (left_result[0] and right_result[0] and
                        abs(left_result[1] - right_result[1]) <= 1)

            return [balanced, 1 + max(left_result[1], right_result[1])]

        return dfs(root)[0]
