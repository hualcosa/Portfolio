class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        ##calls will only ever be made to match(text[i:], pattern[j:]), we use \text{dp(i, j)}dp(i, j) to handle those calls instead, saving us expensive string-building operations and allowing us to cache the intermediate results.
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j+1 < len(p) and p[j+1] == "*":
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)
                        
                memo[i, j] = ans
                print(f'{s[i:]} ---- {p[j:]}: {ans}')  
            return memo[i, j]
        return dp(0,0)
        