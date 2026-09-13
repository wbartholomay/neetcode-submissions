class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts_t = {}
        for char in t:
            counts_t[char] = counts_t.get(char, 0) + 1

        l = 0

        res_l = 0
        res_r = float('inf')

        have, need = 0, len(counts_t)
        counts_s = {}
        for r in range(len(s)):
            char = s[r]
            counts_s[char] = counts_s.get(char, 0) + 1
            if char in counts_t and counts_t[char] == counts_s[char]:
                have += 1

            while have == need and l <= r:
                if (r - l + 1) < (res_r - res_l + 1):
                    res_l = l
                    res_r = r

                counts_s[s[l]] -= 1
                if s[l] in counts_t and counts_t[s[l]] > counts_s[s[l]]:
                    have -= 1
                l += 1

        if res_r == float('inf'):
            return ""
        
        return s[res_l:res_r+1]
