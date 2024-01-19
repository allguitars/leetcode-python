'''
217: Contains duplicate
https://leetcode.com/problems/contains-duplicate/

NeetCode: https://youtu.be/3OamzN90kPg

#Easy
#Array #HashTable #Sorting
'''


class Solution(object):
    def containsDuplicate(self, nums):

        hashset = set()

        for n in nums:
            if n in hashset:
                return True

            hashset.add(n)

        return False


nums = [1, 2, 3, 1]
print(Solution().containsDuplicate(nums))

# Time complexity: O(n)
# Memory complexity: O(n)
