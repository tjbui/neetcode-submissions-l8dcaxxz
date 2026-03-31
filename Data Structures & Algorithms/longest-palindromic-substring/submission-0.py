class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""


        for i in range(len(s)):
            l = i
            r = i

            # odd
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(result):
                    result = s[l:r+1]
                l -= 1
                r += 1

            # even
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(result):
                    result = s[l:r+1]
                l -= 1
                r += 1

        return result

        
        

# ababd  ---> odd number

# s[0] as center:
# a

# s[1] as center:
# aba

# s[2] as center:
# bab

# d[3] as center:
# d

# abbc ---> even number