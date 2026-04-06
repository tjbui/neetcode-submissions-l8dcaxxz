class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        num_removed = 0
        prev_start, prev_finish = -50001, -50001
        for start, finish in intervals:
            if prev_finish > start:
                num_removed += 1

                if prev_finish > finish:
                    prev_start, prev_finish = start, finish
                else:
                    prev_start, prev_finish = prev_start, prev_finish
            else:
                prev_start, prev_finish = start, finish

        return num_removed

        

# [[1, 2], [2, 4], [1, 4]]

# [1, 2], [1, 4], [2, 4], 
# sort by start time

# 