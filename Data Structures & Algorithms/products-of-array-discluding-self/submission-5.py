class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        num_zeros = 0
        for i in nums:
            if i == 0:
                num_zeros += 1
                continue
            prod *= i

        if num_zeros > 1:
            return [0] * len(nums)

        if num_zeros == 1:
            ret = []
            for i in nums:
                if i == 0:
                    ret.append(prod)
                else:
                    ret.append(0)
            return ret

        ret = []
        for i in nums:
            ret.append(int(prod / i))

        return ret
        

#
# [1,2,4,6]
# prod = 1 * 2 * 4 * 6 = 48
# [48 / 1, 48 / 2, 48 / 4, 46 / 6]
# [48, 24, 12, 8]

# 2+ zeros: [0, 0, ...]

# 1 zero: [-1,0,1,2,3]
# [0,-6,0,0,0]
