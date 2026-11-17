class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        memo = [[-1] * (target + 1) for _ in range(n+1)]

        def dfs(i, tar):

            if tar == 0:
                return True

            if i >= n or tar < 0:
                return False

            if memo[i][tar] != -1:
                return memo[i][tar]

            memo[i][tar] = (dfs(i+1, tar) or dfs(i+1, tar-nums[i]))

            return memo[i][tar]

        return dfs(0,target)

            
        