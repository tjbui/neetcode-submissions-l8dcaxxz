class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1, p2 = 0, 0
        count = 0

        while p2 < len(nums):
            if nums[p2] != val:
                nums[p1] = nums[p2]
                p1 += 1

                count += 1
            p2 += 1

        return count
            



# nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
# 
# [0, 1, 2, 2, 3, 0, 4, 2]
#  p1
#  p2

# [0, 1, 2, 2, 3, 0, 4, 2]
#     p1
#     p2

# [0, 1, 2, 2, 3, 0, 4, 2]
#        p1
#        p2

# [0, 1, 2, 2, 3, 0, 4, 2]
#        p1
#           p2

# [0, 1, 2, 2, 3, 0, 4, 2]
#        p1
#              p2

# [0, 1, 3, 2, 3, 0, 4, 2]
#           p1
#                 p2

# [0, 1, 3, 0, 3, 0, 4, 2]
#              p1
#                    p2