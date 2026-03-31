class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sortedNums = self.mergeSort(nums)

        for i in range(len(nums)):
            nums[i] = sortedNums[i]
        

    def mergeSort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        lArr = nums[0: len(nums) // 2]
        rArr = nums[len(nums) // 2: len(nums)]

        lArr = self.mergeSort(lArr)
        rArr = self.mergeSort(rArr)

        return self.merge(lArr, rArr)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        lPtr = 0
        rPtr = 0

        res = []
        while lPtr < len(left) and rPtr < len(right):
            if left[lPtr] < right[rPtr]:
                res.append(left[lPtr])
                lPtr += 1
            else:
                res.append(right[rPtr])
                rPtr += 1

        while lPtr < len(left):
            res.append(left[lPtr])
            lPtr += 1

        while rPtr < len(right):
            res.append(right[rPtr])
            rPtr += 1

        return res
