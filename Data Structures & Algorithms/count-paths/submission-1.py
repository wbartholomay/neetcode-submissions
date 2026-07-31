class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]

        def dfs(row, col):
            if row == m -1 and col == n -1:
                return 1

            if grid[row][col] == 0:
                if row < m-1:
                    grid[row][col] += dfs(row + 1, col)
                if col < n-1:
                    grid[row][col] += dfs(row, col + 1)
                    
            return grid[row][col]

        return dfs(0, 0)