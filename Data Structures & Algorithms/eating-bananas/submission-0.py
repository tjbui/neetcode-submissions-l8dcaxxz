import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            m = (l + r) // 2  # Current k

            total = 0
            for i in piles:
                total += math.ceil(i / m)
            
            if total > h:
                l = m + 1
            else:
                r = m

        return l



