class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        res = 0

        l = 0
        max_frequency = 0
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            max_frequency = max(max_frequency, counts[s[r]])

            # shift left of window if window has broken condition

            while (r - l + 1) - max_frequency > k:
                counts[s[l]] -= 1
                l += 1
            
            res = max(r - l + 1, res)
        
        return res