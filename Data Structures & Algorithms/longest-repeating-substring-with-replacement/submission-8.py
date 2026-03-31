from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        l = 0
        r = 0

        best = 0
        max_freq = 0
        while r < len(s):
            counts[s[r]] += 1

            max_freq = max(max_freq, counts[s[r]])
            other_count = r - l + 1 - max_freq

            while other_count > k:
                other_count -= 1 # not necessarily but generous
                counts[s[l]] -= 1
                l += 1

            best = max(best, r - l + 1)
            r += 1

        return best

# BAAA, k = 0

# B                     {B --> 1}
# BA  --> maxFreq = 1   {B --> 1, A --> 1}
#  A                    {A --> 1}
#  AA
#  AAA


# ABCDE, k = 1

# A    
# AB    maxFreq = 1
# ABC   maxFreq = 1  --> l - r + 1 - k > maxFreq

# AAABABB, k = 1

# A         {A --> 1}
# AA        {A --> 2}
# AAA       {A --> 3}
# AAAB      {A --> 3, B --> 1}
# AAABA     {A --> 4, B --> 1}
# AAABAB    {A --> 4, B --> 2}
#    BAB    {A --> 1, B --> 2}
#    BABB   {A --> 1, B --> 3}


# ABCDE, k = 1

# A
# AB
# ABC