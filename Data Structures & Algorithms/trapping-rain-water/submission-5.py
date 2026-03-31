class Solution:
    # O(n) time, O(n) space
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        curr_max = 0
        for i in range(1, len(height)):
            curr_max = max(curr_max, height[i - 1])
            max_left[i] = curr_max

        max_right = [0] * len(height)
        curr_max = 0
        for i in range(len(height) - 2, -1, -1):
            curr_max = max(curr_max, height[i + 1])
            max_right[i] = curr_max
                
        total_water = 0
        for i in range(len(height)):
            total_water += max(0, min(max_right[i], max_left[i]) - height[i])

        return total_water

# [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
# position 0:
#       max_height_left = 0, 
#       max_height_right = 3,
#       height[0] = 0,
#       total_water = 0 (+0)
# position 1:
#       max_height_left = 0, 
#       max_height_right = 3,
#       height[1] = 2
#       total_water = 0 (+0)
# position 2:
#       max_height_left = 2,
#       max_height_right = 3,
#       height[2] = 0
#       total_water = 2 (+2)

#            [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
# max_left:  [0, 0, 2, 2, 3, 3, 3, 3, 3, 3]
# max_right: [3, 3, 3, 3, 3, 3, 3, 2, 1, 0]
#