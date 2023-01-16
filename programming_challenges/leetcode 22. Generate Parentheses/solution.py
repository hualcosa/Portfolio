class Solution(object):
    def generateParenthesis(self, n):
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            # we have completed all posibilities
            if len(S) == 2 * n:
                ans.append("".join(S))
                return 
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop() # cleaning for no side effects during next backtrack calling
            if right < left:
                S.append(")")
                backtrack(S, left, right + 1)
                S.pop()
        backtrack()
        return ans
                
            
    