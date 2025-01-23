class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        total_communicating_servers = 0
        
        cached_row_sums = [sum(grid[y]) for y in range(len(grid))]
        cached_column_sums = [sum(col) for col in zip(*grid)]

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    #get the sum of the row and column you're on
                    row_sum = cached_row_sums[row]
                    column_sum = cached_column_sums[col]

                    # Check if the server communicates with others
                    if row_sum > 1 or column_sum > 1:
                        total_communicating_servers += 1

        return total_communicating_servers