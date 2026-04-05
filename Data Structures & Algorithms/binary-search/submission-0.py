class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return -1
        

# [-1, 0, 2, 4, 6, 8], target = 4
#   l              r
#         m

# [-1, 0, 2, 4, 6, 8], target = 4
#            l     r
#               m

# [-1, 0, 2, 4, 6, 8], target = 4
#            l     
#            r  
#            m 