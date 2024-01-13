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
        # ** NeetCode 的寫法 ======
        # 每次遞迴呼叫只做一次加法，即 total + candidates[i]
        # 整體速度會快幾 ms
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
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

        # ** 簡化寫法，不用傳入那麼多參數 ======
        # 我自己的寫法，但是每次呼叫 dfs 都要將所有元素加一次  會比上面的方法慢幾 ms
        # res = []
        # cur = []

        # def dfs(i):
        #     # total = sum(cur)
        #     if sum(cur) == target:
        #         res.append(cur.copy())
        #         return
        #     if i >= len(candidates) or sum(cur) > target:
        #         return

        #     # 要包含 candidates[i]
        #     cur.append(candidates[i])
        #     dfs(i)
        #     # 一定不含 candidates[i], 只能有 i+1 之後的數字
        #     cur.pop()
        #     dfs(i+1)

        # dfs(0)
        # return res


s = Solution()

# candidates, target
print(s.combinationSum([2, 3, 5], 8))

# Output:
# [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
