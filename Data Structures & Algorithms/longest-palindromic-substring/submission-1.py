class Solution:
    def longestPalindrome(self, s: str) -> str:

        res_i = 0
        res_len = 0

        n = len(s)

        for i in range(n):

            left = i-1
            right = i+1

            while left >= 0 and right < n:
                if s[left] == s[right]:
                    
                    if right - left > res_len:

                        res_len = right - left
                        res_i = left

                else:
                    break

                left -= 1
                right += 1

            left = i
            right = i+1

            while left >= 0 and right < n:
                if s[left] == s[right]:
                    
                    if right - left > res_len:

                        res_len = right - left
                        res_i = left

                else:
                    break

                    
                left -= 1
                right += 1

        return s[res_i:res_i+res_len+1]


                
        