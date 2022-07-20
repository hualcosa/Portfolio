class Solution:
    import sys
    def isCommonPrefix(self, strs, size):
        str1 = strs[0][0:size]
        for i in range(1, len(strs)):
            if not strs[i].startswith(str1):
                return False
        return True
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if (strs is None) or (len(strs) == 0):
            return ""
        minLen = 200 # using constraint adopted by the problem
        
        for s in strs:
            minLen = min(minLen, len(s))
        
        low = 1
        high = minLen
        while low <= high:
            middle = (low + high) // 2
            if self.isCommonPrefix(strs, middle):
                low = middle + 1
            else:
                high = middle - 1
        middle = (low + high) // 2
        return strs[0][0:middle]
    