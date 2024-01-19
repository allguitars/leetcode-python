'''
1. Two Sum
https://leetcode.com/problems/two-sum/

neetcode: https://youtu.be/KLlXCFG5TnA

Using a hashmap
Time: O(n)
Space: O(n) -> to maintain the hashmap

#Easy
#Array #HashTable
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # val: index
        # every element that comes before the current element will be stored in this hashmap
        previous_map = {}

        for index, number in enumerate(nums):
            diff = target - number

            if diff in previous_map:
                return [previous_map[diff], index]

            previous_map[number] = index

        # this line will not be executed as we assume the pair always exists
        return None


nums = [2, 7, 11, 15]
target = 9

# nums = [3, 2, 4]
# target = 6

# nums = [3, 3]
# target = 6

print(Solution().twoSum(nums, target))
