from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = defaultdict(int)
        for c in s1:
            s1Map[c] += 1
        
        s2Map = defaultdict(int)
        l, r = 0, 0
        while r < len(s2):
            s2Map[s2[r]] += 1

            if r - l + 1 > len(s1):
                s2Map[s2[l]] -= 1
                if s2Map[s2[l]] == 0:
                    del s2Map[s2[l]]
                l += 1

            if s1Map == s2Map:
                return True

            r += 1
        return False
            
        

# Input: s1 = "abc", s2 = "lecabee"
#
# l e c a b e e
# l   r

# l e c a b e e
#   l   r