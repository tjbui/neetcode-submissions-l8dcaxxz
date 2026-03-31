class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for i in nums:
            if (i - 1) not in s:
                cur = 1
                while (i + 1) in s:
                    cur += 1
                    i += 1
                longest = max(longest, cur)
        return longest