class Tri:
    def __init__(self):
            n = 38
            self.nums = [0 for _ in range(n)]
            self.nums[1] = self.nums[2] = 1
            for i in range(3, n):
                self.nums[i] = self.nums[i-1] + self.nums[i-2] + self.nums[i - 3]

class Solution:
    def tribonacci(self, n: int) -> int:
        t = Tri()
        return t.nums[n]