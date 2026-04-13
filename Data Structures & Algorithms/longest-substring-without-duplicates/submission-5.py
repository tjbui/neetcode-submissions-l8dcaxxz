class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()

        l, r = 0, 0
        best = 0
        while r < len(s):
            while s[r] in characters:
                characters.remove(s[l])
                l += 1

            characters.add(s[r])

            best = max(best, r - l + 1)
            r += 1

        return best
        
# s = "zxyzxyz"

# Sliding window
# zxyzxyz s = {z}
# l
# r
# 

# zxyzxyz s = {z, x}
# l
#  r

# zxyzxyz s = {z, x, y}
# l
#   r

# zxyzxyz
#  l
#    r