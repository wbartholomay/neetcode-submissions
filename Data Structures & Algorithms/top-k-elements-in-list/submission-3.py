class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in counts:
            count = counts[num]
            buckets[count].append(num)
        
        result = []
        for i in range(len(buckets) -1, -1, -1):
            bucket = buckets[i]
            if len(bucket) == 0:
                continue
            result.extend(bucket)
            if len(result) >= k:
                break
        return result