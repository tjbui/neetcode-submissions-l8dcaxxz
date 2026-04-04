class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, total, current_combination):
            if total == target:
                result.append(current_combination)
                return
            if i >= len(nums) or total > target:
                return

            dfs(i + 1, total, current_combination)

            added = list(current_combination)
            added.append(nums[i])
            dfs(i, total + nums[i], added)
            return

        dfs(0, 0, [])
        return result

#             2                     []
#      2,2           2           3      []
# 2,2,2   2,2   2,3     2
#                    2,4