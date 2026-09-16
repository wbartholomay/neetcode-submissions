class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()

        l = 0

        res = []

        for r in range(len(nums)):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            
            queue.append(r)

            if r - l + 1 < k:
                continue

            if queue[0] < l:
                queue.popleft()

            res.append(nums[queue[0]])
            l += 1
        
        return res