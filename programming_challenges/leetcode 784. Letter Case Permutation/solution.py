class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def backtrack(sub="", i=0):
            if len(sub) == len(S):
                res.append(sub)
            else:
                if S[i].isalpha():
                    backtrack(sub + S[i].swapcase(), i+1)
                backtrack(sub + S[i], i + 1)
            
        res = []
        backtrack()
        return res
        
