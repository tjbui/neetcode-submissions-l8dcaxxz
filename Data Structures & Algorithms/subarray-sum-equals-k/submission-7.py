from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preMap = defaultdict(int)
        preMap[0] = 1

        total = 0
        result = 0
        for i in range(len(nums)):
            total += nums[i]

            need_to_subtract = total - k
            result += preMap[need_to_subtract]
            preMap[total] += 1

        return result
        
# [2, -1, 1, 2], k = 2
#       