class Solution:
    def dfs(self, words, memo, currentWord):
        if currentWord in memo:
            return memo[currentWord]
        
        maxLength = 1
        
        for i in range(len(currentWord)):
            newWord = currentWord[:i] + currentWord[i+1:]
            if newWord in words:
                currentLength = 1 + self.dfs(words, memo, newWord)
                maxLength = max(maxLength, currentLength)
        
        # add the result to the dictionary
        memo[currentWord] = maxLength
        return maxLength
        
    def longestStrChain(self, words: List[str]) -> int:
        memo = {}
        wordsPresent = set(words)
        
        ans = 0
        for word in words:
            ans = max(ans, self.dfs(wordsPresent, memo, word))
        return ans
        
        