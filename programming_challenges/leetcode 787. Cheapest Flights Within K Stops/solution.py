class Solution:
    def __init__(self):
        self.adj_matrix = None
        self.memo = {}
        
    def findShortest(self, node, stops, dst, n):
        
        # No need to go any further if the destination is reached
        if node == dst:
            return 0
        
        # Can't go any further if no steps left
        if stops < 0:
            return float("inf")
        
        # if the result of this state is already cached, return it
        if (node, stops) in self.memo:
            return self.memo[(node, stops)]
        
        # Recusive calls over all the neighbors
        ans = float("inf")
        for neighbor in range(n):
            if self.adj_matrix[node][neighbor] > 0:
                ans = min(ans, self.adj_matrix[node][neighbor] + self.findShortest(neighbor, stops - 1, dst, n))
        
        # Cache the result
        self.memo[(node, stops)] = ans
        return ans
            
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        self.adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.memo = {}
        
        for s, d, w in flights:
            self.adj_matrix[s][d] = w
        
        result = self.findShortest(src, k, dst, n)
        return -1 if result == float("inf") else result
        