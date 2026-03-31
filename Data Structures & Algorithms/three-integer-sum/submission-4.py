class Solution:
    def twoSum(self, nums: List[int], target: int, skipInd: int) -> List[tuple]:
        li = []
        s = set()
        for ind in range(0, len(nums)):
            if ind == skipInd:
                continue

            needed = target - nums[ind]
            if needed in s:
                li.append([needed, nums[ind]])
            s.add(nums[ind])

        if not li:
            return None
        return li

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set()

        for ind, num in enumerate(nums):
            li = self.twoSum(nums, -num, ind)
            if li is None:
                continue

            for tup in li:
                tup.append(num)
                tup.sort()
                if tuple(tup) not in s:
                    s.add(tuple(tup))

        return list(s)
