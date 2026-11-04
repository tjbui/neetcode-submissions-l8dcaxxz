class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        maxArea = 0
        while l < r:
            maxArea = max(maxArea, (r - l) * min(heights[l], heights[r]))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxArea

# 1, 7, 2, 5, 4, 7, 3, 6
# l
# 


#     c     c
#
# 0 1 2 3 4 5 6 7