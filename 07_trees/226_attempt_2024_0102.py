from tree_operations import build_tree, traverse_tree
from tree_operations.tree_node import TreeNode


class Solution:
    def invert_tree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        # DFS solution
        # Swap the children
        root.left, root.right = root.right, root.left
        # Recursively invert the subtrees
        self.invert_tree(root.left)
        self.invert_tree(root.right)

        return root


# BFS 建立二元樹
values = [4, 2, 7, 1, 3, 6, 9]
root = build_tree.with_bfs(values)

# 反轉
root = Solution().invert_tree(root)

# 驗證結果
traverse_tree.with_bfs(root)  # 4 7 2 9 6 3 1

'''
before:
       4
     /   \
    2     7
   / \   / \
  1   3 6   9

after:
       4
     /   \
    7     2
   / \   / \
  9   6 3   1
'''
