'''
124. Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/

NeetCode: https://youtu.be/Hr5cWUld4vU

#Hard
#DP #Tree #BinaryTree #DFS

#     1
#   /   \
#  2     3
#       / \
#      4   5 
#     / \
#    6   7

** 規則一：
如果某一層已經有分叉過一次，則下一層的路徑不可以再分叉，遵循 "A node can only appear in the sequence at most once."
例如
(1) 節點分叉到 (2), (3)
(3) 不可以再分叉到 (4) 跟 (5), 否則等於 (3) 在序列上出現兩次。 -> 只能選左右其中一個子節點當作路徑上的下一節點
如果選了 (4) 作為下一節點, (4) 本身也不能再分叉
假設最後選擇了 (6), 那整條 path -> 2,1,3,4,6 -> 總和 16

** 規則二：
如果已經從某一節點做分叉，則不能選擇其父節點，否則也違反了 "A node can only appear in the sequence at most once."
例如
從 (4) 開始分叉, 就不能考慮 (3), 否則等於 4 被重複尋訪
既然 (4) 上層的節點都不能用, 最後的 path -> 6,4,7 -> 總和 17

初始想法：
針對每個節點，計算左右兩子樹的最大總和並加總，此時本身已經分叉，所以子樹路徑不能有分叉。
結果為左子樹"不分叉"最大總和 + 自己 + 右子樹"不分叉"最大總和

進一步思考：
1. 先解出下層（子問題）的結果
    因為這結果可在往上包含父節點時被重複利用，所以不需要從根節點開始解。
2. 有時不一定要包含子樹
    在比較左右子樹的不分叉最大總和時，如果有出現負值的總和，則捨棄不採用，即從這裡開始沒必要往下走，因為會越加越負。
    程式碼可利用 `max(左邊不分叉最大總和, 右邊不分叉最大總和, 0)` , 即加入第三個數字 0 來達到排除負數的目的。

標記：
左子樹最大不分叉總和  可以標記在左子節點上
右子樹最大不分叉總和  可以標記在右子節點上

Time: O(n)
'''

from tree_operations.tree_node import TreeNode
from tree_operations.build_tree import with_bfs as build


class Solution:
    def maxPathSum(self, root: TreeNode | None = None) -> int:
        res = [root.val]
        # 用 list 是為方便使成為 global 變數
        # 如果 res 只宣告成一個 int 變數  則 dfs() 裡面無法存取到它

        # return max path sum WITHOUT split
        def dfs(root: TreeNode | None):
            if not root:
                return 0

            left_max = dfs(root.left)  # 左子樹不分叉路徑最大總和
            left_max = max(left_max, 0)  # 負值則捨棄  改取 0
            right_max = dfs(root.right)  # 右子樹不分叉路徑最大總和
            right_max = max(right_max, 0)  # 負值則捨棄  改取 0

            # compute max path sum WITH split
            # 因為已經有兩邊各自的不分叉路徑最大總和，若加上本身，即成為
            # 由自己開始分叉的路徑最大總和
            # 此時是把自己當作最高層，不去考慮父節點以上的數值。
            # 因此 res[0] 記錄的是由下逐步往上時，各節點當成分叉點時的最大總和
            res[0] = max(res[0], root.val + left_max + right_max)

            # dfs 回傳的是包含本身的不分叉路徑最大總和
            return root.val + max(left_max, right_max)

        dfs(root)
        return res[0]


s = Solution()

#     1
#    / \
#   2   3
root = build([1, 2, 3])
assert s.maxPathSum(root) == 6
# path: 2-1-3

#     -10
#    /   \
#   9    20
#       /  \
#      15   7
root = build([-10, 9, 20, None, None, 15, 7])
assert s.maxPathSum(root) == 42
# path: 15-20-7

print('Pass')
