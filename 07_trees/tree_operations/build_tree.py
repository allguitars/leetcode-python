from collections import deque
from .tree_node import TreeNode


def with_bfs(values):
    if not values:
        return None
    # if len(values) == 1:
    #     return TreeNode(values[0])
    # if len(values) == 2:
    #     root = TreeNode(values[0])
    #     root.left = TreeNode(values[1])
    #     return root

    # create the root node
    root = TreeNode(values[0])
    # queue holds nodes (not values)
    queue = deque([root])

    i = 1
    while i < len(values):
        # handle the first node in the queue
        # pop it from the queue
        current_node = queue.popleft()

        # append left child if present
        if i < len(values) and values[i] is not None:
            # append left child node
            current_node.left = TreeNode(values[i])
            # enqueue the new node
            queue.append(current_node.left)
        i += 1

        # append right child if present
        if i < len(values) and values[i] is not None:
            # append left child node
            current_node.right = TreeNode(values[i])
            # enqueue the new node
            queue.append(current_node.right)
        i += 1

    return root
