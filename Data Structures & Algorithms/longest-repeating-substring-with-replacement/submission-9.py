from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        l, r = 0, 0
        maxFreq = 0
        best = 0

        while r < len(s):
            counts[s[r]] += 1
            maxFreq = max(counts[s[r]], maxFreq)

            while (r - l + 1 - maxFreq) > k:
                counts[s[l]] -= 1
                l += 1

            best = max(best, r - l + 1)
            r += 1

        return best


# "AAABABB", k = 2

# A         --> maxFreq = 1
# AA        --> maxFreq = 2
# AAA       --> maxFreq = 3
# AAAB      --> maxFreq = 3
# AAABA     --> maxFreq = 4
# AAABAB    --> maxFreq = 4
# AAABABB   --> maxFreq = 4 
#               --> window length - maxFreq > k 
#  AABABB   --> maxFreq = 4 (invalid but its okay 
#                            since we can't grow 
#                            window unless valid)
# return best