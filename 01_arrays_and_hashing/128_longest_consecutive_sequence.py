'''
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/

NeetCode: https://youtu.be/P6RZZMu_maU

#Medium
#Array #HashTable #UnionFind
'''

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert the input list into a set
        nums_set = set(nums)
        longest_length = 0

        for n in nums:
            # check if the number is the start of the sequence
            if n - 1 not in nums_set:
                # 如果這個數字沒有左邊的臨近數字，表示它可以當一個數列的開頭。
                # 往右邊的鄰近數字開始計算連續數列的長度
                length = 0
                while n + length in nums_set:  # 例如，若有數列 (1,2,3) 在 set 中，length
                    length += 1

                longest_length = max(length, longest_length)

        return longest_length


s = Solution()

assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
assert s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9

print('Pass')
