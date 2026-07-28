class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for y in range(len(board)):
            for x in range(len(board[y])):
                char = board[y][x]
                if char == word[0]:
                    if self.func(board, word[1:], {(x, y)}, (x, y)):
                        return True
        return False
        
    def func(self, board: List[List[str]], word: str, visited: Set[Tuple[int]], cur_pos: [Tuple[int]]) -> bool:
        if word == "":
            return True

        left_pos = (cur_pos[0] - 1, cur_pos[1])
        right_pos = (cur_pos[0] + 1, cur_pos[1])
        up_pos = (cur_pos[0], cur_pos[1] - 1)
        down_pos = (cur_pos[0], cur_pos[1] + 1)
        positions = (left_pos, right_pos, up_pos, down_pos)
        for position in positions:
            if (self.check_position(board, word, visited, position)):
                return True
        
        return False

    def check_position(self, board, word, visited, position) -> bool:
        if position[0] >= 0 and position[0] < len(board[0]) and position[1] >= 0 and position[1] < len(board):
            if position not in visited and board[position[1]][position[0]] == word[0]:
                visited.add(position)
                res = self.func(board, word[1:], visited, position)
                visited.remove(position)
                return res
        return False