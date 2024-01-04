'''
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/

NeetCode:
https://youtu.be/s6ATEkipzow

Time: O(n)

#Medium
#Tree #BinarySearchTree #BinaryTree #DFS
'''

from typing import Optional
from tree_operations.tree_node import TreeNode
from tree_operations.build_tree import with_bfs as build


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # inner helper function -- check validity for a node
        # lower: current lower limit
        # upper: current upper limit
        def is_valid(node, lower, upper):
            if not node:
                return True
            if not (lower < node.val < upper):
                return False

            # 看下方圖解
            return (is_valid(node.left, lower, node.val) and
                    is_valid(node.right, node.val, upper))

        # root 可以是任何數字，所以它的範圍是負無窮大到正無窮大
        return is_valid(root, float('-inf'), float('inf'))


s = Solution()
root = build([2, 1, 3])
assert s.isValidBST(root) == True

root = build([5, 1, 4, None, None, 3, 6])
assert s.isValidBST(root) == False

# 下面那個誤區
root = build([5, 3, 7, None, None, 4, 8])
assert s.isValidBST(root) == False

print('Pass')

'''
A case that needs to be considered:
#     5
#   /   \
#  3     7
#       / \
#      4   8 (7 < 8 < inf)
# (?? 5 < 4 < 7 <- 發生問題所在)

root:
-inf < 5 < inf

5往左 -> 3:
-inf < (3) < 5    # 往左必須變小 -> 上限是 parent val, 下限必須與 parent 的下限相同, 即 -inf

5往右 -> 7:
5 < (7) < inf     # 往右必須變大 -> 所以下限為 parent val, 上限則與 parent 上限相同, 即 inf

7往左 -> 4:
5 < (4) < 7       # 往左必須變小 -> 故上限是 parent val, 下限則與 parent 下限相同 , 即 5 -> 發現未符合 BST 規則！
                    (7 的左子節點必須也要大於 5, 才能讓 root 右半邊的節點都比 5 大)
7往右：
7 < (8) < inf     # 往右必須變大 -> 故下限為 parent val, 上限則和 parent 上限相同，即 inf

如果只看每個節點本身，是沒有違反左小右大規則的。
但是 4 不應該出現在右半部，因為 root 是 5。這種情況容易被忽略。
所以要用兩邊範圍夾擠的方式來檢查每個節點，然後依照每個節點的所在位置去調整這個應該遵循的範圍。

再看另外一個例子，更多層的樹，看邊界的變化。

#     5
#   /   \
#  1     9
#       / \
#      8  11   
#        /  \
#       10  13 

root:
-inf < [5] < inf
5 往右 -> 9:    5 < [9]  < inf
9 往右 -> 11:   9 < [11] < inf
9 往左 -> 8:    5 <  8   < 9
11 往左-> 10:   9 < [10] < 11
11 往右-> 13:  11 < [13] < inf

結論：
因為是 Binary Search Tree 所以
1. 左子節點要比父節點小, 上限是 parent val, 但是仍要大於父節點的下限, 這樣才會維持BST
2. 右子節點要比父節點大, 下限是 parent val, 但是仍要小於父節點的上限。

'''
