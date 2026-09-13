class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        heap = []

        for i in range(l, k - 1):
            heapq.heappush_max(heap, (nums[i], i))
        
        for r in range(k - 1, len(nums)):
            heapq.heappush_max(heap, (nums[r], r))
            while l > heap[0][1] or heap[0][1] > r:
                heapq.heappop_max(heap)
            res.append(heap[0][0])
            l += 1
        
        return res