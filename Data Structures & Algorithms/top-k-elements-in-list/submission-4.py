from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        
        h = []
        for key, value in d.items():
            heapq.heappush(h, (-value, key))

        ret = []        
        for i in range(0, k):
            ret.append(heapq.heappop(h)[1])
    
        return ret

# [1, 2, 2, 3, 3, 3], k = 2
# 1 --> 1
# 2 --> 2
# 3 --> 3

#    3
#  2   1
# pop() --> 3
# pop() --> 2