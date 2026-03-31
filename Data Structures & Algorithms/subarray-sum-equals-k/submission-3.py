from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        m = defaultdict(int)
        m[0] = 1

        prefixSum = 0
        count = 0
        for i in nums:
            prefixSum += i
            
            difference = prefixSum - k
            count += m[difference]
            m[prefixSum] += 1


        return count



# [1, 1, 1, 1, 1, 1], k = 3
#
# subarr1: [1,         prefixSum = 1
# subarr2: [1, 1       prefixSum = 2
# subarr3: [1, 1, 1    prefixSum = 3  --> good
# subarr4: [1, 1, 1, 1 prefixSum = 4  --> subtract subarr1
# ...

# [1, -1, 1, 1], k = 1
# need to map prefixSum --> count because of negative numbers
# subarr1: [1,          prefixSum = 1
# subarr2: [1, -1       prefixSum = 0
# subarr3: [1, -1, 1    prefixSum = 1
# subarr4: [1, -1, 1, 1 prefixSum = 2 --> subtract subbarr1 OR subarr3

# cannot precompute because
# subarr1: [1,          prefixSum = 1
# subarr2: [1, -1       prefixSum = 0
# subarr3: [1, -1, 1    prefixSum = 1 --> at this point, only alllowed to
#                                         subtract subarr1 or subarr2
# subarr4: [1, -1, 1, 1 prefixSum = 2


# [-1, -1, 1], k = 0
# subarr1: [-1          prefixSum = -1
# subarr2: [-1, -1      prefixSum = -2
# subarr3: [-1, -1, 1   prefixSum = 1


