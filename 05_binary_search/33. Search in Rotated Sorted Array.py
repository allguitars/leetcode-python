'''
33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

NeetCode: https://youtu.be/U8XENwh8Oy8

#Medium
#Array BinarySearch
'''

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m

            # m in left sorted portion
            if nums[l] <= nums[m]:
                # 先考慮 target 在 m 右邊的情況比較容易想
                # 因為 m 在 left sorted portion, 所以右邊的數字可能有小有大
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    # target 在 m 左邊
                    r = m - 1

            # m in right sorted portion
            else:
                # target 在 m 左邊的情況（有大有小）
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1


s = Solution()

assert (s.search([4, 5, 6, 7, 0, 1, 2], 0)) == 4
assert (s.search([4, 5, 6, 7, 0, 1, 2], 3)) == -1
assert (s.search([1], 0)) == -1

print('Pass')
