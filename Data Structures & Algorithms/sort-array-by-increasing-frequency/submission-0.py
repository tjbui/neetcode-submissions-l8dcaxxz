from collections import defaultdict

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hmap = defaultdict(int)

        for i in nums:
            hmap[i] += 1

        def sort_func(i):
            return (hmap[i], -i)

        nums.sort(key=sort_func)

        return nums
        

# [1,1,2,2,2,3]
#
# 