class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        result = []

        def dfs(row):
            if row == n:
                print(board)
                result.append(["".join(r) for r in board])
                return
            
            for col in range(n):
                if self.check_board(board, row, col):
                    board[row][col] = "Q"
                    dfs(row + 1)
                    board[row][col] = "."
        dfs(0)
        for board in result:
            for i, _ in enumerate(board):
                board[i] = str(board[i])
        print(result)
        return result


    def check_board(self, board, current_row, current_col) -> bool:
        for row in range(0, current_row):
            distance = current_row - row
            has_left_diag_conflict = current_col - distance >= 0 and board[row][current_col - distance] == "Q"
            has_right_diag_conflict = current_col + distance < len(board[row]) and board[row][current_col + distance] == "Q"
            if has_left_diag_conflict or has_right_diag_conflict or board[row][current_col] == "Q":
                return False
        return True