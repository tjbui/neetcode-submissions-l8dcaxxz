class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_height = 0

        while l < r:
            max_height = max(max_height, (r - l) * min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_height

# [1,7,2,5,4,7,3,6]
# [1, 2, 3]
#  0  1  2
#