class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        l = 0
        r = 1
        best = 0
        while r < len(prices):
            best = max(best, prices[r] - prices[l])

            if prices[l] > prices[r]:
                l = r
            r += 1

        return best

        

# [10, 1, 5, 6, 7, 1]
# buy on 1, sell on 7


# [10, 1, 5, 6, 7, 1]
#   l  r

# [10, 1, 5, 6, 7, 1]
#      l  r           --> max = 4

# [10, 1, 5, 6, 7, 1]
#      l     r        --> max = 5

# [10, 1, 5, 6, 7, 1]
#      l        r     --> max = 6