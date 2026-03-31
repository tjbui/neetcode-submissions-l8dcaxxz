class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        for i in nums:
            if i != 0:
                prod *= i
            else:
                zero_count += 1
                
        if zero_count > 1:
            return [0] * len(nums)

        out = []
        if zero_count == 0:
            for i in nums:
                out.append(int(prod / i))
        else:
            for i in nums:
                if i != 0:
                    out.append(0)
                else:
                    out.append(int(prod))

        return out