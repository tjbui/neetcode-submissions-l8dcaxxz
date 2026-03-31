class Solution:
    # O(n) time, O(1) space
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        total_water = 0
        max_left = height[l]
        max_right = height[r]
        while l < r:
            if max_left < max_right:
                l += 1
                total_water += max(0, max_left - height[l])
                max_left = max(max_left, height[l])
            else:
                r -= 1
                total_water += max(0, max_right - height[r])
                max_right = max(max_right, height[r])

        return total_water
            
        

# [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
#  l                          r
# max_left  = 0
# max_right = 1

# [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
#     l                       r
# Move l since 0 < 1
# total_water += 0 - height[i] ---> the minimum is 0 since we moved l bc l < r
# max_left  = 2
# max_right = 1

# [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
#     l                    r
# move r since 1 < 2
# total_water += 1 - height[i] ---> the minimum is 1 since we moved r bc r < l
# max_left  = 2
# max_right = 2

# [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
#        l                    r
# move l (doesn't matter)
# total_water += 2 - height[i] ---> the minimum is 2
# max_left  = 2
# max_right = 2