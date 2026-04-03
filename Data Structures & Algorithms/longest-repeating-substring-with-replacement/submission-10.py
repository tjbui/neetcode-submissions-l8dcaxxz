from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        l = 0
        r = 0
        best = 0

        while r < len(s):
            counts[s[r]] += 1

            maxFreq = 0
            for key, val in counts.items():
                maxFreq = max(maxFreq, val)

            while (r - l + 1 - maxFreq) > k:
                counts[s[l]] -= 1
                l += 1

            best = max(best, r - l + 1)
            r += 1

        return best


# "A A A B A B B", k = 1
#        l r