class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = 100
        maxDiff = 0

        for num in prices:
            if num - minBuy > maxDiff:
                maxDiff = num - minBuy

            if num < minBuy:
                minBuy = num

        return maxDiff