'''
226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/
neetcode: https://youtu.be/OnSn2XEQ4MY

#Easy

#Recursion
#DFS
#Tree
#BinaryTree

Similar Questions:
2415. Reverse Odd Levels of Binary Tree
https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

'''


class Solution(object):
    def invertTree(self, root):
        if not root:
            return None

        # swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


'''
       4
     /   \
    2     7
   / \   / \
  1   3 6   9

       4
     /   \
    7     2
   / \   / \
  9   6 3   1
'''
