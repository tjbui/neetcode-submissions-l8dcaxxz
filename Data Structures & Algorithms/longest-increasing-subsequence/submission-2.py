class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        opt = [1] * len(nums)
        opt[0] = 1
        for i in range(1, len(nums)):
            choose_i = 1
            for j in range(0, i):
                if nums[j] < nums[i]:
                    choose_i = max(choose_i, 1 + opt[j])

            opt[i] = choose_i
            print(i, opt[i])

        return max(opt)