try:
    # Works when we're at the top level
    from tree_operations import b
except ImportError:
    # If we're not in the top level
    # And we're trying to call the file directly
    import sys
    # sys.path[0] is the current file's path
    # 把含有 tree_operations 的父目錄加到 system path
    sys.path.append(sys.path[0] + '/..')
    from tree_operations import build_tree


def max_depth1(root):
    '''
    Recursive DFS
    '''
    # base case: 空樹沒有深度
    if not root:
        return 0

    # 如果這一層有節點，則深度至少有 1
    # 然後再比較左右子樹的 max depth，取較大的一個加上本身的 1
    # 如果沒有子節點，則兩個 0 取較大值仍為 0
    left_max_depth = max_depth1(root.left)
    right_max_depth = max_depth1(root.right)
    return 1 + max(left_max_depth, right_max_depth)


def main():
    values = [3, 9, 20, None, None, 15, 7]
    root = build_tree.with_bfs(values)  # build tree
    assert max_depth1(root) == 3  # test result

    values = [1, None, 2]
    root = build_tree.with_bfs(values)
    assert max_depth1(root) == 2

    print('Pass')


if __name__ == '__main__':
    main()
