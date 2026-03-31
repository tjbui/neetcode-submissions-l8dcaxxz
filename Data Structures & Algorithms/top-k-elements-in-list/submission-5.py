from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for i in nums:
            counts[i] += 1

        heap = []
        for key, value in counts.items():
            heapq.heappush(heap, (-value, key))

        result = []
        for i in range(0, k):
            result.append(heapq.heappop(heap)[1])

        return result
        
# [1, 2, 2, 3, 3, 3], k = 2
# 1 --> 1
# 2 --> 2
# 3 --> 3

#  3
# 2 1
# pop() --> 3, pop() --> 2