from tree_operations.build_tree import with_bfs as build


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


values = [3, 9, 20, None, None, 15, 7]
root = build(values)

preorder_traversal(root)  # 3 9 20 15 7
print()
inorder_traversal(root)  # 9 3 15 20 7
