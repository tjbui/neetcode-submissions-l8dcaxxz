class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 0

        while r < len(nums):
            nums[l] = nums[r]
            while r < len(nums) and nums[r] == nums[l]:
                r += 1
            l += 1
        
        return l


# [1, 1, 2, 3, 4]
# [1, 2, 3, 4, x]              


# [2, 10, 10, 10, 30, 30, 30]
# [2, 10, 30,  x,  x,  x,  x]

# [2, 10, 10, 10, 30, 30, 30]
#                          r 

# [2, 10, 30]
#          l