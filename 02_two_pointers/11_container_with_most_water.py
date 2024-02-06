'''
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/

NeetCode: https://youtu.be/UuiTKBwPgAo

#Medium
#Array #TwoPointers #Greedy
'''

from typing import List
import time


class Solution:
    def maxArea1(self, height: List[int]) -> int:
        '''
        Brute force solution
        Time: O(n^2).
        這個解法無法通過 LeetCode 的執行時間要求
        '''
        res = 0
        for l in range(len(height)):
            for r in range(l+1, len(height)):
                # 長 * 寬
                # 比較矮的一邊是瓶頸，當作寬。
                area = (r - l) * min(height[l], height[r])
                res = max(res, area)  # 更新結果
        return res

    def maxArea2(self, height: List[int]) -> int:
        '''
        Linear time solution with two extra pointers
        Time: O(n)
        '''
        res = 0
        l = 0
        r = len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1  # 包含兩邊相等的情況，移動哪一個 pointer 都沒關係。

        return res


s = Solution()

# 暴力解
start_us = time.time() * 1000000  # microsecond, 微秒
assert s.maxArea1([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
end_us = time.time() * 1000000
print(f'time consumed: {end_us - start_us} us')  # 費時 14.25 us

# O(n) 解
start_us = time.time() * 1000000
assert s.maxArea2([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
end_us = time.time() * 1000000
print(f'time consumed: {end_us - start_us} us')  # 費時 4.0 us

assert s.maxArea2([1, 1]) == 1

print('Pass')
