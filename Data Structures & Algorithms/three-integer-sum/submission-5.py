class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        without_ind = [] # list of lists
        nums.sort()
        for i in range(0, len(nums)): # O(n^2)
            new_list = list(nums)
            del new_list[i]
            without_ind.append(new_list)

        print(without_ind)

        s = set()

        result = []
        for ind, num in enumerate(nums):
            target = -num
            without_li = without_ind[ind]

            l = 0
            r = len(nums) - 2
            while l < r:
                if without_li[l] + without_li[r] < target:
                    l += 1
                elif without_li[l] + without_li[r] > target:
                    r -= 1
                else:
                    trip = [num, without_li[l], without_li[r]]
                    trip.sort()
                    if tuple(trip) not in s:
                        s.add(tuple(trip))
                        result.append(tuple(trip))
                    l += 1
                    r -= 1

        return result
            