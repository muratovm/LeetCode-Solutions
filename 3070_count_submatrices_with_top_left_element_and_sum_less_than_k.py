import numpy as np

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        count = 0
        rows, cols = len(grid), len(grid[0])
        dp_matrix = np.empty((rows, cols))
        
        for y in range(rows):
            for x in range(cols):
                if y == 0 and x == 0:
                    dp_matrix[y][x] = grid[y][x]
                elif x == 0:
                    dp_matrix[y][x] = grid[y][x] + dp_matrix[y-1][x]
                elif y == 0:
                    dp_matrix[y][x] = grid[y][x] + dp_matrix[y][x-1]
                else:
                    dp_matrix[y][x] = grid[y][x] + dp_matrix[y-1][x] + dp_matrix[y][x-1] - dp_matrix[y-1][x-1]
                if dp_matrix[y][x] <= k:
                    count += 1
                        
        #print(dp_matrix)
        
        return count
