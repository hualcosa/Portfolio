class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # ^ performs a XOR operation between the two numbers and then the number of ones correspond
        # to the hamming distance
        return bin(x ^ y).count('1')