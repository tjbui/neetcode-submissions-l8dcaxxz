class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        runningCount = 0
        res = nums[0]

        for num in nums:
            if num == res:
                runningCount += 1
            else:
                runningCount -= 1
            if runningCount < 0:
                res = num

        return res
