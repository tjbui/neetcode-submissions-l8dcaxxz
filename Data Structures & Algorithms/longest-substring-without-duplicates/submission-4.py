from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = defaultdict(int)

        l, r = 0, 0
        best = 0
        while r < len(s):
            m[s[r]] += 1

            while m[s[r]] > 1:
                m[s[l]] -= 1
                l += 1

            best = max(best, r - l + 1)
            r += 1

        return best
        

# s = "zxyzxyz"

# Brute force:
# z
# zx
# zxy
# zxyz
# ...

# x
# xy
# xyz
# ...

# Sliding window
# zxyzxyz
# l
# r

# zxyzxyz
# l
#  r

# zxyzxyz
# l
#   r

# zxyzxyz
#  l
#    r