class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new = []
        count = 0
        for num in nums:
            if num != val:
                new.append(num)
                count += 1

        for i in range(0, count):
            nums[i] = new[i]

        # nums = new # doesn't work

        return count