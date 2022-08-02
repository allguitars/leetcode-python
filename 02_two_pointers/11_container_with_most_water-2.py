'''
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/

NeetCode: https://youtu.be/UuiTKBwPgAo

We want to maximize the area, so the width should be as big as possible.
So, we place the the left pointer on the far left and the right pointer on the far right.

How do we update the two pointers?
看哪一個移動可以增加面積
以第一輪來說  left 高度為 1  right 高度為 7
移動較高的一邊不會增加面積  因為水的高度受較矮的牆限制
所以移動 left 到 point 2 -> 高度 8 -> 這時候會受右邊限制因為 7 比 8 矮 -> 取 7 當高
此時寬為 7 高為 7 -> 面積 49

第二輪一樣移動比較矮的一邊  這時候移動右邊往前一格到 point 8 高度 3 -> 面積 6 * 3 = 18

依此類推  直到 left pointer 碰到 right pointer

Time: O(n)
'''


def max_area(height):
    l = 0
    r = len(height) - 1
    res = 0

    while l < r:
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return res


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(height))
