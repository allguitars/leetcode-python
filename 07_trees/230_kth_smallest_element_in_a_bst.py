'''
230. Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst

NeetCode: https://youtu.be/5LUXSvjmGCw

#Medium
#Tree #BinaryTree #BinarySearchTree #DFS

對於一個 BST 如果做 in-order traversal 可以得到排序過的數字
但是這裡我們不用遞迴的方式做 traversal  而是用 iterative 的方式
不用遞迴就必須要利用一個 stack, 才能記錄父節點, 當子節點處理完畢, 才可以退回到父節點

in-order traversal 就是 DFS
1. 一路往左走到底, 沿路經過的節點都 push 到 stack 中 
2. 到底(遇到 null)之後才 pop stack -> 數目 + 1 (或是印出來)
3. pop 之後, 因為是 in-order, 接著跳到它的右子節點
4. 然後也是要一路往左走到底!! 回到 STEP 1
'''

from typing import Optional
from tree_operations.tree_node import TreeNode
from tree_operations.build_tree import with_bfs as build


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        stack = []
        cur = root

        while cur or stack:
            # go strait to the bottom left for each sub-tree
            while cur:
                stack.append(cur)
                cur = cur.left

            # no left child anymore
            cur = stack.pop()
            count += 1
            if count == k:
                return cur.val
            cur = cur.right


s = Solution()

root = build([3, 1, 4, None, 2])
assert s.kthSmallest(root, 1) == 1

root = build([5, 3, 6, 2, 4, None, None, 1])
assert s.kthSmallest(root, 3) == 3


print('Pass')
