class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_ = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in map_.keys():
                return [i, map_[complement]]
            map_[nums[i]] = i
        
        # In case there is no solution, returns None
        return None