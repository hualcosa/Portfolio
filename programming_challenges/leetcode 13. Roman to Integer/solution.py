class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        i = 0
        convertion_table = {'I': 1,
                            'V': 5,
                            'X': 10,
                            'L': 50,
                            'C': 100,
                            'D': 500,
                            'M': 1000}
        
        # dealing with edge cases:
        if len(s) == 1:
            return convertion_table[s]
        
        while i < len(s):
            # if we don't fall in one of the six cases where 
            # we have to subtract the numbers, we simply add it to the result
            if i == len(s) - 1:
                result += convertion_table[s[i]]
                i += 1
            elif s[i] == 'I' and s[i+1] == 'V':
                result += 4
                i += 2
            elif s[i] == 'I' and s[i+1] == 'X':
                result += 9
                i += 2
            elif s[i] == 'X' and s[i+1] == 'L':
                result += 40
                i += 2
            elif s[i] == 'X' and s[i+1] == 'C':
                result += 90
                i += 2
            elif s[i] == 'C' and s[i+1] == 'D':
                result += 400
                i += 2
            elif s[i] == 'C' and s[i+1] == 'M':
                result += 900
                i += 2
            else:
                result += convertion_table[s[i]]
                i += 1
                
        return result
        