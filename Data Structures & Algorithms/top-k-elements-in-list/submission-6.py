from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for i in nums:
            counts[i] += 1

        buckets = [[] for _ in range(0, len(nums) + 1)]
        for key, value in counts.items():
            buckets[value].append(key)
        
        counter = 0
        ind = len(nums)
        res = []
        while counter < k:
            if len(buckets[ind]) > 0:
                res.append(buckets[ind].pop())
                counter += 1
                continue
            ind -= 1

        return res
        

# bucket sort
# [1, 2, 2, 3, 3, 3, 4, 4, 4]
# 
# 1 --> 1
# 2 --> 2
# 3 --> 3
# 4 --> 3
#
# [[], [1], [2], [3, 4], [], [], [], [], []]