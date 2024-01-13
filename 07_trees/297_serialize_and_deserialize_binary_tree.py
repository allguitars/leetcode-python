'''
297. Serialize and Deserialize Binary Tree
https://leetcode.com/problems/serialize-and-deserialize-binary-tree

NeetCode: https://youtu.be/u4JAi2JJhI8

#Hard
#String #Tree #DFS #BFS #Design #BinaryTree

Similar Questions:
449. Serialize and Deserialize BST
https://leetcode.com/problems/serialize-and-deserialize-bst/
652. Find Duplicate Subtrees
https://leetcode.com/problems/find-duplicate-subtrees/

'''

from tree_operations.tree_node import TreeNode
from tree_operations.build_tree import with_bfs as build
from tree_operations.traverse_tree import with_bfs as traverse


class Codec:

    def serialize(self, root: TreeNode | None) -> str:
        '''
        利用 dfs 達成 preorder traversal
        '''
        res = []

        def dfs(node: TreeNode | None):
            if not node:
                # 空節點也要記錄
                res.append('N')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ','.join(res)

    def deserialize(self, data: str) -> TreeNode:
        vals = data.split(',')
        self.i = 0  # global variable

        def dfs() -> TreeNode | None:
            if vals[self.i] == 'N':
                self.i += 1
                return None

            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()


ser = Codec()
deser = Codec()

#     1
#   /   \
#  2     3
#       / \
#      4   5
root = build([1, 2, 3, None, None, 4, 5])
data = ser.serialize(root)  # data: '1,2,N,N,3,4,N,N,5,N,N' (preorder)
new_root = deser.deserialize(data)
assert traverse(new_root) == [1, 2, 3, None, None, 4, 5]

root = build([])
data = ser.serialize(root)  # data: 'N'
new_root = deser.deserialize(data)
assert traverse(new_root) == None

print('Pass')
