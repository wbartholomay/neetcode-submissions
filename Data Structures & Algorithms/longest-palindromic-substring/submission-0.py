class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            odd_result = self.findLongestPalindromeFromCenter(i, i, s)
            even_result = self.findLongestPalindromeFromCenter(i-1, i, s)
            if len(odd_result) > len(result):
                result = odd_result
            if len(even_result) > len(result):
                result = even_result
        return result
    
    def findLongestPalindromeFromCenter(self, l, r, s):
        if l < 0 or r >= len(s):
            return ""

        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                break
            l-=1
            r+=1

        return s[l+1: r]