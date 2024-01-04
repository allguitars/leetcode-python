'''
572. Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/

NeetCode: https://youtu.be/vRbbcKXCxOw

#Easy
#Tree
#BinaryTree
#DFS
#HashTable

Similar Questions:
508. Most Frequent Subtree Sum (Medium)
https://leetcode.com/problems/most-frequent-subtree-sum/
'''

from typing import Optional
from tree_operations.build_tree import with_bfs as build
from tree_operations.tree_node import TreeNode


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # subRoot 是空的，則無論 root 是否為空，subtree 都成立
        if not subRoot:
            return True
        # root 是空，但 subRoot 不是空，不可為 subtree
        if not root:
            return False

        # 此時兩邊都不是空

        # 運氣好，從本身開始比較就是 same tree
        if self.isSameTree(root, subRoot):
            return True

        # 比較左右子樹
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return (self.isSameTree(p.left, q.left) and
                    self.isSameTree(p.right, q.right))

        # One is empty, but the other is not
        return False


solution = Solution()

# Case 1
root = build([3, 4, 5, 1, 2])
subRoot = build([4, 1, 2])

assert solution.isSubtree(root, subRoot) == True

# Case 2
root = build([3, 4, 5, 1, 2, None, None, None, None, 0])
subRoot = build([4, 1, 2])

assert solution.isSubtree(root, subRoot) == False

# Case 3
root = build([3, 4, 5, 1, 2, None, None, None, None, 0])
subRoot = build([4, 1, 2, None, None, 0])

assert solution.isSubtree(root, subRoot) == True

print('Pass')
