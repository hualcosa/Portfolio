class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            # we calculate middle this way to avoid overflows
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            else:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        
        # if the algorithm reach this point, it means the number is not in the list
        # hence, we have to add the following rule
        if target < nums[mid]:
            return mid
        else:
            return mid + 1