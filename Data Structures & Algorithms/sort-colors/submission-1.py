class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3

        for num in nums:
            counts[num] += 1

        numsInd = 0
        for countsInd, count in enumerate(counts):
            for j in range(count):
                nums[numsInd] = countsInd
                numsInd += 1


