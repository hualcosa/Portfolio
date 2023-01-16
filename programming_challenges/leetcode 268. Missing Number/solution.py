class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)
         # edge case
        if n == 1:
            return 1 if nums[0] == 0 else 0
        
        if nums[0] != 0:
            return 0
        for i in range(n-1):
            if nums[i+1] != nums[i] + 1:
                return nums[i] + 1
        
        return nums[n-1] + 1 # return n