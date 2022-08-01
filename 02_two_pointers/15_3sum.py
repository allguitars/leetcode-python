'''
15. 3Sum
https://leetcode.com/problems/3sum/

NeetCode: https://youtu.be/jzZsG8n2R9A

#Medium #Array #TwoPointers #Sorting
'''


def three_sum(nums):
    nums.sort()
    res = []

    # linear scan from the left and pick the number as the first number of the triple
    for i, a in enumerate(nums):
        # The array has been sorted. If next number is the same, the result won't change,
        # so we skip it and continue to the round. (increment i by 1)
        if i > 0 and a == nums[i-1]:
            continue

        # once the first number is chosen, the rest two numbers will be a two-sum-ii problem
        l = i + 1
        r = len(nums) - 1

        # while the first number is fixed, do "two sum ii" algorithm on the
        # rest numbers of the right hand side
        while l < r:
            # to understand why this sub-problem is a two-sum-ii problem, imagine that
            # the sub-array is nums[l:r+1], and sum of nums[l] and nums[r] has to be
            # -a so that the three_sum can be zero -> in this case, target = -a
            three_sum = a + nums[l] + nums[r]
            if three_sum > 0:
                r -= 1
            elif three_sum < 0:
                l += 1
            else:  # threeSum == 0
                res.append([a, nums[l], nums[r]])

                # once an answer is hit, update the l,r pointers to find the potential pair of
                # the second and third numbers (first number is still fixed)
                # so, we move the l pointer to the next position
                # if the number at the next position is the same, then move again
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return res


nums = [-1, 0, 1, 2, -1, -4]
# nums = [-3, 3, 4, -3, 1, 2]
print(three_sum(nums))
