# neetcode: https://youtu.be/1pkOgXD63yU


class Solution(object):
    def maxProfit(self, prices):
        l, r = 0, 1  # left=buy, right=sell
        maxProfit = 0

        while r < len(prices):   # every iteration is to find the maximum profit
            # profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:  # right value is lower, so we make it the new left pointer (new starting point)
                l = r

            r += 1  # right pointer shifts for every iteration

        return maxProfit


prices = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]
print(Solution().maxProfit(prices))
