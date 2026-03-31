from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        maxLen = 0
        maxFreq = 0
        frequencies = defaultdict(int)

        while right < len(s):
            frequencies[s[right]] += 1
            maxFreq = max(maxFreq, frequencies[s[right]])

            while ((right - left + 1) - maxFreq > k):
                frequencies[s[left]] -= 1
                left += 1

            maxLen = max(maxLen, right - left + 1)
            right += 1

        return maxLen