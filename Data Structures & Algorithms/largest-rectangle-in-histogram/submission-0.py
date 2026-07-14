class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        r_stack = []
        right_lim = [n] * n

        for i, h in enumerate(heights):
            while r_stack and r_stack[-1][1] > h:
                j = r_stack.pop()[0]
                right_lim[j] = i

            r_stack.append((i,h))

        l_stack = []
        left_lim = [-1] * n
        
        for i in range(n-1,-1,-1):
            h = heights[i]

            while l_stack and l_stack[-1][1] > h:
                j = l_stack.pop()[0]
                left_lim[j] = i

            l_stack.append((i,h))

        print(right_lim)
        print(left_lim)
        res = 0

        for i in range(n):

            res = max(res, heights[i] * (right_lim[i] - left_lim[i] - 1))


        return res