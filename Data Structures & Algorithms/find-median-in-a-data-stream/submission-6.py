import heapq

class MedianFinder:

    def __init__(self):
        self.minHeap = [] # heapq is minHeap by default
        self.maxHeap = [] # push negative values for maxHeap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, num)

        if self.minHeap and self.maxHeap:
            if -self.maxHeap[0] > self.minHeap[0]:
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

        if len(self.minHeap) > len(self.maxHeap) + 1:
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

        if len(self.maxHeap) > len(self.minHeap) + 1:
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + (-self.maxHeap[0])) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return -self.maxHeap[0]
        
# .add(3), .add(2), .add(7), .add(4)
# 
# maxHeap         minHeap
#   [3]             []
#
#   [3, 2]          []        ---> len(maxHeap) > len(minHeap) + 1
#   [2]             [3]            move 3 to minheap
#
#   [2, 7]          [3]       ---> peak(maxHeap) > peak(minHeap)
#   [2]             [3, 7]         move 7 to minheap
#
#   [2, 4]          [3, 7]    ---> peak(maxHeap) > peak(minHeap)
#   [2]             [3, 4, 7] ---> len(minHeap) > len(maxHeap + 1)
#   [2, 3]          [4, 7]