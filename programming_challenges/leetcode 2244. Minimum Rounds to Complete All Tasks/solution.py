class Solution:
    from collections import Counter
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = Counter(tasks)
        
        minimumRounds = 0
        for task, count in freq.items():
            if count == 1:
                return -1
            if count % 3 == 0:
                minimumRounds += count // 3
            else:
                minimumRounds += count // 3 + 1
        
        return minimumRounds