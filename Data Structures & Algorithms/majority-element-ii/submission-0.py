from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        res = []
        for key, val in counts.items():
            if val > (n // 3):
                res.append(key)

        return res