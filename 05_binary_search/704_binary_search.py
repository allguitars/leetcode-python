# 704. Binary Search

# NeetCode: https://youtu.be/s4DPM8ct1pI

# time: O(log n)

class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:    # 關於為何有等號，可以考慮list只有一個元素的狀況。這時候 l == r
            m = (l + r) // 2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return -1


nums1 = [-1, 0, 3, 5, 9, 12]
target = 9
print(Solution().search(nums1, target))

nums2 = [-1, 0, 3, 5, 9, 12]
target2 = 2
print(Solution().search(nums2, target2))

nums3 = [-1, 0, 3, 5, 9, 12]
target3 = 13
print(Solution().search(nums3, target3))
