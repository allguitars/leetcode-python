class Solution(object):
    def max_profit(self, prices):
        # initialization
        max_profit = 0  # result
        l = 0  # left: buy, right: sell

        # moving of the main pointer
        for r in range(1, len(prices)):

            # condition for when to calculate the result
            # 在任何時刻，只要左邊價格較低，就計算價差，並和目前的最大值做比較。如果發現比較大就取代原有的價差。
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                # 當新（右邊）價格比舊（左邊）的價格還要低的時候
                # 表示我們遇到了一個"目前所知"最低價！
                # 所以將其當作新的基準點，然後往右找較高價計算價差。
                l = r  # 將目前的新低價作為新的基準點

        return max_profit


prices = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]
assert Solution().max_profit(prices) == 5
assert Solution().max_profit(prices2) == 0

print('Pass')
