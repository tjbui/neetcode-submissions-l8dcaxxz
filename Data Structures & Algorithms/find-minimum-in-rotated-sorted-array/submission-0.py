class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            if nums[m] < nums[r]:
                r = m

        return nums[l]                
        

# 3, 4, 5, 1, 2
# l     m     r

# 1, 2
# l  r
# m 