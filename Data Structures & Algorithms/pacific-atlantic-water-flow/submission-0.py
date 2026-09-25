class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        atlantic_queue = deque()
        atlantic_visited = [[False] * cols for _ in range(rows)]
        pacific_queue = deque()
        pacific_visited = [[False] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if row == 0 or col == 0:
                    pacific_queue.append([row, col])
                if row == rows - 1 or col == cols - 1:
                    atlantic_queue.append([row, col])
        
        while atlantic_queue:
            row, col = atlantic_queue.popleft()
            if atlantic_visited[row][col]:
                continue
            atlantic_visited[row][col] = True
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if not(0 <= new_row < rows and 0 <= new_col < cols) or atlantic_visited[new_row][new_col] or heights[new_row][new_col] < heights[row][col]:
                    continue
                atlantic_queue.append([new_row, new_col])
            
        
        while pacific_queue:
            row, col = pacific_queue.popleft()
            if pacific_visited[row][col]:
                continue
            pacific_visited[row][col] = True
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if not(0 <= new_row < rows and 0 <= new_col < cols) or pacific_visited[new_row][new_col] or heights[new_row][new_col] < heights[row][col]:
                    continue
                pacific_queue.append([new_row, new_col])
        
        res = []
        print(atlantic_visited)
        print(pacific_visited)
        for row in range(rows):
            for col in range(cols):
                if atlantic_visited[row][col] and pacific_visited[row][col]:
                    res.append([row, col])
        return res