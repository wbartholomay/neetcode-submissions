class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i, interval in enumerate(intervals):
            if interval[0] > newInterval[1]:
                result.append(newInterval)
                return result + intervals[i:]
            elif interval[1] < newInterval[0]:
                result.append(interval)
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        result.append(newInterval)
        return result
            