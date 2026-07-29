class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        result = 0
        for _ in range(k):
            result = heapq.heappop_max(nums)
        return result