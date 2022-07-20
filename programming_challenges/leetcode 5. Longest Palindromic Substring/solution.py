class Solution:
    def expandAroundCenter(self, s:str, L:int, R:int) -> int:
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        
        return R - L - 1
    
    def longestPalindrome(self, s: str) -> str:
        if s is None or len(s) < 1: return ""
    
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s,i,i)
            len2 = self.expandAroundCenter(s, i, i+1)
            len_ = max(len1, len2)
            if len_ > end - start:
                start = i - (len_ - 1)//2
                end = i + len_//2
                
        return s[start:end+1]
            