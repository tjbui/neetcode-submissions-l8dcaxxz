class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for i in nums:
            result = result ^ i
        return result
        

# [3, 2, 3]
#

# 0011 
# 0011 XOR
# 0000

# 0000
# 0010 XOR
# 0010