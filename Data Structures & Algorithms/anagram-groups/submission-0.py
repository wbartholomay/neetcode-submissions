class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            chars = [0 for _ in range(26)]
            for char in s:
                chars[ord(char) - ord('a')] += 1
            key = tuple(chars)
            anagrams.setdefault(key, []).append(s)
        return list(anagrams.values())