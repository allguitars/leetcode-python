from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root):
    if not root:
        return
    print(root.val, end=' ')
    preorder_traversal(root.left)
    preorder_traversal(root.right)


def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left)
    print(root.val, end=' ')
    inorder_traversal(root.right)


def preorder_traversal_list(root):
    res = []

    def helper(node):
        if not node:
            return
        res.append(node.val)
        helper(node.left)
        helper(node.right)

    helper(root)
    return res


def inorder_traversal_list(root):
    res = []

    def helper(node):
        if not node:
            return
        helper(node.left)
        res.append(node.val)
        helper(node.right)

    helper(root)
    return res


def with_bfs(root):
    # todo: fix following case
    #     1
    #   /   \
    #  2     3
    #   \   / \
    #   6  4   5
    #     / \
    #    7   8

    # result:
    # 1 2 3 None 6 4 5 None None None None 7 8
    # 目前會印出 [1, 2, 3, None, 6, 4, 5, None, None, None, None, None, None, 7, 8]

    if not root:
        return None

    queue = deque()
    queue.append(root)
    res = []

    def all_null(q):
        # 如果 queue 裡面剩下的都是 N  那就沒有必要再繼續處理
        return all(node.val == 'N' for node in q)

    # 需要繼續處理的例子如 queue: [N, N, 4, 5]  即同一層裡面還有 leaf
    # 但如果是 [N,N,N,N] 就跳出，例如節點 4 跟 5 會在 queue 裡面 append 四個 N
    while queue and not all_null(queue):
        current_node = queue.popleft()

        if (current_node.val == 'N'):
            # print('None', end=' ')
            res.append(None)
        else:
            # print(current_node.val, end=' ')
            res.append(current_node.val)

        # left child
        if current_node.left:
            queue.append(current_node.left)  # node or leaf
        else:
            queue.append(TreeNode('N'))  # 空節點加入值為 N 的節點
        # right child
        if current_node.right:
            queue.append(current_node.right)  # node or leaf
        else:
            queue.append(TreeNode('N'))  # 空節點加入值為 N 的節點

    return res


'''
#     1
#   /   \
#  2     3
#       / \
#      4   5

# result:
# 1 2 3 None None 4 5
'''
