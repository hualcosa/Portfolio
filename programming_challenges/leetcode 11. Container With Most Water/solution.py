class Solution:
    def maxArea(self, height: List[int]) -> int:
        # initialize max to zero
        max_ = 0
        # initialize left and right to extreme ends of the array
        left = 0
        right = len(height) - 1
        # while left < right, loop
        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            max_ = max(max_, currentArea)
            # take the decision regarding which pointer to move
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_
        