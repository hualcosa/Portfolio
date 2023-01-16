class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def mirrorPal(n):
            # remove leading 0s
            if len(n) > 1:
                n = n.lstrip('0')
            firstLen = len(n) // 2 + len(n) % 2
            first = n[:firstLen]
            # reverse second half
            second = first[::-1]
            # if there was a pivot element, remove the duplicate
            if len(n) % 2:
                second = second[1:]
            return ''.join(first + second)
        firstlen = len(n) // 2 + len(n) % 2
        print(f'inputs to the function: {str(int(n[:firstlen]) - 1) + "9" * (len(n) - firstlen)}')
        print(f'inputs to the function: {str(int(n[:firstlen]) + 1) + "0" * (len(n) - firstlen)}')
        solutions = (
            int(mirrorPal(n)),
            int(mirrorPal(str(int(n[:firstlen]) - 1) + "9" * (len(n) - firstlen))),
            int(mirrorPal(str(int(n[:firstlen]) + 1) + "0" * (len(n) - firstlen)))
        )
        print(solutions)
        best = -10
        for sol in solutions:
            if sol == int(n):
                continue
            if abs(sol - int(n)) < abs(best - int(n)):
                best = sol
            elif  abs(sol - int(n)) == abs(best - int(n)) and sol < best:
                best = sol
        return str(best)

        
