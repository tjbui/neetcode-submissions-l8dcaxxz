class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k >= len(arr):
            return arr

        l, r = 0, len(arr) - 1
        while l < r:
            m = (l + r) // 2

            if x == arr[m]:
                l, r = m, m
            elif x < arr[m]:
                r = m
            else:
                l = m + 1

        p1, p2 = l - 1, l
        while p2 - p1 - 1 < k:
            if p1 < 0:
                p2 = k
                break
            if p2 >= len(arr):
                p1 = len(arr) - k - 1
                break
            
            dist_1 = abs(x - arr[p1])
            dist_2 = abs(x - arr[p2])

            if dist_1 < dist_2:
                p1 -= 1
            elif dist_2 < dist_1:
                p2 += 1
            else:
                if arr[p1] < arr[p2]:
                    p1 -= 1
                else:
                    p2 += 1

        return arr[p1 + 1: p2]


        

            

        

# arr = [2,4,5,8], k = 2, x = 6
# out = [4, 5]

# [2, 4,    , 5, 8] ---> binary search logn
#         6
# ind = 2

# [2, 4, 5, 8]
#  l        r

# [2, 4, 5, 8]
#  l  m     r   --> 4 < 6

# [2, 4, 5, 8]
#        l 
#        m
#        r

# 2, 5, 8, 9, 10  --> search for 3, idx = 1
# l           r

# 2, 5, 8, 9, 10  --> search for 3, idx = 1
# l     m     r

# 2, 5, 8, 9, 10  --> search for 3, idx = 1
# l  m  r

# 2, 5, 8, 9, 10  --> search for 3, idx = 1
# l   
# m  r

# 2, 5, 8, 9, 10  --> search for 3, idx = 1
#    l   
#    r