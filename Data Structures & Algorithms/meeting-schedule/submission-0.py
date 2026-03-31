"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key = lambda i: i.start)

        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i - 1].end > sorted_intervals[i].start:
                return False

        return True


# [(15,20), (0,30), (5,10)]
# [(0,30), (5,10), (15,20)] ---> sort by start time

# (0,30), (5,10) ---> Meeting 1 starts before Meeting 0 ends
#   0       1

# (5, 10), (15, 20) ---> Meeeting 2 starts before Meeting 1 ends
#    1        2