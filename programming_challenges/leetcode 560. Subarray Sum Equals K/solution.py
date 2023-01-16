class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, summ = 0, 0 # initialize count and sum variables
        mapp = {} # hashmap to store how many times each sum has happened (sum_i, # occurences)
        mapp[0] = 1
        for num in nums:
            summ += num
            if (summ - k) in mapp: # if sum[i] - sum[j] = k, it means that the sum from i until j = k. Then we increment the count
                count += mapp[summ - k]
            mapp[summ] = mapp.get(summ, 0) + 1 # update the number of occurrences of summ
        
        return count
        