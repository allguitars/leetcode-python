'''
167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

NeetCode: https://youtu.be/cQ1Oz4ckceM

Time: O(n)
Space: O(1)

#Medium #Array #TwoPointers #BinarySearch
'''


def two_sum(numbers, target):
    l = 0
    r = len(numbers) - 1

    while True:
        sum = numbers[l] + numbers[r]

        # array is ready sorted, so if the sum is greater than target,
        # it means we need to make the bigger number (right poiter) smaller
        # otherwise, if the sum is smaller, we need to increase the smaller number
        if sum < target:
            l += 1

        if sum > target:
            r -= 1

        if sum == target:
            return [l+1, r+1]


# numbers = [1, 3, 4, 5, 7, 10, 11]
numbers = [1, 3, 4, 5, 7, 11]
target = 9

print(two_sum(numbers, target))
