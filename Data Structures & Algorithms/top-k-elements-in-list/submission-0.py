from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for i in nums:
            d[i] = d[i] + 1

        h = []
        for key, value in d.items():
            heapq.heappush(h, (-value, key))

        res = []
        for i in range(0, k):
            res.append(heapq.heappop(h)[1])

        return res