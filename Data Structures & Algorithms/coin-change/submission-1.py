class Solution:
    # greedy doesn't work
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)

        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        if dp[amount] == amount + 1:
            return -1
        return dp[amount]
        
            
# [3, 3, 5], amount = 6
# counter example for greedy

# DP[i] = minimum amount of coins to make amount = i
# DP[0] = 0
# DP[1] = 