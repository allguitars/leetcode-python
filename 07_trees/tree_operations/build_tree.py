from collections import deque
from .tree_node import TreeNode


def with_bfs(values):
    if not values:
        return None
    if len(values) == 1:
        return TreeNode(values[0])
    if len(values) == 2:
        root = TreeNode(values[0])
        root.left = TreeNode(values[1])
        return root

    queue = deque()
    # create the root node
    root = TreeNode(values[0])
    # queue holds nodes (not values)
    queue.append(root)

    i = 1
    while i < len(values):
        # handle the first node in the queue
        # pop it from the queue
        current_node = queue.popleft()

        # append left child
        left_value = values[i]  # pick next value from list
        i += 1
        if left_value is not None:
            # append left child node
            current_node.left = TreeNode(left_value)
            # enqueue the new node
            queue.append(current_node.left)

        # append right child
        right_value = values[i]
        i += 1
        if right_value is not None:
            # append left child node
            current_node.right = TreeNode(right_value)
            # enqueue the new node
            queue.append(current_node.right)

    return root
