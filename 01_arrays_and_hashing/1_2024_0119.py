from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}  # val: index

        for i, n in enumerate(nums):
            diff = target - n

            if diff in map:
                return [map[diff], i]

            map[n] = i

        return


s = Solution()

assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
assert s.twoSum([3, 2, 4], 6) == [1, 2]
assert s.twoSum([3, 3], 6) == [0, 1]

print('Pass')
