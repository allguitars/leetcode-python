try:
    # Works when we're at the top level
    from tree_operations import build_tree, traverse_tree
except ImportError:
    # If we're not in the top level
    # And we're trying to call the file directly
    import sys
    # sys.path[0] is the current file's path
    # 把含有 tree_operations 的父目錄加到 system path
    sys.path.append(sys.path[0] + '/..')
    from tree_operations import build_tree, traverse_tree
