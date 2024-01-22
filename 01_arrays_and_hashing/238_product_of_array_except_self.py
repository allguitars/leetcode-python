'''
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

NeetCode: https://youtu.be/bNvIQI2wAjk

#Medium
#Array #PrefixSum
'''

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # 從陣列前面開始掃，產生所有位置的 prefix 值
        # 每個位置擁有前面所有數字（不包含自己）相乘的結果
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]  # update the prefix

        # 從後面開始掃，算是每個位置的 suffix
        # 但差別在於，直接乘上之前所存的 prefix 值，計算出該位置的答案。
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * suffix  # 直接計算結果，不存 suffix
            suffix = suffix * nums[i]

        return res


s = Solution()

assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

print('Pass')
