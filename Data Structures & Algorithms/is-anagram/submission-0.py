from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = defaultdict(int)
        for c in s:
            mapS[c] = mapS[c] + 1

        mapT = defaultdict(int)
        for c in t:
            mapT[c] = mapT[c] + 1

        return mapT == mapS