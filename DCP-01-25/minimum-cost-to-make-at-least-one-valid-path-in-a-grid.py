class Solution(object):
    def minCost(self, grid):
        RIGHT, LEFT, DOWN, UP = 1, 2, 3, 4
        m, n = len(grid), len(grid[0])
        h, seen = [(0, 0, 0)], set()
        while h:
            (count, r, c) = heapq.heappop(h)
            if (r, c) in seen: continue
            seen.add((r, c))
            if r == m-1 and c == n-1:
                return count
            if r > 0:
                heapq.heappush(h, (count + (grid[r][c] != UP), r-1, c))
            if r < m-1:
                heapq.heappush(h, (count + (grid[r][c] != DOWN), r+1, c))
            if c > 0:
                heapq.heappush(h, (count + (grid[r][c] != LEFT), r, c-1))
            if c < n-1:
                heapq.heappush(h, (count + (grid[r][c] != RIGHT), r, c+1))
        return -1
