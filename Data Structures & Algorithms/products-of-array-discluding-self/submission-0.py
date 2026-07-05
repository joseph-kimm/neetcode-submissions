class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        left = [nums[0]] * n  
        right = [nums[-1]] * n

        for i in range(1,n):
            left[i] = left[i-1] * nums[i]

        for j in range(n-2, -1, -1):
            right[j] = right[j+1] * nums[j]

        res = [right[1]]

        for i in range(1,n-1):
            res.append(left[i-1] * right[i+1])

        res.append(left[-2])

        return res



        