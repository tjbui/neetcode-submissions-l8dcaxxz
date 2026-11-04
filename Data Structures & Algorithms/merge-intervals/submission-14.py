class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        if len(intervals) == 1:
            return [intervals[0]]

        intervals.sort()

        prevInterval = intervals[0]
        mergedIntervals = []
        for i in range(1, len(intervals)):
            currInterval = intervals[i]

            if currInterval[0] <= prevInterval[1]: # yes overlapping
                prevInterval = [prevInterval[0], max(currInterval[1], prevInterval[1])]

                # if last, need to append merged
                if i == len(intervals) - 1:
                    mergedIntervals.append(prevInterval)
            else: # not overlapping
                mergedIntervals.append(prevInterval)
                prevInterval = currInterval

                # if last, need to append currInterval
                if i == len(intervals) - 1:
                    mergedIntervals.append(currInterval)

        return mergedIntervals

        

# [[1,3], [1,5], [6,7]]

# [1,3], [1,5], [6,7]
# curr

# 