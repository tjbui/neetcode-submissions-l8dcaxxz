class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for idx, num in enumerate(nums):
            needed = target - num

            if needed in d:
                return [d[needed], idx]
            else:
                d[num] = idx

        return []

# [3, 4, 5, 6], target = 7

# [3, 4, 5, 6]
#     i

# 3 --> 10 ? needs 7. 7 not in dict
# {3 --> 0}

# 4 --> 10 ? needs 3. 3 is in dict
# return [i, d[needed]]