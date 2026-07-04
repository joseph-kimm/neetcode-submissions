class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + '#' + s)
        
        return ''.join(res)


    def decode(self, s: str) -> List[str]:

        if not s:
            return []

        res = []

        left = 0
        right = 0
        while right < len(s):

            if s[right] == '#':
                size = int(s[left:right])
                res.append(s[right+1:right+1+size])
                left = right+1+size
                right = left
            
            right+=1

        return res
