class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_index = len(intervals)
        for i, interval in enumerate(intervals):
            if interval[0] > newInterval[0]:
                new_index = i
                break
        intervals.insert(new_index, newInterval)
        result = []
        for interval in intervals:
            if len(result) > 0 and result[-1][1] >= interval[0]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        return result