class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) == 0:
            return True

        count = dict()
        n = len(s1)

        for s in s1:

            count[s] = 1 + count.get(s, 0)

        l = 0
        original = count.copy()

        for r in range(len(s2)):

            if s2[r] in count.keys():
            
                count[s2[r]] -= 1

                if count[s2[r]] == 0 and (r - l + 1) == n:
                    return True
            
                while count[s2[r]] < 0:
                    count[s2[l]] += 1
                    l += 1

            else:
                count = original.copy()
                l = r+1
        
            
        return False
        
            
