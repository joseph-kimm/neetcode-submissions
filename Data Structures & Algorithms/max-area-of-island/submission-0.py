class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        DIRECTIONS = [(0,1), (1,0), (-1,0), (0,-1)]

        ROW = len(grid)
        COL = len(grid[0])

        max_area = 0

        def is_valid(r,c):

            if r < 0 or r >= ROW or c < 0 or c >= COL:
                return False
            
            return True

        queue = collections.deque()

        for r in range(ROW):
            for c in range(COL):

                if grid[r][c] == 0:
                    continue

                queue.append((r,c))
                grid[r][c] = 0
                curr = 1

                while queue:
                    i,j = queue.popleft()

                    for r_dir, c_dir in DIRECTIONS:

                        if is_valid(i+r_dir, j+c_dir) and grid[i+r_dir][j+c_dir] == 1:
                            queue.append((i+r_dir, j+c_dir))
                            grid[i+r_dir][j+c_dir] = 0
                            curr+= 1

                max_area = max(max_area, curr)

        return max_area


                

        