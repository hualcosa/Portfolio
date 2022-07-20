class Solution:
    def rob(self, nums: List[int]) -> int:
        # handling extreme cases
        if not nums:
            return 0
        
        # Base case initialization
        maxRobbedAmount = [None for _ in range(len(nums) + 1)]
        N = len(nums)
        
        maxRobbedAmount[N], maxRobbedAmount[N-1] = 0, nums[N-1]
        
        # DP table calculations
        for i in range(N-2, -1, -1):
            maxRobbedAmount[i] = max(maxRobbedAmount[i+1], nums[i] + maxRobbedAmount[i+2])
        
        return maxRobbedAmount[0]