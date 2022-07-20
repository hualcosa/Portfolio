class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        count = 0
        for digit in n[2:]:
            if digit == '1':
                count += 1
                
        return count