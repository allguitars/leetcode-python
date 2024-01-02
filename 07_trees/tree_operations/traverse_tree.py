from collections import deque


def with_bfs(root):
    if root is None:
        return

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
