class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROW = len(grid)
        COL = len(grid[0])

        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        queue = collections.deque()

        island = 0

        def isvalid(r,c):
            if r < 0 or r >= ROW or c < 0 or c >= COL:
                return False

            else:
                return True

        for r in range(ROW):
            for c in range(COL):

                if grid[r][c] == '1':
                    island += 1
                    grid[r][c] = '0'
                    queue.append((r,c))

                    while queue:

                        i,j = queue.popleft()

                        for dr, dc in DIRECTIONS:
                            if isvalid(i+dr, j+dc) and grid[i+dr][j+dc] == '1':
                                queue.append((i+dr, j+dc))
                                grid[i+dr][j+dc] = '0'

        return island


        