from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0

        best = 0
        m = defaultdict(int)
        while r < len(s):
            m[s[r]] += 1
            while m[s[r]] > 1:
                m[s[l]] -= 1
                l += 1

            best = max(best, r - l + 1)
            r += 1

        return best
                
# zxyzxyz

# z
# {z --> 1}

# zx
# {z --> 1, x --> 1}

# zxy 
# {z --> 1, x --> 1, y --> 1}

# zxyz
# {z --> 2, x --> 1, y --> 1}
