class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(i):
            if i == len(nums) - 1:
                return [[nums[i]]]

            perms = backtrack(i + 1)

            new_perms = []
            for arr in perms:
                for ind in range(len(arr) + 1):
                    temp = list(arr)
                    temp.insert(ind, nums[i])
                    new_perms.append(temp)
            return new_perms

        return backtrack(0)