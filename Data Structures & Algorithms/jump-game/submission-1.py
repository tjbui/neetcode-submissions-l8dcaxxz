class Solution:
    # DP solution O(n^2)
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            for j in range(0, nums[i] + 1):
                if i + j < len(nums) and dp[i + j] == True:
                    dp[i] = True

        return dp[0]


# [1, 2, 0, 1, 0]
#  p
#     p
#           p
#              p