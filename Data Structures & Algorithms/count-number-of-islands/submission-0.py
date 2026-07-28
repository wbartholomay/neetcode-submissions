class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0

        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or grid[row][col] == "0":
                return
            
            grid[row][col] = "0"
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    result += 1



        return result