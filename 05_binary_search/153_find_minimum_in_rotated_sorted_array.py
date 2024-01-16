'''
153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

NeetCode: https://youtu.be/nIVW4P8b1VA

#Medium
#Array #BinarySearch
'''

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # just pick the first value from the list to be the initial value
        # this variable will be updated during the process
        res = nums[0]
        l, r = 0, len(nums) - 1  # leftmost and rightmost

        while l <= r:
            if nums[l] < nums[r]:
                # 如果目前區間已經排序，則最小值可能在最左邊。
                res = min(res, nums[l])
                # 且已經沒有必要再移動 m location

            # 如果仍跨越兩個排序區間，則繼續切半。

            m = (l + r) // 2
            res = min(res, nums[m])  # 看 m 有沒有剛好切在最小值上

            # 看 m 是切在哪一區間
            if nums[m] >= nums[l]:
                # 例如 [4,5,6,1,2,3] 中 6 位於左半區間，則最小值應該要往右找
                l = m + 1  # 切右半邊
            else:
                r = m - 1  # 切左半邊

        return res


s = Solution()

assert s.findMin([3, 4, 5, 1, 2]) == 1
assert s.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
assert s.findMin([11, 13, 15, 17]) == 11

print('Pass')
