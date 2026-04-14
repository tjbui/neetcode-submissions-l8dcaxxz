class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for ind, num in enumerate(nums):
            needed = target - num

            if needed in d:
                return [d[needed], ind]

            d[num] = ind

        return [-1, -1]

# nums = [3, 4, 5, 6], target = 7
# Output: [0, 1]

# [3, 4, 5, 6]

# Brute force, look at all pairs O(n^2)
# (3, 4), (3, 5), (3, 6)
# (4, 5), (4, 6)
# (5, 6)

# 3, 4, 5, 6
# 