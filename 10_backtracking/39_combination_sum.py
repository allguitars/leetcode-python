'''
39. Combination Sum
https://leetcode.com/problems/combination-sum/description/

NeetCode: https://youtu.be/GBKI9VSKdGg

Combination vs. Permutation
組合 -> 同樣的數字，順序改變，仍算是一種情況。

Time: O(2^t), where t = target

#Medium
#Array #Backtracking
'''

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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


s = Solution()

# candidates, target
print(s.combinationSum([2, 3, 5], 8))

# 這個方法無法排除相同組合但順序不同的  例如 [3,5] and [5,3]
# Output:
# [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
