# 746. Min Cost Climbing Stairs
# neetcode: https://youtu.be/ktmzAZWkEZ0

# Time: O(n) -> n sub-problems
# Space: O(1) -> with DP solution, we can just use two extra variables


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # [10, 15, 20, 0]
        cost.append(0)

        # 從 15 開始往前更新每個元素的值  因為 20 的後面是 0  20+0代表不需要更新
        for i in range(len(cost) - 3, -1, -1):
            # compare the cost of 1-step jump and 2-step jump
            cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])  # 也可以寫成 cost[i] + min(cost[i+1], cost[i+2])

        return min(cost[0], cost[1])


cost = [10, 15, 20]
print(Solution().minCostClimbingStairs(cost))
