class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = set()
        
        nums.sort()

        for i in range(len(nums)):
            tar = nums[i]

            l = i+1
            r = len(nums) - 1

            while l < r:
                
                res = nums[l] + nums[r]

                if res + tar > 0:
                    r -= 1

                elif res + tar < 0:
                    l += 1
                
                else:
                    triplet = tuple(sorted([nums[i], nums[l], nums[r]]))
                    ans.add(triplet)
                    l += 1
                    r -= 1

        final = []
        for a in ans:
            final.append(list(a))

        return final



                