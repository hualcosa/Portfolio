class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # If nums1 is larger than nums2, swap the arrays.
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        
        dict_ = {}
        for n in nums1:
            if dict_.get(n, -1) != -1:
                dict_[n] += 1
            else:
                dict_[n] = 1
                
        # Initialize the insertion pointer (k) with zero
        k = 0
        for n in nums2:
            cnt = dict_.get(n, 0)
            # If the current number is in the hash map and count is positive
            if cnt > 0:
                # Copy the number into nums1[k], and increment k
                nums1[k] = n
                k += 1
                # Decrement the count in the hash map
                dict_[n] -= 1
                
        #Return first k elements of nums1        
        return nums1[:k]
            