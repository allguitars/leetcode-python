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

from collections import deque


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


# ** Iterative BFS **
# We are traversing the tree level by level until we get
# to the last level and we cannot continue anymore
# So, we are counting the levels that we have
def max_depth2(root):
    '''
    Iterative BFS
    '''
    if not root:
        return 0

    # maintain the level
    level = 0
    # nice trick here, we directly put the first element in it
    # when initializing it
    q = deque([root])

    while q:
        # 在每一輪的 while loop 裡面，queue 只會有"某一層"裡面所有的節點
        # 所以 while 的開頭，即表示開始處理新的一層，故 level 數目加一
        level += 1
        # 所以我先計算這一層有幾個節點，即目前 queue 的長度。
        for i in range(len(q)):
            node = q.popleft()
            # 將子節點加到 queue
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return level


# ** Iterative DFS **
# 沒有遞迴的 DFS
# Implement a STACK data structure to emulate
# Pre-order DFS
def max_depth3(root):
    '''
    Iterative DFS
    '''
    # 用陣列即可模擬 stack
    stack = [[root, 1]]  # 同時紀錄目前的 level 數
    level = 0

    while stack:
        node, depth = stack.pop()

        if node:
            level = max(level, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
            # 即使子節點有可能是空的，但我們在 while 下一輪會用 if node: 過濾

    # 如果最開始加入 stack 的 root 是 None，雖然 while stack 會進入
    # 但是裡面的 if node: 不會執行，故 level 仍保持為 0
    return level


def main():
    values = [3, 9, 20, None, None, 15, 7]
    root = build_tree.with_bfs(values)  # build tree
    assert max_depth1(root) == 3  # test result
    assert max_depth2(root) == 3
    assert max_depth3(root) == 3

    values = [1, None, 2]
    root = build_tree.with_bfs(values)
    assert max_depth1(root) == 2
    assert max_depth2(root) == 2
    assert max_depth3(root) == 2

    print('Pass')


if __name__ == '__main__':
    main()
