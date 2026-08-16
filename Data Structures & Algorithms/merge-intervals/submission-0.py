class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        for i, interval in enumerate(intervals):
            if len(result) == 0:
                result.append(interval)
                continue
            
            if result[-1][1] >= interval[0]:
                result[-1][1] = max(result[-1][1], interval[1])
                continue
            
            result.append(interval)
        
        return result