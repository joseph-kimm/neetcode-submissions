class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def palindrome(string,l,r):
            while l <= r:
                if (string[l] != string[r]):
                    return False

                l += 1
                r -= 1

            return True


        def backtrack(start):

            if start == len(s):
                res.append(part[:])

            for i in range(start, len(s)):

                if palindrome(s, start,i):
                    part.append(s[start:i+1])
                    print(s[start:i+1])
                    backtrack(i+1)
                    part.pop()

        
            return

        
        backtrack(0)
        return res

