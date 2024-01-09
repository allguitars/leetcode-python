from collections import deque


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
    if not root:
        return None

    queue = deque()
    queue.append(root)

    while queue:
        # handle the first node in the queue
        # pop it from the queue
        current_node = queue.popleft()
        print(current_node.val, end=' ')

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
