from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []

        counts = defaultdict(int)
        for i in nums:
            counts[i] += 1

        for key, value in counts.items():
            heapq.heappush(maxHeap, (-value, key))

        result = []
        for i in range(k):
            result.append(heapq.heappop(maxHeap)[1])

        return result
# 