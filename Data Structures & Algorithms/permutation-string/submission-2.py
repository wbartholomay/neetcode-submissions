class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts_1 = {}
        for i in range(len(s1)):
            curr_char = s1[i]
            counts_1[curr_char] = counts_1.get(curr_char, 0) + 1
        
        l = 0
        counts_2 = {}
        for r in range(len(s2)):
            curr_char = s2[r]
            counts_2[curr_char] = counts_2.get(curr_char, 0) + 1
            
            while counts_2[curr_char] > counts_1.get(curr_char, 0):
                counts_2[s2[l]] -= 1
                l += 1
            
            if (r - l + 1) == len(s1):
                return True
        return False