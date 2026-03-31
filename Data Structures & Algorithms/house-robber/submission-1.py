class Solution:
    def rob(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        elif (len(nums) == 1):
            return nums[0]
        elif (len(nums) == 2):
            return max(nums[0], nums[1])
        elif (len(nums) == 3):
            return max(nums[0] + nums[2], nums[1])

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        dp[2] = max(nums[0] + nums[2], nums[1])
        i = 3
        while i < len(nums):
            dp[i] = max(nums[i] + dp[i - 2], nums[i-1] + dp[i - 3])
            i += 1
        
        return dp[len(nums) - 1]
