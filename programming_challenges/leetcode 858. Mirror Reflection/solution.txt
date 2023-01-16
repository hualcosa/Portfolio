class Solution:
    import math
    def mirrorReflection(self, p: int, q: int) -> int:

            L = math.lcm(p,q)
            if (L//q)%2 == 0:
                return 2

            return (L//p)%2