class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_list = sorted(nums)

        result_set = set()
        result_list = []
        for ind, target in enumerate(sorted_list):
            target *= -1
            l = ind + 1
            r = len(sorted_list) - 1

            while (l < r):
                if sorted_list[l] + sorted_list[r] > target:
                    r -= 1
                elif sorted_list[l] + sorted_list[r] < target:
                    l += 1
                else:
                    sorted_triplet = tuple(sorted([sorted_list[l], sorted_list[r], -target]))
                    if sorted_triplet not in result_set:
                        result_set.add(sorted_triplet)
                        result_list.append(list(sorted_triplet))
                    l += 1

        return result_list


# nums = [-1,0,1,2,-1,-4]
# sorted = [-4, -1, -1, 0, 1, 2]
#
# target = -4 --> 4
# [-1, -1, 0, 1, 2]
# 
# target = -1 --> 1
# [-1, 0, 1, 2]
