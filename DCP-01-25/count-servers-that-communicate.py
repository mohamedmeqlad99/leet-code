class Solution:
    def countServers(self, grid):
        rows, cols = len(grid), len(grid[0])
        row_counts = [0] * rows
        col_counts = [0] * cols

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_counts[r] += 1
                    col_counts[c] += 1

        connected_servers = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (row_counts[r] > 1 or col_counts[c] > 1):
                    connected_servers += 1

        return connected_servers
