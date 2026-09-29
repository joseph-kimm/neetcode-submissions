class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        height = len(board)
        width = len(board[0])
        visited = set()

        def backtrack(i, j, n):

            if n == len(word):
                return True

            if min(i,j) < 0 or i >= height or j >= width or word[n] != board[i][j] or (i,j) in visited:
                return False

            visited.add((i,j))
            res = (
                backtrack(i+1,j,n+1) or
                backtrack(i,j+1,n+1) or
                backtrack(i-1,j,n+1) or
                backtrack(i,j-1,n+1)
            )
            visited.remove((i,j))
            return res

        for i in range(height):
            for j in range(width):
                if backtrack(i,j,0):
                    return True

        return False

            


        