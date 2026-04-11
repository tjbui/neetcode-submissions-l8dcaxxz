class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        def houseRobber1(arr):
            if len(arr) == 0:
                return 0
            if len(arr) == 1:
                return arr[0]

            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 1], arr[i] + dp[i - 2])

            return dp[len(arr) - 1]

        firstHouse = houseRobber1(nums[1:])
        lastHouse = houseRobber1(nums[:len(nums) - 1])

        return max(firstHouse, lastHouse)

        

# [2, 9, 8, 3, 6]

# Run house robber 1 on [9, 8, 3, 6]
# Run house robber 1 on [2, 9, 8, 3]
# return best