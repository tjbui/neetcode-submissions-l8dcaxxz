class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        new_intervals = []

        prev_start, prev_end = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            new_start = intervals[i][0]
            new_end = intervals[i][1]

            if new_start <= prev_end:
                prev_start = min(new_start, prev_start)
                prev_end = max(new_end, prev_end)
            else:
                new_intervals.append([prev_start, prev_end])
                prev_start, prev_end = new_start, new_end

        new_intervals.append([prev_start, prev_end])

        return new_intervals
        

# intervals = [[1, 3], [1, 5], [6, 7]]

# sort by start time --> if next ends before prev starts: merge

# 