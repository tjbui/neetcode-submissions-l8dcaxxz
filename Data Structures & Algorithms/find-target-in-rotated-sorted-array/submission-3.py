class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target: 
                return m
            elif nums[m] <= nums[r]: # right side is sorted
                if target >= nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else: # left side is sorted
                if target <= nums[m - 1] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1

        return -1


# [3, 4, 5, 6, 1, 2], target = 1
#  l     m        r

# [3, 4, 5, 6, 1, 2]
#           l     r



# 3          3, 4, 5, 1, 2
# sorted     unsorted

# 3, 4       5, 6, 1, 2
#            we know this side is unsorted, so other side is sorted