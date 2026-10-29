class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = 0
        r = len(nums) - 1
        i = 0

        while i <= r:

            if nums[i] == 2:

                temp = nums[r]
                nums[r] = nums[i]
                nums[i] = temp

                r -= 1
            
            elif nums[i] == 0:

                temp = nums[l]
                nums[l] = nums[i]
                nums[i] = temp

                l+=1
                i+=1

            else:
                i+= 1

        return nums

         