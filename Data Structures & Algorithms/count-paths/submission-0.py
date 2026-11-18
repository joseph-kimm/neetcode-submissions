class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        DIR = [(1,0), (0,1)]

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        queue = collections.deque()

        queue.append((0,0))

        def isValid(r,c):
            if r < m and c < n:
                return True

            return False

        while queue:

            r,c = queue.popleft()

            for i,j in DIR:

                if isValid(r+i,c+j):

                    if dp[r+i][c+j] == 0:
                        queue.append((r+i,c+j))

                    dp[r+i][c+j] += dp[r][c]

        return dp[m-1][n-1]
            


            

        