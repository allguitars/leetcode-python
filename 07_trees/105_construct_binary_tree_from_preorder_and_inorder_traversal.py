'''
105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

NeetCode: https://youtu.be/ihj4IQGZ2zc

#Medium
#Array #HashTable #DivideAndConquer #Tree #BinaryTree

Facts that we can use:
# 1) preorder traversal: [3, 9, 20, 15, 7]
#    第一個數字永遠會代表 root, 接下來會走到左子樹
#    但其實我們無法確認接下來的數字 9 是在左子樹還是右子樹, 畢竟左子樹可以是空的
#    至少我們可以先移除已經確定的 3, 接著搭配 inorder traversal 來處理剩下的數字
# 2) 從 inorder traversal 中: [9, 3, 15, 20 ,7]
#    找到 root value (在第一點已經決定了 root value), 出現在這個數字左邊的數字就會屬於左子樹!
#    第一點剩下的數字有 [9, 20, 15, 7], 根據 inorder 將其 preorder 剩下的數字 partition -> [9] and [15, 20 ,7]

preorder 分開的左半部 [9] 只有一個數字 -> done -> also remove from inorder rest
preorder 的右半部 [15, 20 ,7] -> 根據第一點規則, 第一個數字一定是該樹的 root -> 15 為 root -> remove it from list
拿這個 15 到 inorder 中剩下的數字 [20, 15, 7] 去找分割點 -> 分為 [20] and [7]
preorder 左半 [20] 只有一個數字 -> done
preorder 右半 [7] 也只有一個數字 -> done
'''
# [3, 9, 20, 15, 7]
#  0  1  2   3   4

# root: 3
# left: [3] <- preorder[1: mid+1]
# right: [20, 15, 7] <- preorder[mid+1:]

# [9, 3, 15, 20 ,7]
#  0  1  2   3   4

# left: [9] -> inorder[:mid]
# right [15, 20, 7] -> inorder[mid+1:]

# index of 3 -> mid: 1


from typing import Optional, List
from tree_operations.tree_node import TreeNode
from tree_operations.traverse_tree import inorder_traversal_list, preorder_traversal_list


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
built_tree = Solution().buildTree(preorder, inorder)

assert preorder_traversal_list(built_tree) == [3, 9, 20, 15, 7]
assert inorder_traversal_list(built_tree) == [9, 3, 15, 20, 7]

preorder = [-1]
inorder = [-1]
built_tree = Solution().buildTree(preorder, inorder)

assert preorder_traversal_list(built_tree) == [-1]
assert inorder_traversal_list(built_tree) == [-1]

print('Pass')
