from typing import List, Tuple

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = [[False] * cols for _ in range(rows)]

        regions = []

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'X' or visited[row][col]:
                    continue
                region = []
                visited[row][col] = True
                stack = [(row, col)]
                while stack:
                    r, c = stack.pop()
                    region.append((r, c))
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (0 <= nr < rows and 0 <= nc < cols
                                and not visited[nr][nc]
                                and board[nr][nc] == 'O'):
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                regions.append(region)

        for region in regions:
            for position in region:
                if position[0] == 0 or position[1] == 0 or position[0] == rows - 1 or position[1] == cols - 1:
                    break
            else:
                for position in region:
                    board[position[0]][position[1]] = 'X'