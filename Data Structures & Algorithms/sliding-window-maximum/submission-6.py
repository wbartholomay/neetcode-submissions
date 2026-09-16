class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []

        l = 0

        res = []

        for r in range(len(nums)):
            heapq.heappush_max(heap, (nums[r], r))

            if r - l + 1 < k:
                continue
            
            while not l <= heap[0][1] <= r:
                heapq.heappop_max(heap)
            
            res.append(heap[0][0])
            l += 1
        
        return res