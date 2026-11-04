class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            needed = target - nums[i]
            
            if needed in d:
                return [d[needed], i]

            d[nums[i]] = i

        return [-1, -1]

# 3, 4, 5, 6, target = 7
#
# 3, 4, 5, 6, target = 7
# i
# 
# 7 - 3 = 4
# 