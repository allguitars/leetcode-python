'''
78. Subsets (Medium)
https://leetcode.com/problems/subsets/

Neetcode: https://youtu.be/REOH22Xwdkk

#Backtracking 
#Note(notability)
'''


def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return

        # decision to include nums[i]
        subset.append(nums[i])
        dfs(i+1)

        # decision NOT to include nums[i]
        # 用 pop() 即可還原 subset 狀態，不需要額外的變數來保存。
        subset.pop()
        dfs(i+1)

    dfs(0)
    return res


nums = [1, 2, 3]
print(subsets(nums))

# [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
