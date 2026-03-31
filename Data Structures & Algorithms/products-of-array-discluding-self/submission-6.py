class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = []
        curr = 1
        before.append(curr)
        for i in range(1, len(nums)):
            curr *= nums[i - 1]
            before.append(curr)

        after = [0] * len(nums)
        curr = 1
        after[len(nums) - 1] = curr
        for i in range(len(nums) - 2, -1, -1):
            curr *= nums[i + 1]
            after[i] = curr

        ret = []
        for i in range(len(nums)):
            ret.append(before[i] * after[i])

        return ret


# [1,2,4,6]
# before: [1, 1, 2, 8]
# after:  [48, 24, 6, 1]

# [-1,0,1,2,3]
# before: [1, -1, 0, 0, 0]
# after:  [0,  6, 6, 3, 1]