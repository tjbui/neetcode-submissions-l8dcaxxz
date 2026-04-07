"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_list, end_list = [], []
        for interval in intervals:
            start_list.append(interval.start)
            end_list.append(interval.end)
        start_list.sort()
        end_list.sort()

        s, e = 0, 0
        active, most_rooms = 0, 0
        while s < len(start_list):
            if start_list[s] < end_list[e]:
                active += 1
                s += 1
            else:
                active -= 1
                e += 1
            most_rooms = max(most_rooms, active)

        return most_rooms
            
        
        

# intervals = [(0, 40), (5, 10), (15, 20)]

#  0 --------------------------------------- 40              
#       5 ---- 10
#                   15 ---- 20

# Min heap to track end time

# 0, 5, 15      10, 20, 40
# s              e
# active = 1

# 0, 5, 15      10, 20, 40
#    s           e
# active = 2

# 0, 5, 15      10, 20, 40
#        s           e
# active = 1


