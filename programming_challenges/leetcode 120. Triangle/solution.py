class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        if N == 1:
            return triangle[0][0]
        
        triangle[1][0] = triangle[1][0] + triangle[0][0]
        triangle[1][1] = triangle[1][1] + triangle[0][0]
        for row in range(2, N):
            for col in range(len(triangle[row])):
                if col == 0:
                    triangle[row][col] = triangle[row][col] + triangle[row-1][col]
                elif col == row:
                    triangle[row][col] = triangle[row][col] + triangle[row-1][col-1]
                else:
                    triangle[row][col] = min(triangle[row][col] + triangle[row-1][col-1],
                                             triangle[row][col] + triangle[row-1][col])
                    
        return min(triangle[-1])
                
        