class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLUMNS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647

        def bfs(row, col):
            queue = deque([(row, col)])
            visited = {(row, col)}

            steps = 0

            while queue:
                steps += 1
                for _ in range(len(queue)):
                    pos = queue.popleft()
                    for direction in directions:
                        new_pos = (pos[0] + direction[0],pos[1]+ direction[1])
                        if new_pos in visited or new_pos[0] < 0 or new_pos[0] >= ROWS or new_pos[1] < 0 or new_pos[1] >= COLUMNS:
                            continue
                        val = grid[new_pos[0]][new_pos[1]]
                        print(f"New Position: {new_pos}    Val: {val}")
                        if val == -1 or val == 0 or val < steps:
                            continue
                        
                        print(new_pos)
                        visited.add(new_pos)
                        grid[new_pos[0]][new_pos[1]] = steps
                        queue.append(new_pos)
            
        for row in range(ROWS):
            for col in range(COLUMNS):
                if grid[row][col] == 0:
                    bfs(row, col)