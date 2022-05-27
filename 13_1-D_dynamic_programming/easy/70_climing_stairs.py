# 70. Climbing Stairs
# neetcode: https://youtu.be/Y0lT9Fck7qI

# Time: O(n)
# Space: two variables (we don't even need the entire array of n elements)

class Solution(object):
    def climbStairs(self, n):
        one, two = 1, 1

        for _ in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one


n = 5
print(Solution().climbStairs(n))
