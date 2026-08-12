class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        result = 0
        visited = set()
        heap = [(grid[0][0], (0,0))]
        while heap:
            value, pos = heapq.heappop(heap)
            if pos in visited:
                continue
            
            visited.add(pos)
            if value > result:
                result = value
            
            if pos[0] == ROWS - 1 and pos[1] == COLS - 1:
                return result
            
            for direction in directions:
                dest = (pos[0] + direction[0], pos[1] + direction[1])
                if dest[0] >= 0 and dest[0] < ROWS and dest[1] >= 0 and dest[1] < COLS and dest not in visited:
                    heapq.heappush(heap, (grid[dest[0]][dest[1]], dest))
         