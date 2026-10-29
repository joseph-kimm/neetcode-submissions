class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [-1] * (n)
        memo[0] = cost[0]
        memo[1] = cost[1]

        def dp(i):

            if memo[i] != -1:
                return memo[i]

            memo[i] = cost[i] + min(dp(i-1), dp(i-2))

            return memo[i]

        dp(n-1)

        print(memo)
        return min(memo[n-1], memo[n-2])

        