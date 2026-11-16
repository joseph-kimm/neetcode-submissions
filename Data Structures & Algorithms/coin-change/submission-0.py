class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = [999] * (amount + 1)
        memo[0] = 0

        for i in range(1,amount+1):

            for coin in coins:

                if i - coin >= 0:

                    memo[i] = min(memo[i], memo[i-coin] + 1)

        if memo[-1] == 999:
            return -1

        else:
            return memo[-1]

            
        