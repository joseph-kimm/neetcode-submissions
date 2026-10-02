class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []
        diff_dia = set() # covers one diagonal
        sum_dia = set() # covers other diagonal
        columns = set()
        curr = []

        def backtrack(r):

            if r == n:
                comb = ['.'] * n
                for r,c in curr:
                    row = ['.'] * n
                    row[c] = 'Q'
                    row = ''.join(row)
                    comb[r] = row

                res.append(comb)
                return

            for c in range(n):

                if c not in columns and (r-c) not in diff_dia and (r+c) not in sum_dia:

                    curr.append((r,c))
                    columns.add(c)
                    diff_dia.add(r-c)
                    sum_dia.add(r+c)
                    
                    backtrack(r+1)

                    curr.pop()
                    columns.remove(c)
                    diff_dia.remove(r-c)
                    sum_dia.remove(r+c)

            return

        backtrack(0)
        return res



        