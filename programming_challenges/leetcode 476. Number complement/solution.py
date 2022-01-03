class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        reverse = [1 - int(n) for n in binary]
        result = 0
        for pos, exp in enumerate(range(len(reverse) -1, -1, -1)):
            result += reverse[pos] * (2**exp)
        return result