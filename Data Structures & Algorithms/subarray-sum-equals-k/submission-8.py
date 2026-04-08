from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefSums = defaultdict(int)
        prefSums[0] = 1

        out = 0
        currSum = 0
        for i in nums:
            currSum += i

            difference = currSum - k # k = currSum - difference
            if prefSums[difference] > 0:
                out += prefSums[difference]
            
            prefSums[currSum] += 1

        return out

        

# [2, -1, 1, 2], k = 2
# 
# [2] --> = k
# [2, -1]
# [2, -1, 1] --> = k
# [2, -1, 1, 2]

# [-1]
# [-1, 1]
# [-1, 1 2] --> = k
# ...


# [2, -1, 1, 2], k = 2
#  
# [2]  prefSum = {0 --> 1}
#      currSum = 2

# [2, -1] prefSum = {2 --> 1}
#         currSum = 1

# 