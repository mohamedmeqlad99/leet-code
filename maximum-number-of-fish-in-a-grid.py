from collections import deque

class Solution(object):
    def findMaxFish(self, grid):
        def bfs(r, c):
            q = deque([(r, c)])
            visited[r][c] = True
            fish_count = 0
            while q:
                x, y = q.popleft()
                fish_count += grid[x][y]
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] > 0:
                        visited[nx][ny] = True
                        q.append((nx, ny))
            return fish_count

        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        max_fish = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0 and not visited[r][c]:
                    max_fish = max(max_fish, bfs(r, c))

        return max_fish
