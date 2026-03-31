class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strOneLen = len(strs[0])
        numStrs = len(strs)

        pref = ""
        breakFlag = 0
        for i in range(0, strOneLen):
            curr = strs[0][i]
            for s in strs:
                if len(s) <= i:
                    breakFlag = 1
                    break
                if s[i] != curr:
                    breakFlag = 1
                    break
            if breakFlag:
                break
            pref += strs[0][i]

        return pref

            
