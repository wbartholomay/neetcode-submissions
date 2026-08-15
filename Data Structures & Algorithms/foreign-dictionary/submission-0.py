class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        edges = {c: set() for w in words for c in w}
        for i in range(len(words) - 1):
            word_1 = words[i]
            word_2 = words[i+1]
            for j in range((len(word_1))):
                if j >= len(word_2):
                    return ""

                if word_1[j] != word_2[j]:
                    edges[word_1[j]].add(word_2[j])
                    break

        print(edges)
        visited = {}
        res = []
        def dfs(char):
            if char in visited:
                return visited[char]
            
            visited[char] = True
            for neighbor in edges[char]:
                if dfs(neighbor):
                    return True
                
            visited[char] = False
            res.append(char)
        
        for char in edges:
            if (dfs(char)):
                # cycle detected
                return ""

        res.reverse()
        return "".join(res)

