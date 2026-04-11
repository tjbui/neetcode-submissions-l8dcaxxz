class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        for i in range(0, len(s)):
            l, r = i, i

            while l >= 0 and r <= len(s) - 1:
                if s[l] == s[r]:
                    total += 1
                    l -= 1
                    r += 1
                else:
                    break

        for i in range(0, len(s)):
            l, r = i, i + 1

            while l >= 0 and r <= len(s) - 1:
                if s[l] == s[r]:
                    total += 1
                    l -= 1
                    r += 1
                else:
                    break

        return total



        

# "aaa"

# "aaa"
#  i
# "a", "aa", "aaa"

# "aaa"
#   i
# "a", "aa"

# "aaa"
#    i
# "a"

# check palindrome on any string is O(n) --> 2 pointers
# running on every substring will be O(n^3)