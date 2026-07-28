class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = dict()
        for num in nums:
            if num not in frequencies:
                frequencies[num] = 0
            frequencies[num] += 1
        buckets = [[] for _ in range(len(nums))]
        for num, frequency in frequencies.items():
            buckets[frequency - 1].append(num)
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
