class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        import numpy as np
        a = np.array(nums)
        return False if len(nums) == len(np.unique(a)) else True