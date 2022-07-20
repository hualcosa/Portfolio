class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            # if the number in position I already is > 0, since the array is sorted
            # it is time to stop
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSumII(nums, i, res)
                
        return res
    def twoSumII(self, nums: List[int], i: int, res: List[list[int]]):
        lo, hi = i + 1, len(nums) - 1
        
        while lo < hi:
            sum_ = nums[i] + nums[lo] + nums[hi]
            
            if sum_ < 0:
                lo += 1
            elif sum_ > 0:
                hi -= 1
            else:
                # add answer to the list of possibilities
                res.append([nums[i], nums[lo], nums[hi]])
                # adjust the pointers
                lo += 1
                hi -= 1
                # making sure we skip repeated elements
                while lo < hi and nums[lo] == nums[lo-1]:
                    lo += 1