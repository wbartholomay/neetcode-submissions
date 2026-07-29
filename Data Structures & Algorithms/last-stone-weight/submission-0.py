class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)
            if stone1 == stone2:
                continue
            new_stone = stone1 - stone2
            heapq.heappush_max(stones, new_stone)
        
        if len(stones) == 0:
            return 0
        return stones[0]