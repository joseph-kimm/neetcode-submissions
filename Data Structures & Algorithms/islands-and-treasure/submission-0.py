class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        DIRECTIONS = [(0,1), (1,0), (-1,0), (0,-1)]
        ROW = len(grid)
        COL = len(grid[0])

        def isValid(r,c):
            if r < 0 or r >= ROW or c < 0 or c >=COL:
                return False

            return True

        treasures = []

        for r in range(ROW):
            for c in range(COL):

                if grid[r][c] == 0:
                    treasures.append((r,c))

        for a,b in treasures:
            queue = collections.deque()
            queue.append((a,b,1))
            
            while queue: 

                r,c,dist = queue.popleft()

                for i,j in DIRECTIONS:
                    
                    if isValid(r+i, c+j) and grid[r+i][c+j] > dist:
                        grid[r+i][c+j] = dist
                        queue.append((r+i, c+j, dist+1))

        return



                

                
                




                

        