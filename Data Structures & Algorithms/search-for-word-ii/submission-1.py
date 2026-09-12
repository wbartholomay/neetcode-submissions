
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        cur_node = self.root
        for char in word:
            index = ord(char) - ord('a')
            child = cur_node.children[index]
            if child is not None:
                cur_node = child
            else:
                new_node = TrieNode()
                cur_node.children[index] = new_node
                cur_node = new_node
        cur_node.is_word = True
    
    def search(self, word: str) -> bool:
        cur_node = self.root
        for char in word:
            index = ord(char) - ord('a')
            child = cur_node.children[index]
            if child is None:
                return False
            cur_node = child
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))
        trie = Trie()
        for word in words:
            trie.insert(word)

        res = set()
        visited = set()

        def dfs(row: int, col: int, node: TrieNode, cur_path: str):
            if row < 0 or row > ROWS - 1 or col < 0 or col > COLS - 1 or (row, col) in visited:
                return

            visited.add((row, col))
            char = board[row][col]
            index = ord(char) - ord('a')

            child_node = node.children[index]

            if child_node is None:
                visited.remove((row, col))
                return
            
            cur_path += char
            if child_node.is_word:
                res.add(cur_path)

            for direction in DIRECTIONS:
                dfs(row + direction[0], col + direction[1], child_node, cur_path)
            
            visited.remove((row, col))
            return
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root, "")

        return list(res)

