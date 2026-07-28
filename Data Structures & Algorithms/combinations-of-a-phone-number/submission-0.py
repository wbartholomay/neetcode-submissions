class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {"2" : ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
                      "5" : ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
                      "8" : ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

        result = []

        def dfs(index, cur):
            if len(cur) == len(digits):
                if len(cur) > 0:
                    result.append(cur)
                return
            
            letters = letter_map[digits[index]]
            for letter in letters:
                new_cur = cur + letter
                dfs(index + 1, new_cur)
        
        dfs(0, "")
        return result
        