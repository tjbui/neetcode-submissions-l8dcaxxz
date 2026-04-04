class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [-1000] * (len(nums) + 1)
        dp[0] = -1000

        for i in range(1, len(nums) + 1):
            dp[i] = max(nums[i - 1], nums[i - 1] + dp[i - 1])

        best = -1000
        for i in range(len(dp)):
            best = max(best, dp[i])

        return best


# [2,-3,4,-2,2,1,-1,4]
# out = 8

# [2]

# [2, -3]

# [2, -3, 4]

# DP[i] = sum of the maximum subarray for nums[0: i] where we must choose i
# DP[0] = 0