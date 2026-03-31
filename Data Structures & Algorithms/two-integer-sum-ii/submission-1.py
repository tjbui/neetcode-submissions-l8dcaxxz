class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while (l < r):
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l + 1, r + 1]
        
        # invalid
        return []
        

# [1, 2, 3, 4], target = 3
#  1   2   3   4 
#  l   r    

# 1 + 4 = 5 --> too big
# 1 + 3 = 4 --> too big
# 1 + 2 = 3 --> correct