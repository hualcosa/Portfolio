class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        # while number != 0 i.e. while there are still 1 bits in the number, loop 
        while n:
            # get the right-most bit of the original number and shift it
            ret += (n & 1) << power
            # shifts the number to the right i.e Consume the right most bit
            n = n >> 1
            # decrease the power
            power -= 1
        return ret