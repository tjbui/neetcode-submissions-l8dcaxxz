from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        m = defaultdict(int)
        m[0] = 1

        prefixSum = 0
        total = 0
        for num in nums:
            prefixSum += num
            diff = prefixSum - k

            total += m[diff]
            m[prefixSum] += 1

        return total

        

# [2, -1, 1, 2], k = 2
# subarr1: [2            prefixSum = 2, need 0 --> +1
# subarr2: [2, -1        prefixSum = 1, need 1
# subarr3: [2, -1, 1     prefixSum = 2, need 0 --> +1
# subarr4: [2, -1, 1, 2  prefixSum = 4, need 2 --> +2
# return 4

# edge case k = 0
# [-1, -1]
# subarr1: [-1           prefixSum = -1, need -1 --> non empty so don't add 1
# subarr2: [-1, -1        prefixSum = -2, need -2 --> non empty so don't add 1
# return 0 


