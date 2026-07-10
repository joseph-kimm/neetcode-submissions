class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0

        pos = {s[0]:0}
        l = 0
        r = 1

        length = 1

        while r < len(s):
            if s[r] in pos.keys():
                length = max(length, r - l)
                l = max(l, pos[s[r]] + 1)

            
            pos[s[r]] = r
            r += 1

        length = max(length, r - l)

        return length



        