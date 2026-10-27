class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        DIR = [(0,1), (1,0), (0,-1), (-1,0)]

        ROW = len(grid)
        COL = len(grid[0])
        
        def isValid(r,c):

            if r < 0 or r >= ROW or c < 0 or c >= COL:
                return False

            return True

        queue = collections.deque()
        fresh = set()

        for i in range(ROW):
            for j in range(COL):

                if grid[i][j] == 2:
                    queue.append((i,j,0))

                elif grid[i][j] == 1:
                    fresh.add((i,j))

        time = 0

        while queue:
            r,c, time = queue.popleft()

            for i,j in DIR:
                if isValid(r+i, c+j) and grid[r+i][c+j] == 1:
                    grid[r+i][c+j] = 2
                    fresh.remove((r+i, c+j))
                    queue.append((r+i, c+j, time+1))

        if fresh:
            return -1
        
        else:
            return time




                
