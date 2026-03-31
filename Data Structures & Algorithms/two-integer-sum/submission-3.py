class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict()

        for ind in range(0, len(nums)):
            needed = target - nums[ind]

            if needed in m:
                return [m[needed], ind]
            
            m[nums[ind]] = ind

        return [0, 0]