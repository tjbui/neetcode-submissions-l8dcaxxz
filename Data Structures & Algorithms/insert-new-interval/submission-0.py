class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # case 1
                new_intervals.append(newInterval)
                return new_intervals + intervals[i:]
            elif intervals[i][1] < newInterval[0]: # case 2
                new_intervals.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), 
                               max(newInterval[1], intervals[i][1])]
        
        new_intervals.append(newInterval)
        return new_intervals

# case 1
# intervals = [[4, 6], [8, 10]], newInterval = [1, 3]
# [1, 3] ends before [4, 6] starts

# case 2
# intervals = [[4, 6], [9, 10]], newInterval = [7, 8]
# [4, 6] ends before [7, 8] starts

# case 3
# intervals = [[4, 6], [9, 10]], newInterval = [7, 9]
# newInterval = [7, 10]



# intervals = [[1, 3], [4, 6]], newInterval = [2, 5]
#
# [1, 3] ---> yes overlap 
# [4, 6] ---> yes overlap
# intervals[i-1].end >= intervals[i].start ---> overlapping
# 



# intervals = [[1, 2], [3, 5], [9, 10]], newInterval = [6, 7]

# [1, 2] ---> no overlap
# [3, 5] ---> no overlap
