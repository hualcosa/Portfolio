class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_ = set()
        for n in nums:
            if n in set_:
                return True
            set_.add(n)
        return False