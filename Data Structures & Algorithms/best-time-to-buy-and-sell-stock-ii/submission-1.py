class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n

        for i in range(1, n):
            max_diff = 0
            for j in range(0, i):
                if prices[i] - prices[j] + dp[j] > max_diff:
                    max_diff = prices[i] - prices[j] + dp[j]
            
            dp[i] = max(max_diff, dp[i - 1])

        return dp[n - 1]