import heapq

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)

        minHeap = []
        maxRooms = 0
        for interval in intervals:
            while minHeap and interval.start >= minHeap[0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, interval.end)
            maxRooms = max(maxRooms, len(minHeap))

        return maxRooms
            
            
            



