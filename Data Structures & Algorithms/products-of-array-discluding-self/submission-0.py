class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        has_zero = 0
        has_two_zeros = 0
        for i in nums:
            if i != 0:
                prod *= i
            else:
                if has_zero == 1:
                    has_two_zeros = 1
                has_zero = 1
                
        if has_two_zeros:
            return [0] * len(nums)

        out = []
        if not has_zero:
            for i in nums:
                out.append(int(prod / i))
        else:
            for i in nums:
                if i != 0:
                    out.append(0)
                else:
                    out.append(int(prod))

        return out