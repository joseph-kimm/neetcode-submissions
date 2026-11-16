class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        posi = nums.copy()
        nega = nums.copy()

        for i in range(1, len(nums)):

            posi[i] = max(posi[i], posi[i-1] * nums[i], nega[i-1] * nums[i])
            nega[i] = min(nega[i], posi[i-1] * nums[i], nega[i-1] * nums[i])

        return max(posi)
        