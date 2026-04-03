class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)

        wordSet = set(wordDict)

        dp[0] = True
        for i in range(1, len(s) + 1):
            currS = s[0:i]
            for word in wordDict:
                if ((currS[len(currS) - len(word): len(currS)] in wordSet) and
                    (dp[len(currS) - len(word)])):
                    dp[i] = True

        return dp[len(s)]
        

# s = "catsincars", wordDict = ["cats","cat","sin","in","car"]

# c       ---> False
# ca      ---> False
# cat     ---> True
# cats    ---> True
# catsi   ---> False
# catsin  ---> in good, cats good.
#         ---> for word in wordDict:
#         ---> check if s[len(s) - len(word): len(s)] is in dict
#         --->   and if s[0: len(s) - len(word)]