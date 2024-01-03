from tree_operations.build_tree import with_bfs as build
from tree_operations.tree_node import TreeNode


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:  # both of them are empty
        return True

    if not p or not q:  # one of them is empty
        return False

    if p.val != q.val:
        return False

    return (is_same_tree(p.left, q.left) and
            is_same_tree(p.right, q.right))


p = build([1, 2, 3])
q = build([1, 2, 3])
assert is_same_tree(p, q) == True

p = build([1, 2])
q = build([1, None, 2])
assert is_same_tree(p, q) == False

p = build([1, 2, 1])
q = build([1, 1, 2])
assert is_same_tree(p, q) == False

print('Pass')
