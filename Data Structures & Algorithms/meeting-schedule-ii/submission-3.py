"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
    
        intervals.sort(key=lambda interval: interval.start)
        end_time_heap = [intervals[0].end]
        for interval in intervals[1:]:
            earliest_end_time = end_time_heap[0]
            if earliest_end_time > interval.start:
                heapq.heappush(end_time_heap, interval.end)
            elif earliest_end_time < interval.end:
                heapq.heappop(end_time_heap)
                heapq.heappush(end_time_heap, interval.end)

        return len(end_time_heap)