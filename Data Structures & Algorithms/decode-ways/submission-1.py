class Solution:
    def numDecodings(self, s: str) -> int:

        if int(s[0]) == 0:
            return 0

        n = len(s)
        memo = [0] * len(s)
        memo[0] = 1

        for i in range(1,n):

            # ones
            ones = int(s[i])
            if ones != 0:
                memo[i] = memo[i-1]

            # tens
            tens = int(s[i-1:i+1])

            if tens >= 10 and tens < 27:

                if i < 2:
                    memo[i] += 1

                else:
                    memo[i] += memo[i-2]

        return memo[-1]
        

        


        