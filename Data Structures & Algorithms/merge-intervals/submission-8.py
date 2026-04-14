class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        if len(intervals) == 1:
            return [intervals[0]]

        intervals.sort()

        merged_intervals = []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            curr = intervals[i]

            if curr[0] <= prev[1]:
                prev = [min(prev[0], curr[0]), max(prev[1], curr[1])]
                if i == len(intervals) - 1:
                    merged_intervals.append(prev)
            else:
                merged_intervals.append(prev)
                prev = curr
                if i == len(intervals) - 1:
                    merged_intervals.append(curr)

        return merged_intervals
            

# 
# intervals = [[1, 3], [1, 5], [6, 7]]
# Output: [[1, 5], [6, 7]]

# if we sort based on start time, we know if the next start before prev ends,
# overlap

# [1, 3], [1, 5], [6, 8], [7, 10]
# [1, 5], [6, 10]

# prev = [1, 3]
# [1, 5] --> start before prev ends
# merge into [1, 5]

# prev = [1, 5]
# [6, 8]
# --> no overlap, append [1, 5] to merged