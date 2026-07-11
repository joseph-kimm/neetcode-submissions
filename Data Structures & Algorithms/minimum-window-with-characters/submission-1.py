class Solution:
    def minWindow(self, s: str, t: str) -> str:

        count = {}
        for c in t:
            count[c] = 1 + count.get(c, 0)

        min_sub = [-1,-1]
        min_len = len(s) + 1

        l = 0
        
        curr = 0
        need = len(count)

        for r in range(len(s)):
            c = s[r]

            if c in count.keys():
                count[c] -= 1

                if count[c] == 0:
                    curr += 1

            while curr == need:

                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    min_sub = [l,r]

                if s[l] in count.keys():
                    
                    count[s[l]] += 1

                    if count[s[l]] > 0:
                        curr -= 1
                
                l+= 1

        if min_sub[0] < 0:
            return ""
        else:
            print(min_sub)
            return s[min_sub[0]:min_sub[1]+1]



        