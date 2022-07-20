class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)

        if str_x[0] == '-':
            result = int(str_x[0] + str_x[:0:-1])
            return result if abs(result) <= 2**31 else 0
        else:
            result = int(str_x[::-1])
            return result if abs(result) <= 2**31 else 0