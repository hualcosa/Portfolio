class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = []
        n = len(nums)
        mmax = 0
        # populate initial state
        for i in range(n):
            heapq.heappush(pq, (nums[i][0], i, 0)) # (intial_value, list_index, num_index in the list)
            mmax = max(mmax,nums[i][0])
        ans = [pq[0][0], mmax]
        
        while True:
            _, list_index, num_index = heapq.heappop(pq)
            # if current smallest number is the last item in its list, then break
            if num_index == len(nums[list_index]) - 1:
                break
            
            next_num = nums[list_index][num_index+1]
            mmax = max(mmax, next_num)
            # it is necessary to put next_num in the tuple, because the priority
            # queue is going to find the minimum based on it
            heapq.heappush(pq, (next_num, list_index, num_index+1))
            
            if mmax - pq[0][0] < ans[1] - ans[0]:
                ans = [pq[0][0], mmax]
                
        return ans