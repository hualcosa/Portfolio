class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # initialize the dp array
        dp = [False] * (len(s) + 1)
        # set the n+1 position = True
        dp[len(s)] = True
        
        # Go build the decision tree from end until index 0
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # if index position plus word's length <= string size
                # and the range correspond to a matching word...
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        # the answer will be stored in dp[0]
        return dp[0]