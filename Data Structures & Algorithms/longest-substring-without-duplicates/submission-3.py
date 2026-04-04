class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        charSet = set()

        best = 0
        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])

            best = max(best, r - l + 1)
            r += 1

        return best

