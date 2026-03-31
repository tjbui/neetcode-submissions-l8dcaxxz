class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for ind in range(0, len(nums)):
            needed = target - nums[ind]
            if needed in map:
                return [map[needed], ind]
            map[nums[ind]] = ind