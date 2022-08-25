class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        n = len(nums)
        
        # Sort the generated subset. This will help to identify duplicates.
        nums.sort()
        max_number_of_subsets = 2 ** n
        
        # To store the previously seen sets.
        seen = set()
        
        for subset_index in range(max_number_of_subsets):
            current_subset = []
            hashcode = ''
            for j in range(n):
                mask = 1 << j
                is_set = mask & subset_index
                if is_set:
                    current_subset.append(nums[j])
                    # Generate the hashcode by creating a comma separated string of numbers in the currentSubset.
                    hashcode += str(nums[j]) + ","
            if hashcode not in seen:
                seen.add(hashcode)
                subsets.append(current_subset)
        return subsets