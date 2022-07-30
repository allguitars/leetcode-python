'''
79. Word Search
'''


def exist(board, word):
    ROWS = len(board)
    COLS = len(board[0])
    path = set()

    def dfs(r, c, pos):
        # pos reached the end, meaning we got the whole word matched
        if pos == len(word):
            return True

        # out of bounds || cell does not match the letter || cell already visited
        if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[pos] != board[r][c] or (r, c) in path):
            return False

        # cell matches the current letter but we have not reached the end of the word
        # continue dealing with the remaining letters

        # mark current cell as vistited
        path.add((r, c))

        # move on to the next cell
        # imagine that, in each recursive call,
        # we treat it as if we are starting from the begining with that cell
        result = (dfs(r+1, c, pos+1) or
                  dfs(r-1, c, pos+1) or
                  dfs(r, c+1, pos+1) or
                  dfs(r, c-1, pos+1))

        # BACKTRACK: remove the mark as we do not want to mess with other paths
        # 到這個關鍵點，表示不管有沒有找到，"從我這一cell開始"的所有可能性我都走過了。
        # 當我要把結果回傳時，就要清除我現在的足跡。
        # 如此一來，退回到我"前一步"要從其他相鄰cell重新開始時，才不會被舊足跡阻礙。
        path.remove((r, c))

        return result

    # start from any cell in the board
    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0):
                return True

    return False


board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]

word = "ABCCED"

print(exist(board, word))
