class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new_intervals = []

        intervals.sort()

        for i in range(1, len(intervals) + 1):
            if i == len(intervals):
                new_intervals.append(intervals[i - 1])
                break

            if intervals[i][0] <= intervals[i - 1][1]:
                intervals[i] = [min(intervals[i][0], intervals[i - 1][0]), 
                                max(intervals[i][1], intervals[i - 1][1])]
            else:
                new_intervals.append(intervals[i - 1])

        return new_intervals            

# [[1, 3], [1, 5], [6,7]] ---> [[1, 5], [6, 7]]
#  i - 1     i
#
# if not overlapping: just append i - 1
# if they are overlapping: intervals[i] = COMBINE(i, i - 1)
#
# [[1, 5], [6, 7]]
#  i - 1     i
# append i - 1

# [[6, 7],   ]
#  i - 1    i