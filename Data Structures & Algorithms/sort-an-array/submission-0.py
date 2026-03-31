class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        left = self.sortArray(nums[0:len(nums) // 2])
        right = self.sortArray(nums[len(nums) // 2: len(nums)])
        
        return self.merge(left, right)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        lptr = 0
        rptr = 0

        merged = []
        while lptr < len(left) and rptr < len(right):
            if left[lptr] < right[rptr]:
                merged.append(left[lptr])
                lptr += 1
            else:
                merged.append(right[rptr])
                rptr += 1

        while rptr < len(right):
            merged.append(right[rptr])
            rptr += 1

        while lptr < len(left):
            merged.append(left[lptr])
            lptr += 1

        return merged