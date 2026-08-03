class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}

        def helper(i1, i2):
            if i1 == len(text1) or i2 == len(text2):
                return 0

            if cache.get((i1, i2)) is None:
                if text1[i1] == text2[i2]:
                    cache[(i1, i2)] =  1 + helper(i1 + 1, i2 + 1)
                else:
                    cache[(i1, i2)] = max(helper(i1 + 1, i2), helper(i1, i2 + 1))
            
            return cache[(i1, i2)]
        
        return helper(0, 0)