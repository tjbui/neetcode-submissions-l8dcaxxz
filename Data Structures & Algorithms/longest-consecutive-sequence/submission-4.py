class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for i in nums:
            if i - 1 not in s:
                count = 1
                curr = i
                while curr + 1 in s:
                    curr = curr + 1
                    count += 1
                longest = max(longest, count)

        return longest
        

# [2,20,4,10,3,4,5]
# 
# curr = 2, count = 1
# 2 --> 3 is in s, curr = 3, count = 2
# 3 --> 4 is in s, curr = 4, count = 3
# 4 --> 5 is in s, curr = 5, count = 4
# 5 --> 6 NOT in s