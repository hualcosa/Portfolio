class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = []
        for idx1,cur in enumerate(nums):
            needed = target - cur
            try:
                idx2 = nums.index(needed)
                if idx1 != idx2:
                    sol.append(idx1)
                    sol.append(idx2)
                    break
            except ValueError:
                continue
        return sol