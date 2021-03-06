# 121: Best time to buy and sell stock
# neetcode: https://youtu.be/1pkOgXD63yU


class Solution(object):
    def maxProfit(self, prices):
        l, r = 0, 1  # left=buy, right=sell
        max_profit = 0

        while r < len(prices):   # every iteration is to find the maximum profit
            # profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:  # right value is lower, so we make it the new left pointer (new starting point)
                l = r

            r += 1  # right pointer shifts for every iteration

        return max_profit


prices = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]
print(Solution().maxProfit(prices))
