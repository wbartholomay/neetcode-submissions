class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total_bananas = 0
        queue = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                if grid[row][col] != 0:
                    total_bananas += 1
        
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        max_time = 0
        bananas_visited = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            row, col, time = queue.popleft()
            if visited[row][col]:
                continue
            visited[row][col] = True
            bananas_visited += 1
            max_time = max(max_time, time)

            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])) or visited[new_row][new_col] or grid[new_row][new_col] == 0:
                    continue
                queue.append((new_row, new_col, time + 1))
        
        if bananas_visited == total_bananas:
            return max_time
        else:
            return -1