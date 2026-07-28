class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        partition = []

        def dfs(i):
            if i >= len(s):
                result.append(partition.copy())
                return
            for j in range(i, len(s)):
                if self.is_palindrome(s, i, j):
                    partition.append(s[i:j+1])
                    dfs(j+1)
                    partition.pop()
        
        dfs(0)
        return result

    def is_palindrome(self, s, l, r) -> bool:
        while l < r:
            print(f"L: {l}    R: {r}    S:{s}")
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True