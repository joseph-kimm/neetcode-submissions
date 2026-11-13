class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]


        memo = [-1] * n
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])

        def dp(i):

            if memo[i] != -1:
                return memo[i]

            memo[i] = max(dp(i-1), nums[i]+dp(i-2))

            return memo[i]

        dp(n-1)

        return memo[-1]
