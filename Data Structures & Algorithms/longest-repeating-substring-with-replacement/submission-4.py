class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        res = 0
        l = 0

        max_frequency = 0
        res = 0
        for r in range(len(s)):
            char = s[r]
            counts[char] = counts.get(char, 0) + 1
            max_frequency = max(max_frequency, counts[char])

            if (r - l + 1) - max_frequency > k:
                counts[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            
        return res