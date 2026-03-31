from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        best = s[:]

        window_map = defaultdict(int)
        t_map = defaultdict(int)

        for c in t:
            t_map[c] += 1
        
        exists_valid = 0
        while r < len(s):
            window_map[s[r]] += 1

            if self.checkWindow(t_map, window_map):
                exists_valid = 1

                while self.checkWindow(t_map, window_map):
                    if len(best) > r - l + 1:
                        best = s[l: r + 1]
                    window_map[s[l]] -= 1
                    l += 1
                    
            r += 1

        if exists_valid == 0:
            return ""

        return best

    def checkWindow(self, t_map: {}, window_map: {}):
        for key, value in t_map.items():
            if window_map[key] < t_map[key]:
                return False

        return True


        

# "OUZODYXAZV", "XYZ"
# t_map = {X --> 1, Y --> 1, Z --> 1}

# O         window_map = {O --> 1}
# OU        window_map = {O --> 1, U --> 1}
# OUZ
# OUZO
# OUZOD
# OUZODY
# OUZODYX   --> good shrink window
#   ZODYX   --> cur_best
#    ODYXA
#    ODYXAZ --> good shrink window
#      YXAZ
#       XAZV