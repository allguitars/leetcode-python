'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''


def three_sum(nums):
    res = []
    nums.sort()

    for i, n in enumerate(nums):
        # skip positive integers
        if n > 0:
            break

        # 如果不是最左邊的數字，且跟前一個數字相同，表示我們已經處理過相同的情況了。
        # 留意這個 list 是已經排序過了，所以右邊的數字一定大於或等於左邊的數字。
        if i > 0 and n == nums[i-1]:
            continue

        # i 位置確定可以使用，即確定了三個數字中的第一個，接著於右方的剩餘數字中找出另外兩個數字。
        # 此時問題變成解 two sum II (排序後的 two sum)，利用 Two Pointer 來解。
        l = i + 1
        r = len(nums) - 1

        while l < r:
            three_sum = n + nums[l] + nums[r]

            if three_sum > 0:  # too large, shrink from right
                r -= 1
            elif three_sum < 0:  # too small, shrink from left
                l += 1
            else:
                res.append([n, nums[l], nums[r]])

                # 當找到我們要的一組時，移動指標會比較特別。
                # [-2, -2, 0, 0, 2, 2]
                # 只需要移動 left pointer，因為如果總合太大，上面的條件式會幫忙處理 right pointer
                l += 1

                # 但是如果 left pointer 出現相同數字，為了避免同樣數組被加進 res，必須再移動一次 left pointer。
                while nums[l] == nums[l-1] and l < r:  # 注意 left 必須比 right 小
                    l += 1
    return res


assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
assert three_sum([0, 1, 1]) == []
assert three_sum([0, 0, 0]) == [[0, 0, 0]]

print('Pass')
