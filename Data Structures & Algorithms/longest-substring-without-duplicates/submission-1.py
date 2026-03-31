from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counts = defaultdict(int)

        left = 0
        right = 0
        best = 0
        while right < len(s):
            counts[s[right]] += 1
            while counts[s[right]] > 1:
                counts[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)
            right += 1

        return best

# "abcabcbb"
# left = 0 
# right = 3
# {a --> 2, b --> 1, c --> 1}
# abca


# "zxyzxyz"
# z
# zx
# zxy
# zxyz    --> duplicate
#  xyz
#  xyzx   --> duplicate
#   yzx


# "xyzywd"
# x
# xy
# xyz
# xyzy    --> duplicate
#  yzy
#   zy
#   zyw
#   zywd