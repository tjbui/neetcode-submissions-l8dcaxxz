class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []

        def dfs(i, total, current_comb):
            if total == target:
                ret.append(current_comb)
                return
            if i > len(nums) - 1 or total > target:
                return

            added = list(current_comb)
            added.append(nums[i])
            dfs(i, total + nums[i], added)

            dfs(i + 1, total, current_comb)


        dfs(0, 0, [])
        return ret



# [2, 5, 6, 9], target = 9
# [2, 2, 5], [9]

# [2, 5, 6, 9]
#  i
# Any combo of 2, 5, 6, 9
#                             [2]
#           [2, 2]                          [2, 3]
# [2, 2, 2]         [2, 2, 3]     [2, 3, 3]        [2, 3, 4]



# [2, 5, 6, 9]
#     i
# Any combo of 5, 6, 9