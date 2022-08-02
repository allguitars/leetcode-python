'''
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/

NeetCode: https://youtu.be/UuiTKBwPgAo

Time: O(n^2)
'''

# Brute force
# This will not pass the time contraint on LeetCode.


def max_area(height):
    res = 0

    for l in range(len(height)):
        for r in range(l+1, len(height)):
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)
    return res


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(height))
