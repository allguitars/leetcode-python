'''
235. Lowest Common Ancestor of a Binary Search Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
NeetCode: https://youtu.be/gs2LMfuOR9k

Time: O(log n)
Space: O(1)

#Medium
#Tree #BinaryTree #BinarySearchTree #DFS

Similar Questions:
236. Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
'''

from tree_operations.tree_node import TreeNode
from tree_operations.build_tree import with_bfs as build


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root

        # Note that this is a Binary Search Tree
        while True:
            if p.val > current.val and q.val > current.val:  # 兩個數字都比較大
                # Go right
                current = current.right
            elif p.val < current.val and q.val < current.val:  # 兩個數字都比較小
                # Go left
                current = current.left
            else:
                return current


solution = Solution()
root = build([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])

# 2 & 4
assert solution.lowestCommonAncestor(root, TreeNode(2), TreeNode(4)).val == 2
# 2 & 5
assert solution.lowestCommonAncestor(root, TreeNode(2), TreeNode(5)).val == 2
# 7 & 9
assert solution.lowestCommonAncestor(root, TreeNode(7), TreeNode(9)).val == 8
# 0 & 5
assert solution.lowestCommonAncestor(root, TreeNode(0), TreeNode(5)).val == 2
# 3 & 5
assert solution.lowestCommonAncestor(root, TreeNode(3), TreeNode(5)).val == 4

# Test another tree
root = build([2, 1])
assert solution.lowestCommonAncestor(root, TreeNode(2), TreeNode(1)).val == 2

# Test case on LeetCode that failed
root = build([3, 1, 8, None, None, 5, 10, 4, 6, 9, 11])
assert solution.lowestCommonAncestor(root, TreeNode(9), TreeNode(11)).val == 10

print('Pass')

'''
#     3
#   /   \
#  1     8
#       / \
#      5  10
#     / \ / \
#    4  6 9 11
'''


'''
#         6
#       /   \
#      2     8
#     / \   / \
#    0   4 7   9
#       / \
#      3   5

# Case 1: p = 2, q = 4
# 1. 都比6小 -> 要往左走
# 2. 走到2時  發現本身就是2  則不管另外一數字跟這個數字差多遠  2就是LCA

# Case 2: p = 2, q = 5
# 1. 一開始都比6小 -> 往左走到2
# 2. 遇到2  不管5距離多遠  2就是 LCA

# Case 3: p = 7, q = 9
# 1. 第一步先往右走到8
# 2. 一個數字比8小  另一個則比8大  所以這邊開始要分道
#    只要一分道  就表示該節點8  是LCA

# Case 4: p = 0, q = 5
# 1. 都比6小  往左走到2
# 2. 一個比2小  一個比2大  則2就是LCA

# Case 5: p = 3, q = 5
# 1. 都比6小  往左走到2
# 2. 都比2大  往右走到4
# 3. 一個比4小  一個比4大  因為這裡要分道了  4就是LCA
'''
