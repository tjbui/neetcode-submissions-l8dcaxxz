class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        
        longest = 0
        for i in nums:
            if i - 1 not in s:
                length = 1
                curr = i
                while curr + 1 in s:
                    curr += 1
                    length += 1
                longest = max(longest, length)

        return longest

# 
# [2,20,4,10,3,4,5]
# 2, 3, 4, 5
#
# set {2, 20, 4, 10, 3, 4, 5}
# 2 --> 3 --> 4 --> 5 -- > 6: no (longest = 4)
# 20 --> 21: no
# 10 --> 11: no
# ONLY CHECK BOTTOM OF SEQUENCE (i - 1 not in set)