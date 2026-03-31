class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxLen = 0
        curLen = 0
        my_set = set()

        while right < len(s):
            if s[right] in my_set:
                my_set.remove(s[left])
                left += 1
                curLen -= 1
            else:
                my_set.add(s[right])
                right += 1
                curLen += 1
                if curLen > maxLen:
                    maxLen = curLen

        return maxLen
            

