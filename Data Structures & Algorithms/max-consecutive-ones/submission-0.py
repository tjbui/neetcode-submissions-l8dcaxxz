class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        running_count = 0

        for i in nums:
            if i == 1:
                running_count += 1
                best = max(best, running_count)
            else:
                running_count = 0

        return best
        

# [1,1,0,1,1,1]
# 