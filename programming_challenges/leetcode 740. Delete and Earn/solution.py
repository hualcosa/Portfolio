class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_number = 0
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)
            
        @cache
        def max_points(num):
            if num == 0:
                return 0
            if num == 1:
                return points[1]
            
            return max(max_points(num - 1), points[num] + max_points(num - 2))
        
        return max_points(max_number)