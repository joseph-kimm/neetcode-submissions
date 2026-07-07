class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1

        water = 0

        while l < r:

            water = max(water, (min(heights[r], heights[l]) * (r - l)))

            if heights[l] < heights[r]:
                l+= 1

            else:
                r-=1

        return water
            
        