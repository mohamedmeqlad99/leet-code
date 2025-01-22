class Solution:
    def highestPeak(self, isWater):
        inf = 1e9
        r,c = len(isWater),len(isWater[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        height = [[inf]*c for _ in range(r)]
        q = deque()
        for i in range(r):
            for j in range(c):
                if isWater[i][j] == 1:
                    q.append((i,j))
                    height[i][j] = 0
        while q:
            x,y = q.popleft()
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if r > nx > -1 and c > ny > -1 and height[nx][ny] == inf:
                    height[nx][ny] = height[x][y]+1
                    q.append((nx,ny))
        return height
