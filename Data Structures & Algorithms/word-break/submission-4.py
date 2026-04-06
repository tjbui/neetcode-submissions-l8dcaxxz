class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            #substr = s[0: i]

            for word in wordDict:
                if (s[0: i][len(s[0: i]) - len(word): len(s[0: i])] == word and
                   dp[len(s[0: i]) - len(word)] == True):
                   dp[i] = True

        return dp[len(s)]
        

# s = "catsincars", wordDict = ["cats","cat","sin","in","car"]
# 
# "c" --> no match          dp[1]
# "ca" --> no match         dp[2]
# "cat" --> yes match       dp[3]
# "cats" --> yes match
# "catsi" -->  no match

# "catsin" --> yes match    dp[6]