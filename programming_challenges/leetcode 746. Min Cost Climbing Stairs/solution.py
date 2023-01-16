class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # initializing dp table
        minimum_cost = [0 for _ in range(len(cost) + 1)]

        # solving the sub problems until we reach the final Solution
        for i in range(2, len(cost) + 1):
            one_step = minimum_cost[i - 1] + cost[i - 1]
            two_steps = minimum_cost[i - 2] + cost[i - 2]
            minimum_cost[i] = min(one_step, two_steps)
        
        # Return the cost of reaching the top floor
        return minimum_cost[-1]
