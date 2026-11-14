class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)
        res = n

        for i in range(n):

            left = i-1
            right = i+1

            while left >= 0 and right < n:
                if s[left] == s[right]:
                    
                    res += 1
                    
                else:
                    break

                left -= 1
                right += 1

            left = i
            right = i+1

            while left >= 0 and right < n:
                if s[left] == s[right]:
                    
                    res += 1

                else:
                    break

                    
                left -= 1
                right += 1

        return res
        

        
        