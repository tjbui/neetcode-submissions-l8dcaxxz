class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return max(dp[len(nums) - 1], dp[len(nums) - 1])
        
# [1, 1, 3, 3]

# [1]
# [1, 1]

# Two choices: either we take nums[i] or we take nums[i - 1]
# DP[i] = best we can get if we take nums[i]