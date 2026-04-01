class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                new_intervals.append(newInterval)
                new_intervals += intervals[i:]
                return new_intervals
            elif newInterval[0] > intervals[i][1]:
                new_intervals.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), 
                               max(newInterval[1], intervals[i][1])]

        new_intervals.append(newInterval)
        return new_intervals