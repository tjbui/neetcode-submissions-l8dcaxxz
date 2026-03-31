from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)

        for num in nums:
            d[num] += 1
        
        res = 0
        count = 0
        for key, val in d.items():
            if val > count:
                res = key
                count = val
        
        return res