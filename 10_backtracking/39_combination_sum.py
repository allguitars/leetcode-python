'''
#Medium #Array #Backtracking
39. Combination Sum

NeetCode: https://youtu.be/GBKI9VSKdGg
'''


def combination_sum(candidates, target):
    res = []
    current = []

    def dfs(i):
        if sum(current) == target:
            res.append(current.copy())
            return
        if i >= len(candidates) or sum(current) > target:
            return

        # include item at index i to the sub-array
        current.append(candidates[i])

        # 1. decision to keep adding current item -- do not change i
        dfs(i)

        # restore the sub-arr after recursive call for making other decision
        current.pop()

        # 2. decision NOT to go with current item anymore -- increment i
        dfs(i+1)

    dfs(0)
    return res


candidates = [2, 3, 5]
target = 8

print(combination_sum(candidates, target))

# 這個方法無法排除相同組合但順序不同的  例如 [3,5] and [5,3]
# Output:
# [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
