from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1

        pref_sum = 0
        count = 0

        for num in nums:
            pref_sum += num
            cut_needed = pref_sum - k
            count += d[cut_needed]

            d[pref_sum] += 1

        return count
        

# [2, -1, 1, 2] k = 2

# pref_sum = 0, count = 0
# {0 --> 1}

# idx = 0, nums[idx] = 2
# pref_sum = 2, count = 1       [2]
# {0 --> 1, 2 --> 1}

# idx = 1, nums[idx] = -1
# pref_sum = 1, count = 1       [2, -1]
# {0 --> 1, 2 --> 1, 1 --> 1}

# idx = 2, nums[idx] = 1
# pref_sum = 2, count = 2       [2, -1, 1]
# {0 --> 1, 2 --> 2, 1 --> 1}

# idx = 3, nums[idx] = 2
# pref_sum = 4, count = 4       [2, -1, 1, 2]
# {0 --> 1, 2 --> 2, 1 --> 1}

