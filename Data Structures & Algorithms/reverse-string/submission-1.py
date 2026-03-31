class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1

        while l < r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp

            l += 1
            r -= 1
            
        
# 
# "hello"
# h e l l o
# l       r

# o e l l h
#   l   r  

# o l l e h
#     l   
#     r