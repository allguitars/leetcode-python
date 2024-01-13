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

        def dfs(i, cur, total):
            if sum(cur) == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or sum(cur) > target:
                return

            # include item at index i to the sub-array
            cur.append(candidates[i])

            # 1. decision to keep adding current item -- do not change i
            dfs(i, cur, total + candidates[i])

            # restore the sub-arr after recursive call for making other decision
            cur.pop()

            # 2. decision NOT to go with current item anymore -- increment i
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res


s = Solution()

# candidates, target
print(s.combinationSum([2, 3, 5], 8))

# Output:
# [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
