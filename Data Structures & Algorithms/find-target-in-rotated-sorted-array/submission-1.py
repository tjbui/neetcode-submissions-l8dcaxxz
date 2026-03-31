class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            if nums[l] <= nums[m]: # case left is sorted
                if target >= nums[l] and target < nums[m]: # in sorted side
                    r = m - 1
                else: # in unsorted side
                    l = m + 1
            else: # case right is sorted
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        if nums[l] == target:
            return l

        return -1
        

# [4, 5, 6, 7, 8, 9, 0, 1, 2], target = 0
#  l           m           r
# 7 > 4 ---> we know left side is sorted
#       ---> is target between 4 and 7? No, so search right


# [8, 9, 0, 1, 2], target = 0
#  l     m     r
# 0 < 8 ---> we know right side is sorted
#       ---> is target between 0 and 2? Yes, so search right

# [0, 1, 2], target = 0
#  l  m  r
# 1 > 0 ---> we know left side is sorted
#       ---> is target between 0 and 1? Yes, so search left

# [0, 1]
#  l  r
#  m
# 0 >= 0 ---> left side is sorted
#        ---> is target between 0 and 0? Yes so search left


# [3, 5, 6, 0, 1, 2]
#  l     m        r
# 
# [3, 5, 6]
#  l  m  r

# [3, 5]
#  l  r
#  m

# [5]
#  l
#  m
#  r